# Lower-cost OpenMontage image provider


<!-- TOAPIS-MODELS-20261020 -->
## Model support and prices · 2026-10-20

Added standalone API presets: 31 image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid calls while pricing is unavailable. Native provider/UI/import/render acceptance remains as documented in the original guide below.

| Image model / tested preset | Current preset quote / image | Historical example amount / image | Fee evidence |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | Billing log, phase unknown |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | Current-key quote unavailable | **$0.005272/image**<br><sub>Token-metered; current $/M unavailable. This sample is not a fixed image tariff.</sub> | Task receipt settled |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | Billing log, phase unknown |
| qwen-image-3.0<br><sub>1K</sub> | Current-key quote unavailable | **$0.021/image** | Billing log, phase unknown |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | Billing log, phase unknown |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | Billing log, phase unknown |

| Video model | Preset / input | Settled clip charge | File duration | Case USD/s, ascending |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / text-to-video | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>Pricing tariff: $0.025/s</sub> |
| seedance-2-mini | 4s / 480p / first-frame | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>Pricing tariff: $3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / text-to-video | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>Pricing tariff: $5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / text-to-video | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>Pricing tariff: $0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / text-to-video | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>Pricing tariff: $0.064/s</sub> |
| seedance-2 | 4s / 480p / first-frame | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>Pricing tariff: $6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / text-to-video | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>Pricing tariff: $0.08/s</sub> |
| seedance-2-5 | 4s / 480p / text-to-video | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>Pricing tariff: $10/M total tokens</sub> |

Pricing checked 2026-10-20. Image examples are dated 2026-10-17; video examples 2026-10-20. Tables sort by example amount or case USD/s. Presets and input modes differ; this is not a matched-settings quality ranking. Unknown-phase image logs are not confirmed final net settlements. Current quotes and historical amounts are separate. Video charges are billing=settled; case USD/s divides charge by actual file duration, never processing time. Token tariffs appear in small text and do not imply a fixed per-second price.

gpt-image-2(VIP) starts at $0.0019/image; this low/1K preset is $0.0019/image. The standalone sampler has 31 historically successful image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid submission until an exact price is available.

[Local sampler](toapis-models/README.md) · [Full price table](PRICING.md) · [Original media and fee evidence](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/model-support-2026-10-20)

Original project examples, historical charges and integration instructions follow. Historical amounts are not rewritten as today’s quotes.

<!-- /TOAPIS-MODELS-20261020 -->

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## Tested model types, presets and costs

Updated October 16, 2026. These are tested historical presets/prices; this addition does not relabel the original batch below.

| Model (API ID) | Type | Tested preset | Unit quote | Confirmed unit charge | Count |
|---|---|---|---:|---:|---:|
| gpt-image-2(VIP) (`gpt-image-2-vip`) | Image | low / 1K / n=1 | $0.0019/image | $0.0019 | 3 |
| nano_banana | Image | 1K | $0.012/image | $0.012 | 1 |
| gpt-image-2 | Image | 1K / n=1 | $0.015/image | $0.015 | 2 |
| Nano Banana 2.1 (`gemini-nano-banana-2.1`) | Image | 1K / n=1 | $0.015/image | $0.015 | 1 |
| gpt-image-2.5-flare | Image | high / 1K / n=1 | $0.0225/image | $0.0225 | 1 |
| gemini-3.1-flash-image-preview | Image | 1K | $0.025/image | $0.025 | 1 |
| doubao-seedream-5-0-pro | Image | medium quoted / requested 1K | $0.042857/image | $0.042856 | 2 |

Confirmed original image/video example subtotal: **$0.195912**.

BaseTool registration and image-tool execution validated. Upstream has video tooling; a native ToAPIs video tool remains unvalidated.

gpt-image-2(VIP), **from $0.0019/image**; the tested low/1K preset here is **$0.0019/image**. Different models, qualities and resolutions do not imply equivalent results.
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->


[简体中文](README_zh-CN.md) · [Model pricing & API access](https://go2v.toapis.com/om14ge) · [Original OpenMontage](https://github.com/calesthio/OpenMontage)



**$0.0019/image** for ToAPIs `gpt-image-2-vip`, `low / 1K / n=1`. Generate an original orbital rover scene, then two reference-guided storyboard variations through a native OpenMontage `BaseTool`. 3 image-2(vip) images: **$0.0057 actually charged** (1.14 credits).



## Demo



![Three real storyboard outputs](assets/overview-en.png)



| Scene | Operation | Actual output | Download |

|---|---|---|---|

| orbital-arrival | Text-to-image | 1024×1024 PNG | [Image](examples/toapis/results/orbital-arrival/result.png) · [Evidence](examples/toapis/results/orbital-arrival/evidence.json) |

| habitat-interior | Reference-guided edit | 1024×1024 PNG | [Image](examples/toapis/results/habitat-interior/result.png) · [Evidence](examples/toapis/results/habitat-interior/evidence.json) |

| blue-hour-departure | Reference-guided edit | 1024×1024 PNG | [Image](examples/toapis/results/blue-hour-departure/result.png) · [Evidence](examples/toapis/results/blue-hour-departure/evidence.json) |



Original prompts: [cases.json](examples/toapis/cases.json). Actual calls dated 2026-10-14. Model generations are stochastic; the recipe is repeatable, pixel-identical output is not promised.



## Seven model options: real examples, prices and charges



All 11 calls actually charged **$0.195912**.



![Model comparison A](assets/comparison-a-en.png)



![Model comparison B](assets/comparison-b-en.png)



| Model / API route | Tier | Quote / image | Actual charge / sample | Actual px | Client seconds | Output |

|---|---|---|---|---|---|---|

| [`gpt-image-2-vip`](https://go2v.toapis.com/om14ge) | low / requested 1K | $0.0019 | $0.0019 | 1024×1024 / PNG | not recorded / recovered | [PNG](examples/toapis/results/orbital-arrival/result.png) · [record](examples/toapis/results/orbital-arrival/evidence.json) |

| [`nano_banana`](https://x.toapis.com/om14nb) | — / requested 1K | $0.012 | $0.012 | 1024×1024 / PNG | 14.41 | [PNG](examples/toapis/comparison/nano_banana/result.png) · [record](examples/toapis/comparison/nano_banana/evidence.json) |

| [`gpt-image-2`](https://toapis.com/en/model-guide/gpt-image-2?utm_campaign=om14i2) | — / requested 1K | $0.015 | $0.015 | 1280×1280 / PNG | 115.69 | [PNG](examples/toapis/resolution-probes/gpt-image-2/result.png) · [record](examples/toapis/resolution-probes/gpt-image-2/evidence.json) |

| [`gemini-nano-banana-2.1`](https://toapis.com/en/model-guide/gemini-nano-banana-2-1?utm_campaign=om14n1) | — / requested 1K | $0.015 | $0.015 | 1024×1024 / JPEG → PNG | 32.38 | [PNG](examples/toapis/comparison/gemini-nano-banana-2.1/result.png) · [Original JPEG](examples/toapis/comparison/gemini-nano-banana-2.1/result-original.jpg) · [record](examples/toapis/comparison/gemini-nano-banana-2.1/evidence.json) |

| [`gpt-image-2.5-flare`](https://im25.toapis.com/om14f) | high / requested 1K | $0.0225 | $0.0225 | 1024×1024 / PNG | 60.2 | [PNG](examples/toapis/comparison/gpt-image-2.5-flare/result.png) · [record](examples/toapis/comparison/gpt-image-2.5-flare/evidence.json) |

| [`gemini-3.1-flash-image-preview`](https://nano2.toapis.com/om14n2) | — / requested 1K | $0.025 | $0.025 | 1024×1024 / PNG | 32.77 | [PNG](examples/toapis/comparison/gemini-3.1-flash-image-preview/result.png) · [record](examples/toapis/comparison/gemini-3.1-flash-image-preview/evidence.json) |

| [`doubao-seedream-5-0-pro`](https://toapis.com/en/model-guide/doubao-seedream-5-0-pro?utm_campaign=om14s5) | medium (quote) / requested 1K | $0.042857 | $0.042856 | 2048×2048 / JPEG → PNG | 86.95 | [PNG](examples/toapis/resolution-probes/doubao-seedream-5-0-pro/result.png) · [Original JPEG](examples/toapis/resolution-probes/doubao-seedream-5-0-pro/result-original.jpg) · [record](examples/toapis/resolution-probes/doubao-seedream-5-0-pro/evidence.json) |



[Full comparison, resolution audit and reproduction commands](examples/toapis/MODEL_COMPARISON.md). Same prompt, different quality tiers; single examples are not a performance ranking.



## API pricing and this demo's spend




<!-- TOAPIS-IMAGE-SAMPLES-20261017 -->
## Same prompt: 8 image models and example costs

Tested **2026-10-17**: the same text-to-image prompt, one output per example, sorted by example amount from low to high. **gpt-image-2(VIP) starts at $0.0019/image; low/1K here is $0.0019/image.**

Each row identifies a task settlement receipt or an account billing log. Unknown-phase logs are not final net settlements; model/time-window candidates are not confirmed task matches. Catalog rates are historical quotes, not locked prices. gpt-image-2.5-flare-vip is token-metered: **$0.005272 is this image's settled charge**, not a fixed image rate. It is a different API ID from gpt-image-2.5-flare. Qwen has no returned key quote; only its example log amount is shown.

The prompt is shared, but quality defaults and output dimensions differ. Request presets and actual pixels are listed separately. Seedream Pro requested 1K with quality omitted (medium quoted), and returned 2048×2048. These are independent ToAPIs API asset tests; they do not extend any project's native-provider, UI, import or video validation, and are not added to the historical project subtotal below.

| Model / API ID | Request preset → actual pixels | Catalog rate (2026-10-17) | Example amount USD ↑ | Cost evidence | Real output |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | Token-based; key quote unavailable | **$0.005272** | Task receipt: settled | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key quote unavailable | **$0.021** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/overview-en.jpg)

[Shared prompt, originals and cost sources](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/image-model-samples-2026-10-17/README.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

<!-- /TOAPIS-IMAGE-SAMPLES-20261017 -->

| Model | Tier | Current price | This demo |

|---|---|---|---|

| `gpt-image-2-vip` | `low / 1K / n=1` | **$0.0019/image** | $0.0057 / 3 images, backend-confirmed charge |



The VIP storyboard tier below and the tested alternatives in the comparison are priced here. Quote checked 2026-10-14 through the authenticated pricing API. 1 credit = $0.005. Original API `billing: null` is preserved in the sanitized evidence; settled charges come from the account owner's backend confirmation when available. [Price snapshot](examples/toapis/pricing.json).



## Reproduce



Python 3.10+. The full upstream source remains in this real fork. For this single image tool, the small dependency list below is sufficient. Full studio use follows the upstream requirements and [AGENT_GUIDE](AGENT_GUIDE.md).



```bash

git clone --depth 1 https://github.com/ToAPIs-2025/lower-cost-openmontage-toapis.git

cd lower-cost-openmontage-toapis

python -m pip install -r requirements-toapis.txt

python examples/toapis/demo.py

# Configure TOAPIS_API_KEY privately, then run the charged demo:

python examples/toapis/demo.py --live

python -m unittest discover -s tests/tools -p test_toapis_image.py

```



`TOAPIS_BASE_URL` defaults to **https://toapis.com**; https://toapis.cn and a trailing /v1 are accepted. No OpenAI or fal key is needed for this provider. `.env.example` includes the new variables; keep keys and `.toapis-state` private. The CLI is a native-provider smoke test, not a complete video production run.



## Native integration



New [ToAPIsImage](tools/graphics/toapis_image.py) is discovered by the upstream registry as `toapis_image`, provider `toapis`. It preserves the existing OpenAI route and uses a separate [async adapter](tools/toapis_async.py).



```python

from tools.graphics.toapis_image import ToAPIsImage

result = ToAPIsImage().execute({

    "prompt": "An original ivory exploration rover on a coral desert moon",

    "model": "gpt-image-2-vip", "quality": "low", "resolution": "1K",

    "size": "1024x1024", "n": 1,

    "output_path": "projects/my-story/assets/images/rover.png",

    "run_id": "my-rover-v1"

})

```



For `image_selector`, require `preferred_tool="toapis_image"`, `hosting_provider="toapis"` and the exact model. Registration and exact route filtering were tested; full automatic agent routing was not. Follow the [tool contract](docs/TOAPIS.md).



## What's changed and tested



- Bearer auth to /v1; authenticated pricing lookup; ratio/resolution mapping; local reference upload; one generation submission; task polling; PNG download and saving.

- Durable task receipts resume an existing task, and block another POST after an ambiguous submission. Change run_id explicitly to request a new generation.

- Fixed a real CDN download failure: Python's default User-Agent returned Cloudflare 1010/403. Result downloads use an accepted User-Agent and carry no API key. The first task was recovered without resubmission.

- Ten offline native tests passed; the VIP storyboard calls used `ToolRegistry` + `ToAPIsImage.execute`. Additional model cases are documented below. Masks, transparency, multiple outputs, non-VIP reference edits and untested tiers fail before submission.



Video, audio, Backlot UI, the complete agent production pipeline and visual continuity are not validated by these image tests. Reference edits can change details; inspect the actual images.



## Upstream attribution



Community fork of [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage), pinned at `e45f5b12bd46440b04f3675af9a77d0718e6a254`. Original [English README](README_UPSTREAM.md), [Chinese README](README_UPSTREAM_zh-CN.md), all source, license and sponsor links remain. The project remains [AGPL-3.0](LICENSE); the reused standalone adapter has its [MIT notice](tools/TOAPIS_ADAPTER_LICENSE). No upstream partnership or endorsement is claimed.



Original JPEGs are retained; PNGs are serialized locally without another API call. Actual pixels and request tiers are recorded separately. Backend durations come from the owner screenshot; client durations remain separate in the task records.

