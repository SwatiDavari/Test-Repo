Docs
=======

Published documentation deliverables for this repo, as distinct from
``needs/`` (traceable requirements) and ``source/`` (per-language source
and coding-guideline READMEs). See ``doc/README.md`` for how each
subfolder is meant to be used and built.

**2026-08-21: added ``myst_parser`` so this section can actually build.**
``release_notes/`` is plain Markdown and previously wasn't part of any
Sphinx build at all — no Markdown parser was registered. Registered here
because the content is small (one file per release) and didn't need
rewriting to RST. The product/safety user manuals that used to live
under a sibling ``manuals/`` folder here have moved to
``needs/user_guide/`` — see ``doc/README.md`` and
``needs/user_guide/index.rst`` for why.

.. toctree::
   :maxdepth: 1

   release_notes/v0.1.0
   errata/index
