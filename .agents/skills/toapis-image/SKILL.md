---
name: toapis-image
description: Community ToAPIs image tool contract and reference-guided storyboard stills.
---

For production, follow AGENT_GUIDE.md and the selected pipeline. This fork adds
one image provider; video, voice, and the complete production pipeline were not
validated by this tutorial. For provider smoke tests use examples/toapis/demo.py.

Require exact tool `toapis_image`, provider `toapis`, model `gpt-image-2-vip`.
VIP uses low/1K/n=1. Other explicit generation-only options and their tiers are in tools/toapis_models.py; see examples/toapis/MODEL_COMPARISON.md. Estimate cost queries authenticated pricing;
an estimate is not a settled charge. Credentials indicate configuration only.

Write a specific scene prompt with subject identity, setting, framing, light,
materials and explicit exclusions. When editing, state what must remain and what
changes. No guarantee of exact character identity or pixel-preserving masking.

Bearer auth uses TOAPIS_API_KEY, origin TOAPIS_BASE_URL=https://toapis.com.
Pixel hints map to aspect ratios; actual returned dimensions must be inspected.
Local references upload to /v1/uploads/images then reference_images are sent to
/v1/images/generations. Submit once, query /v1/images/generations/{id}, download
the result URL without an Authorization header. No /images/edits shortcut.

Private task receipts persist before submission. The same run ID and input resume
the existing task; a new run_id explicitly requests another billed generation.
An ambiguous submission without an ID requires dashboard reconciliation.
Masks, transparency, n>1, unlisted models and tiers are rejected before POST.
