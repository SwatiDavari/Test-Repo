Infrastructure Register
============================

The register satisfying :need:`ORG_INFRA_002` — one ``infra`` need per
infrastructure element this organization's projects actually depend on.
Every entry below was checked directly against the repo (workflow files,
config files, and the device this repo lives on), not assumed.

This is a different axis from :doc:`../../org_tools/tool_register`: that
page tracks the *software* invoked in CI (compilers, linters, Sphinx);
this page tracks the *platform* that software runs on (compute, hosting,
dev environment).

.. infra:: CI/CD compute
   :id: INFRA_CI_COMPUTE
   :links: ORG_INFRA_002
   :provider: GitHub Actions — ``ubuntu-latest`` hosted runners
   :acquisition: SaaS, included with the GitHub organization plan; no self-hosted runners
   :availability_note: Relies entirely on GitHub Actions' own SLA/status page. No independent monitoring, no backup runner pool.
   :used_in: all 8 workflow files under .github/workflows/

   Every ``ci*.yml`` and ``docs.yml`` job runs on this.

.. infra:: Docs hosting
   :id: INFRA_DOCS_HOSTING
   :links: ORG_INFRA_002
   :provider: GitHub Pages
   :acquisition: SaaS, included with the repo; enabled via the ``deploy-pages`` job in docs.yml
   :availability_note: Relies entirely on GitHub Pages' own SLA/status page. No independent monitoring.
   :used_in: docs.yml — deploy-pages job

   Serves the built Sphinx HTML for both this project and, separately,
   whatever ``Needs/`` publishes on its own.

.. infra:: Developer workspace baseline
   :id: INFRA_DEV_WORKSPACE
   :links: ORG_INFRA_002
   :provider: Local developer machines (checked into the repo as config, not a hosted service)
   :acquisition: Checked-in file (``qorix-engg.code-workspace``) — VS Code settings, recommended extensions, ``.venv`` interpreter path
   :availability_note: n/a — local file, no shared/hosted dependency, so no availability concern in the ISO 15288 sense
   :used_in: whole repo, any contributor opening it in VS Code

   Exists, but nothing under ``org_governance/`` referenced it until
   :doc:`org_project_enabling_requirements` did.

.. needtable::
   :types: infra
   :columns: id, title, provider, acquisition
   :style: table
