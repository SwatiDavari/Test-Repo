#!/bin/bash
# Build a Qorix-branded PDF from an .rst file using the shared LaTeX template.
# Usage: build_pdf.sh <input.rst> <output.pdf> <title> <configid> <version> <docdate> <status> <preparedby> <preparedloc>
set -euo pipefail

SRC="$1"; OUT="$2"; TITLE="$3"; CONFIGID="$4"; VERSION="$5"; DOCDATE="$6"; STATUS="$7"; PREPAREDBY="$8"; PREPAREDLOC="$9"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# _static/ lives next to the .rst source (e.g. doc/manuals/_static), NOT
# inside this script's own _pdf_template/ directory -- resolve it relative
# to $SRC, matching the same convention the .rst files themselves use
# (`.. image:: _static/...`), rather than relative to this script.
STATIC_DIR="$(cd "$(dirname "$SRC")" && pwd)/_static"
if [ ! -f "$STATIC_DIR/qorix_logo.png" ]; then
  echo "ERROR: $STATIC_DIR/qorix_logo.png not found -- check STATIC_DIR resolution" >&2
  exit 1
fi
TMP_TEX="$(mktemp --suffix=.tex)"

# Fail fast on any image the .rst references but that doesn't actually exist
# on disk -- a missing file otherwise reaches xelatex as an
# \includegraphics with unknown dimensions and dies deep in the LaTeX pass
# with an opaque "Division by 0" error instead of a clear message here.
SRC_DIR="$(dirname "$SRC")"
while IFS= read -r img; do
  img="${img%$'\r'}"
  [ -z "$img" ] && continue
  if [ ! -f "$SRC_DIR/$img" ]; then
    echo "ERROR: $SRC references image '$img' but $SRC_DIR/$img does not exist" >&2
    exit 1
  fi
done < <(grep -oE '\.\. (image|figure):: .+' "$SRC" | sed -E 's/\.\. (image|figure):: //')

pandoc "$SRC" \
  --template="$SCRIPT_DIR/qorix-template.latex" \
  --resource-path="$(dirname "$SRC"):$SCRIPT_DIR:$STATIC_DIR" \
  -M title="$TITLE" -M configid="$CONFIGID" -M version="$VERSION" -M docdate="$DOCDATE" \
  -M status="$STATUS" -M preparedby="$PREPAREDBY" -M preparedloc="$PREPAREDLOC" \
  -M logo="$STATIC_DIR/qorix_logo.png" \
  -M covergraphic="$STATIC_DIR/qorix_cover_graphic.png" \
  -M toc=true \
  -s -o "$TMP_TEX"

# Color table header rows cyan: pandoc emits booktabs rules as
# "\toprule\noalign{}" / "\midrule\noalign{}" / "\bottomrule\noalign{}" --
# colortbl's \rowcolor cannot be chained into that via macro redefinition,
# so rewrite the generated .tex directly instead. Tables built with
# :header-rows: 0 (e.g. the metadata table) emit an *empty* header --
# \toprule\noalign{} immediately followed by \endhead with no row (and no
# \midrule at all) between them -- coloring that produces a stray black
# bar, so that case is collapsed to a plain \hline instead, uncolored.
perl -0777 -pi -e '
  s/\\toprule\\noalign\{\}\n\\endhead/\\hline\n\\endhead/g;
  s/\\toprule\\noalign\{\}/\\rowcolor{qorixcyan}/g;
  s/\\midrule\\noalign\{\}/\\hline/g;
  s/\\bottomrule\\noalign\{\}/\\hline/g;
' "$TMP_TEX"

OUTDIR="$(dirname "$OUT")"
BASE="$(basename "$TMP_TEX" .tex)"
xelatex -interaction=nonstopmode -output-directory="$(dirname "$TMP_TEX")" "$TMP_TEX" >/tmp/xelatex_run.log 2>&1
xelatex -interaction=nonstopmode -output-directory="$(dirname "$TMP_TEX")" "$TMP_TEX" >>/tmp/xelatex_run.log 2>&1
mv "$(dirname "$TMP_TEX")/$BASE.pdf" "$OUT"
echo "Built $OUT"
