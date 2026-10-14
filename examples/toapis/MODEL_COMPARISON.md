# 七个图片 API 选项 / Seven image API options

同一原创提示词、文生图、无参考图、n=1、1:1、请求 1K。VIP 首张、另外六模型各选一张；标准 GPT 与 Seedream 展示分辨率补测版本，原始调用全部保留。1K 是请求/计价档位，实际像素另列，不能把请求档位等同于 1024px。

One common original prompt, text-to-image, no reference, n=1, 1:1, requested 1K. Each model has one displayed sample; the standard GPT and Seedream sample use the explicit top-level resolution probe. Original first calls remain in the records. These are API route options, not a claim that every route uses a distinct foundation model.

| Model / API route | Tier | Quote / image | Actual charge / sample | Actual px | Client seconds | Output |
|---|---|---|---|---|---|---|
| [`gpt-image-2-vip`](https://go2v.toapis.com/om14ge) | low / requested 1K | $0.0019 | $0.0019 | 1024×1024 / PNG | not recorded / recovered | [PNG](results/orbital-arrival/result.png) · [record](results/orbital-arrival/evidence.json) |
| [`gpt-image-2`](https://toapis.com/en/model-guide/gpt-image-2?utm_campaign=om14i2) | — / requested 1K | $0.015 | $0.015 | 1280×1280 / PNG | 115.69 | [PNG](resolution-probes/gpt-image-2/result.png) · [record](resolution-probes/gpt-image-2/evidence.json) |
| [`gpt-image-2.5-flare`](https://im25.toapis.com/om14f) | high / requested 1K | $0.0225 | $0.0225 | 1024×1024 / PNG | 60.2 | [PNG](comparison/gpt-image-2.5-flare/result.png) · [record](comparison/gpt-image-2.5-flare/evidence.json) |
| [`gemini-nano-banana-2.1`](https://toapis.com/en/model-guide/gemini-nano-banana-2-1?utm_campaign=om14n1) | — / requested 1K | $0.015 | $0.015 | 1024×1024 / JPEG → PNG | 32.38 | [PNG](comparison/gemini-nano-banana-2.1/result.png) · [Original JPEG](comparison/gemini-nano-banana-2.1/result-original.jpg) · [record](comparison/gemini-nano-banana-2.1/evidence.json) |
| [`doubao-seedream-5-0-pro`](https://toapis.com/en/model-guide/doubao-seedream-5-0-pro?utm_campaign=om14s5) | medium (quote) / requested 1K | $0.042857 | $0.042856 | 2048×2048 / JPEG → PNG | 86.95 | [PNG](resolution-probes/doubao-seedream-5-0-pro/result.png) · [Original JPEG](resolution-probes/doubao-seedream-5-0-pro/result-original.jpg) · [record](resolution-probes/doubao-seedream-5-0-pro/evidence.json) |
| [`gemini-3.1-flash-image-preview`](https://nano2.toapis.com/om14n2) | — / requested 1K | $0.025 | $0.025 | 1024×1024 / PNG | 32.77 | [PNG](comparison/gemini-3.1-flash-image-preview/result.png) · [record](comparison/gemini-3.1-flash-image-preview/evidence.json) |
| [`nano_banana`](https://x.toapis.com/om14nb) | — / requested 1K | $0.012 | $0.012 | 1024×1024 / PNG | 14.41 | [PNG](comparison/nano_banana/result.png) · [record](comparison/nano_banana/evidence.json) |

本次全部 11 项调用实扣 **$0.195912**。

All 11 calls actually charged **$0.195912**.

1 credit=$0.005. [All original records](all-runs.json) preserve billing=null even after owner charge confirmation. Price comes from the authenticated ToAPIs API snapshot on 2026-10-14; only these tested options are shown.

各模型质量参数不同：VIP low、Flare high、Seedream 当前报价档 medium，其余未指定 quality。单张未固定 seed，耗时是客户端核价/提交/轮询/下载的端到端观测，不是均值或稳定性测评；不能宣称同质量排名。

Quality settings differ: VIP low, Flare high, Seedream medium quoted tier, others unspecified. One unseeded sample per route. Client duration includes price lookup, submission, polling and download; it is not average latency. No quality or reliability ranking is established.

分辨率核查 / Resolution audit:

- `gpt-image-2` first metadata-only request returned 1280×1280; explicit top-level resolution probe returned 1280×1280. Both originals are retained.
- Seedream first metadata-only request returned 2048×2048; explicit top-level probe returned 2048×2048. Report actual size and confirmed charge rather than assume a 1K request guarantees 1024px.
- Seedream pricing catalog starts input_image_count=1; official docs say the first reference is free. These comparisons use no reference. The catalog floor quote is recorded; actual settlement remains a separate field.
- Model `gemini-nano-banana-2.1` is the live catalog ID for the requested nanobanana2.1 option. `nano_banana` and `gemini-3.1-flash-image-preview` are retained as separate API route IDs; no unsupported claim about their underlying model equivalence is made.
- Nano Banana 2.1 and Seedream returned JPEG. Their original JPEG bytes are retained and linked; PNG convenience copies were serialized locally, without another API generation or image-content edit.

## Run the comparison

```bash
python examples/toapis/compare.py
# After configuring TOAPIS_API_KEY privately:
python examples/toapis/compare.py --live
```

Each task is priced before submitting. The six-option demo stops if its quoted total exceeds $0.50; per-task $0.10 guard remains. Reruns with existing local evidence skip generation. Keep the private receipts; do not automatically resubmit an ambiguous task.
