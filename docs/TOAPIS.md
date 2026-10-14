# Native community ToAPIs image tool

`toapis_image` is an additive `BaseTool`. Register/discover normally; require this
exact tool and hosting_provider=toapis when using image_selector. The VIP low/1K/n=1 route and the six comparison generation tiers are enabled. See tools/toapis_models.py. Default origin https://toapis.com.

| Stage | Route | Handling |
|---|---|---|
| Quote | GET /v1/pricing?model=gpt-image-2-vip | Bearer; exact tier; $0.10/task demo sub-cap |
| Reference | POST /v1/uploads/images | Bearer; multipart file; local PNG/JPEG/WebP |
| Submit | POST /v1/images/generations | Bearer; model, prompt, ratio size, resolution, quality, n, reference_images |
| Query | GET /v1/images/generations/{id} | Bearer; status; no automatic generation resubmission |
| Result | result.data[0].url | No Authorization header; accepted CDN User-Agent; save PNG |

`generation_mode=edit` needs 1–4 local image_path/image_paths. All references
are uploaded, then supplied via reference_images to the generations route.
Masks and transparent outputs are not mapped. No OpenAI /images/edits shortcut.

Persist TOAPIS_STATE_DIR privately and use a stable run_id when recovering a task.
The same input/run/key fingerprint resumes the task. Use a new run_id only when
another paid output is intended. A submission without a task ID is ambiguous;
reconcile the backend before a new POST. Never place the key in result URL requests.

The tool result reports quote separately from billing. It returns cost_usd=None
while settlement is unavailable. Account-owner confirmation is a separate
evidence field and does not overwrite the original API billing=null.

Scope: native ToolRegistry registration + provider execution validated. Full
registry.discover, image_selector execution, agent production, video and voice
remain untested. Production must follow upstream AGENT_GUIDE and its pipelines.

## Model-specific generation mapping

- gpt-image-2-vip: request and observed output in examples/toapis/MODEL_COMPARISON.md.
- gpt-image-2: request and observed output in examples/toapis/MODEL_COMPARISON.md.
- gpt-image-2.5-flare: request and observed output in examples/toapis/MODEL_COMPARISON.md.
- gemini-nano-banana-2.1: request and observed output in examples/toapis/MODEL_COMPARISON.md.
- doubao-seedream-5-0-pro: request and observed output in examples/toapis/MODEL_COMPARISON.md.
- gemini-3.1-flash-image-preview: request and observed output in examples/toapis/MODEL_COMPARISON.md.
- nano_banana: request and observed output in examples/toapis/MODEL_COMPARISON.md.

Only VIP reference edits have been validated. Other models reject local references. Standard GPT and Seedream send matching top-level and metadata resolution; actual returned dimensions are reported independently. The API may return JPEG; raw originals are preserved and PNGs are serialized locally.
