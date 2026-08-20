#!/bin/bash
# Build the Qorix-branded Safety User Manual PDF from
# communication/safety_user_manual.rst via Sphinx's own LaTeX builder
# (required -- Sphinx-Needs directives like .. safefeat:: are NOT understood
# by plain Pandoc, which silently drops their content).
#
# Run from inside needs/. Produces _build/latex/qorix_module_a_safety_user_manual.pdf
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/needs" 2>/dev/null || cd needs

rm -rf _build/latex
sphinx-build -b latex . _build/latex

cd _build/latex

# Sphinx's sphinxhowto/sphinxmanual classes hard-code \pagestyle{plain}
# before the TOC and \pagestyle{normal} right after it, unconditionally
# overriding the fancyhdr header/footer set up in conf.py's
# latex_elements['preamble']. Force both to the fancy style directly in
# the generated .tex (macro-level \let redefinition via \AtBeginDocument
# does not reliably win against Sphinx's later explicit \pagestyle calls).
sed -i \
  -e 's/\\pagestyle{plain}/\\pagestyle{fancy}/g' \
  -e 's/\\pagestyle{normal}/\\pagestyle{fancy}/g' \
  qorix_module_a_safety_user_manual.tex

xelatex -interaction=nonstopmode qorix_module_a_safety_user_manual.tex
xelatex -interaction=nonstopmode qorix_module_a_safety_user_manual.tex

echo "Built _build/latex/qorix_module_a_safety_user_manual.pdf"
