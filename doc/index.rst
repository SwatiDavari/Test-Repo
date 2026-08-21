Docs
=======

Published documentation deliverables for this repo, as distinct from
``needs/`` (traceable requirements) and ``source/`` (per-language source
and coding-guideline READMEs). See ``doc/README.md`` for how each
subfolder is meant to be used and built.

**2026-08-21: added ``myst_parser`` so ``release_notes/`` can actually
build** — it's plain Markdown and previously wasn't part of any Sphinx
build at all. ``manuals/`` briefly moved to ``needs/user_guide/`` the
same day and moved back here shortly after — see ``doc/README.md`` for
why (the safety manual's directive types are now registered in this
project's own ``conf.py`` instead).

.. toctree::
   :maxdepth: 1

   manuals/user_manual
   manuals/safety/safety_user_manual
   release_notes/v0.1.0
   errata/index
