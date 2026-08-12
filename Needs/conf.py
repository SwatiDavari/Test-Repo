extensions = ["sphinx_needs"]

project = "Qorix Engineering Processes Needs"
master_doc = "index"

# --- Need types = the pptx "Cluster" (glob/Feat/Comp/Unit -> int/req/arc/des),
# each cross-referenced to the standard process/work-product it corresponds
# to. See ../STANDARDS.md for the full crosswalk and rationale. ---
needs_types = [
    dict(directive="sys", prefix="SYS_", color="#BFD8D2", style="node",
         title="System Requirement — ASPICE SYS.2 / ISO 15288 System Requirements Definition"),
    dict(directive="feat", prefix="FEAT_", color="#FEDCD2", style="node",
         title="Feature / Software Requirement — ASPICE SWE.1 / ISO 15288 Requirements Definition"),
    dict(directive="comp", prefix="COMP_", color="#DF744A", style="node",
         title="Component / Software Architecture — ASPICE SWE.2 / ISO 15288 Architecture Definition"),
    dict(directive="unit", prefix="UNIT_", color="#DCB239", style="node",
         title="Unit / Detailed Design — ASPICE SWE.3 / ISO 15288 Design Definition"),

    # ISO 26262 functional safety chain — not covered by ASPICE or ISO 15288
    # on its own; layered onto the same needs graph so a safety requirement
    # can link straight into the sys/feat/comp/unit chain above.
    dict(directive="sg", prefix="SG_", color="#B71C1C", style="node",
         title="Safety Goal — ISO 26262-3 clause 6 (HARA)"),
    dict(directive="fsr", prefix="FSR_", color="#D32F2F", style="node",
         title="Functional Safety Requirement — ISO 26262-3 clause 8"),
    dict(directive="tsr", prefix="TSR_", color="#E57373", style="node",
         title="Technical Safety Requirement — ISO 26262-4 clause 6 / ISO 26262-6"),

    # Upstream-of-sys needs: raw stakeholder/business/operational needs
    # (Needs/*-needs.rst) that sys requirements are elicited from. Not
    # part of the ASPICE/ISO 15288 requirements-definition chain itself —
    # this is the pre-requirements input layer feeding it. Added because
    # business-needs.rst / operational-needs.rst / stakeholder-needs.rst
    # already use this directive live in this repo; previously
    # unregistered, which made any build touching them fail outright with
    # "Unknown directive type eng_need".
    dict(directive="eng_need", prefix="NEED_", color="#8E9AAF", style="node",
         title="Stakeholder / Business / Operational Need"),

    # ISO 26262-6 Safety User Manual content — the customer-facing safety
    # feature / recommendation / restriction tables previously hand-maintained
    # in Qorix_SafetyUserManual.docx per module. Modeled as needs so each
    # entry traces to the fsr/tsr chain above (:links:) instead of living as
    # unlinked prose in a Word table. Module-specific IDs (e.g. COM_FEA_001)
    # still satisfy needs_id_regex below — the prefix here is just the
    # auto-id default, not enforced per-module.
    dict(directive="safefeat", prefix="SAFEFEAT_", color="#7B1FA2", style="node",
         title="Module Safety Feature — ISO 26262-6 Safety User Manual"),
    dict(directive="rec", prefix="REC_", color="#F57F17", style="node",
         title="Operational Recommendation — ISO 26262-6 Safety User Manual"),
    dict(directive="res", prefix="RES_", color="#EF6C00", style="node",
         title="Operational Restriction — ISO 26262-6 Safety User Manual"),
]

# Free-text fields on needs.
# `standard` and `derives_from` are intentionally NOT registered as
# needs_extra_links: elsewhere in this repo (organisation/governance/, governed by
# the root conf.py) derives_from mixes real need ids with external
# standard-clause citations that have no matching need — as a real link
# that would fail needs_report_dead_links. Kept as free text here too, for
# the same reason and for consistency between the two conf.py files, even
# though every derives_from usage actually inside Needs/ today happens to
# cite a real eng_need id.
needs_fields = {
    "standard": {
        "description": "Standard/clause this need satisfies",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "derives_from": {
        "description": "Upstream need id or external standard clause this "
                        "requirement derives from (free text — not "
                        "dead-link-checked)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "kind": {
        "description": "Need classification used by eng_need, e.g. 'need'",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "domain": {
        "description": "Requirement/need domain, e.g. functional, "
                        "operational, business",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "lifecycle_stage": {
        "description": "Lifecycle stage this need belongs to, e.g. "
                        "stakeholder_needs",
        "schema": {"type": "string"},
        "nullable": True,
    },

    # Safety User Manual fields (safefeat / rec / res). Free text, same
    # rationale as `derives_from` above: these frequently cite DFMEA action
    # IDs and other identifiers that live outside the needs graph, so a
    # real link type would trip needs_report_dead_links on legitimate
    # citations.
    "rationale": {
        "description": "safefeat: rationale for claiming safety in this feature",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "use_case": {
        "description": "safefeat: use case for the safety feature",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "dependency": {
        "description": "safefeat: internal or external dependency, if any",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "input_reference": {
        "description": "rec/res: Safety Requirement ID or Safety Analysis "
                        "ID (e.g. a DFMEA action ID) this entry originates "
                        "from",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "req_type": {
        "description": "rec/res: Timing, Execution Sequence, Resource, "
                        "Performance, Implementation, External Dependency, "
                        "Configuration, etc.",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "actions": {
        "description": "rec/res: recommended action for the integrator",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "impact": {
        "description": "rec/res: impact of non-adherence to the "
                        "recommended action",
        "schema": {"type": "string"},
        "nullable": True,
    },
}

# Every need must declare at least one upstream link via the built-in
# `links` option (sys <- feat <- comp <- unit, sg <- fsr <- tsr). A broken
# or missing link, or a duplicate id, fails the build below with -W.
needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"

# Fail the build (not just warn) on unresolvable need links, e.g. a
# `:links:` field pointing at an id that doesn't exist.
needs_report_dead_links = True

# --- Qorix-branded PDF export (Safety User Manual) -------------------------
# Produces a second, standalone LaTeX/PDF document from just
# communication/safety_user_manual.rst (still resolving :links:/:need:
# cross-references against the full needs graph loaded above), styled to
# match Qorix_SafetyUserManual.docx: cover page, repeating header
# (Config ID / Version / Date), repeating footer (logo + confidentiality
# line + page number), and cyan table header rows.
latex_engine = "xelatex"
latex_table_style = ["booktabs", "colorrows"]
latex_additional_files = [
    "_static/qorix_logo.png",
    "_static/qorix_cover_graphic.png",
]
latex_documents = [
    ("index", "qorixengineeringprocessesneeds.tex",
     "Qorix Engineering Processes Needs", "QORIX GmbH", "manual"),
    ("communication/safety_user_manual", "qorix_module_a_safety_user_manual.tex",
     "Qorix Module A Safety User Manual", "QORIX GmbH", "howto"),
]
latex_elements = {
    "fontpkg": r"""
\usepackage{fontspec}
\setmainfont{Carlito}
""",
    "preamble": r"""
\usepackage{colortbl}
\definecolor{qorixcyan}{HTML}{00FFFF}
\definecolor{qorixblue}{HTML}{3A00F5}
\definecolor{qorixgray}{HTML}{F2F2F2}
\sphinxsetup{
  TableRowColorHeader={HTML}{00FFFF},
  TableRowColorOdd={HTML}{FFFFFF},
  TableRowColorEven={HTML}{FFFFFF}
}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.6pt}
\fancyhead[L]{\small\qorixconfigid}
\fancyhead[C]{\small\qorixversion}
\fancyhead[R]{\small\qorixdocdate}
\fancyfoot[L]{\raisebox{-0.3\height}{\includegraphics[height=10pt]{qorix_logo.png}}}
\fancyfoot[C]{\small Restricted \& Confidential \textcopyright{}QORIX GmbH}
\fancyfoot[R]{\small\thepage}
% Sphinx's own "howto"/"manual" classes switch to \pagestyle{plain} before
% the table of contents and \pagestyle{normal} right after it,
% unconditionally overriding whatever style was active. Make both of
% those page styles behave exactly like our fancy header/footer (deferred
% to \AtBeginDocument since \ps@fancy itself is only fully defined once
% fancyhdr finishes initializing at \pagestyle{fancy} above).
\AtBeginDocument{\let\ps@plain\ps@fancy\let\ps@normal\ps@fancy}
\newcommand{\qorixconfigid}{<Config ID>}
\newcommand{\qorixversion}{<X.Y.Z>}
\newcommand{\qorixdocdate}{dd-Mmm-YYYY}
\newcommand{\qorixstatus}{Draft}
\newcommand{\qorixpreparedby}{QORIX GmbH}
\newcommand{\qorixpreparedloc}{Germany}
""",
    "maketitle": r"""
\begin{titlepage}
\newgeometry{margin=0cm}
\begin{minipage}[t]{0.62\textwidth}
\vspace{2.2cm}\hspace{1.6cm}
\begin{minipage}{0.85\textwidth}{\LARGE\bfseries\makeatletter\@title\makeatother}\end{minipage}
\end{minipage}%
\begin{minipage}[t]{0.38\textwidth}
\vspace{0pt}\hfill\includegraphics[width=0.9\textwidth]{qorix_cover_graphic.png}
\end{minipage}
\vspace{4cm}\hspace{1.6cm}%
\colorbox{qorixcyan}{\begin{minipage}[t][5.6cm][t]{0.3cm}\mbox{}\end{minipage}}%
\colorbox{qorixgray}{\begin{minipage}[t][5.6cm][t]{11.3cm}
\vspace{0.4cm}\hspace{0.4cm}\begin{minipage}{10.5cm}
\textbf{Prepared By:}\\[4pt]
{\Large\qorixpreparedby}\\[2pt]
\qorixpreparedloc\\[16pt]
\begin{tabular}{@{}ll@{}}
CONFIG ID & : \qorixconfigid \\
VERSION   & : \qorixversion \\
DATE      & : \qorixdocdate \\
STATUS    & : \qorixstatus \\
\end{tabular}
\end{minipage}
\end{minipage}}
\end{titlepage}
\restoregeometry
\tableofcontents
\newpage
""",
}
