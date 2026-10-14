# 更低成本的 OpenMontage 图片方案

[English](README.md) · [模型价格与 API 入口](https://go2v.toapis.com/om14gc) · [OpenMontage 上游](https://github.com/calesthio/OpenMontage)

**$0.0019/张**，ToAPIs `gpt-image-2-vip | low/1K`。原创月球车场景 → 温室内景 → 蓝调离场，通过原生 OpenMontage `BaseTool` 完成文生图与参考改图。3张image-2(vip)生图实扣 **$0.0057**（1.14 积分）。

## 演示

![三张真实分镜图片](assets/overview-cn.png)

| 场景 | 调用 | 真实输出 | 文件 |
|---|---|---|---|
| 月球初抵 | 文生图 | 1024×1024 PNG | [原图](examples/toapis/results/orbital-arrival/result.png) |
| 温室内景 | 第一张参考改图 | 1024×1024 PNG | [原图](examples/toapis/results/habitat-interior/result.png) |
| 蓝调离场 | 第一张参考改图 | 1024×1024 PNG | [原图](examples/toapis/results/blue-hour-departure/result.png) |

[原创输入](examples/toapis/cases.json) · [真实任务与脱敏记录](examples/toapis/results/runs.json)。2026-10-14 实测；模型输出存在随机性，可复用参数与步骤，不能保证相同像素或严格角色一致性。

## 七个模型选项的案例、价格与消费对比

本次全部 11 项调用实扣 **$0.195912**。

![Model comparison A](assets/comparison-a-cn.png)

![Model comparison B](assets/comparison-b-cn.png)

| Model / API route | Tier | Quote / image | Actual charge / sample | Actual px | Client seconds | Output |
|---|---|---|---|---|---|---|
| [`gpt-image-2-vip`](https://go2v.toapis.com/om14ge) | low / requested 1K | $0.0019 | $0.0019 | 1024×1024 / PNG | not recorded / recovered | [PNG](examples/toapis/results/orbital-arrival/result.png) · [record](examples/toapis/results/orbital-arrival/evidence.json) |
| [`gpt-image-2`](https://toapis.com/en/model-guide/gpt-image-2?utm_campaign=om14i2) | — / requested 1K | $0.015 | $0.015 | 1280×1280 / PNG | 115.69 | [PNG](examples/toapis/resolution-probes/gpt-image-2/result.png) · [record](examples/toapis/resolution-probes/gpt-image-2/evidence.json) |
| [`gpt-image-2.5-flare`](https://im25.toapis.com/om14f) | high / requested 1K | $0.0225 | $0.0225 | 1024×1024 / PNG | 60.2 | [PNG](examples/toapis/comparison/gpt-image-2.5-flare/result.png) · [record](examples/toapis/comparison/gpt-image-2.5-flare/evidence.json) |
| [`gemini-nano-banana-2.1`](https://toapis.com/en/model-guide/gemini-nano-banana-2-1?utm_campaign=om14n1) | — / requested 1K | $0.015 | $0.015 | 1024×1024 / JPEG → PNG | 32.38 | [PNG](examples/toapis/comparison/gemini-nano-banana-2.1/result.png) · [Original JPEG](examples/toapis/comparison/gemini-nano-banana-2.1/result-original.jpg) · [record](examples/toapis/comparison/gemini-nano-banana-2.1/evidence.json) |
| [`doubao-seedream-5-0-pro`](https://toapis.com/en/model-guide/doubao-seedream-5-0-pro?utm_campaign=om14s5) | medium (quote) / requested 1K | $0.042857 | $0.042856 | 2048×2048 / JPEG → PNG | 86.95 | [PNG](examples/toapis/resolution-probes/doubao-seedream-5-0-pro/result.png) · [Original JPEG](examples/toapis/resolution-probes/doubao-seedream-5-0-pro/result-original.jpg) · [record](examples/toapis/resolution-probes/doubao-seedream-5-0-pro/evidence.json) |
| [`gemini-3.1-flash-image-preview`](https://nano2.toapis.com/om14n2) | — / requested 1K | $0.025 | $0.025 | 1024×1024 / PNG | 32.77 | [PNG](examples/toapis/comparison/gemini-3.1-flash-image-preview/result.png) · [record](examples/toapis/comparison/gemini-3.1-flash-image-preview/evidence.json) |
| [`nano_banana`](https://x.toapis.com/om14nb) | — / requested 1K | $0.012 | $0.012 | 1024×1024 / PNG | 14.41 | [PNG](examples/toapis/comparison/nano_banana/result.png) · [record](examples/toapis/comparison/nano_banana/evidence.json) |

[完整对比、分辨率差异和复用命令](examples/toapis/MODEL_COMPARISON.md)。同一提示词但模型档位不同，单张样例不是严格性能排名。

## API pricing 与本次花费

| 模型 | 参数 | 当前报价 | 本次花费 |
|---|---|---|---|
| `gpt-image-2-vip` | `low / 1K / n=1` | **$0.0019/张** | $0.0057 / 3 张，后台确认实扣 |

报价于 2026-10-14 通过鉴权 pricing API 核对。1 积分=$0.005；脱敏记录保留 API 原始 billing=null，实际花费在后台确认后填写。[对应模型价格快照](examples/toapis/pricing.json)。

## 复用步骤

Python 3.10+，clone 后得到保留上游源码的真实 fork。下列轻量依赖仅用于本图片工具，完整工作室遵循上游 requirements 与 [AGENT_GUIDE](AGENT_GUIDE.md)。

```bash
git clone --depth 1 https://github.com/ToAPIs-2025/lower-cost-openmontage-toapis.git
cd lower-cost-openmontage-toapis
python -m pip install -r requirements-toapis.txt
python examples/toapis/demo.py
# Configure TOAPIS_API_KEY privately, then run the charged demo:
python examples/toapis/demo.py --live
python -m unittest discover -s tests/tools -p test_toapis_image.py
```

在本机私有环境配置 `TOAPIS_API_KEY`。`TOAPIS_BASE_URL` 默认为 **https://toapis.com**，也接受 https://toapis.cn 和 /v1 后缀。无需 OpenAI/fal Key。保留私有任务状态，勿提交 Key 或 `.toapis-state`。

## 原生接入与优化

新增 [tools/graphics/toapis_image.py](tools/graphics/toapis_image.py)，注册名 `toapis_image`，Provider `toapis`。通过原生 `ToolRegistry.register_module` 获取工具并执行；上游 OpenAI 调用路线保留。

- 鉴权报价 → 本地参考图上传 → 提交一次异步图片任务 → 按 ID 查询 → 下载 PNG。
- 像素提示转为宽高比，独立传 resolution；最终图片尺寸以实际输出为准。
- 任务提交前写入私有状态，有 ID 就恢复原任务；无 ID 的不确定提交停止，避免重复付费。
- 修复实测发现的 CDN 下载 403：结果请求设置可接受的 User-Agent，不携带 API Key。第一项任务按原 ID 恢复，没有重新生成。
- 10 项离线注册/协议/拦截测试通过，原生 VIP 图片 Provider 三项调用成功；新增模型调用另见对比。VIP low/1K/n=1 及对比表中的对应档位已启用，遮罩、透明背景和未核实档位提前拦截。

`image_selector` 可指定 `preferred_tool="toapis_image"`、`hosting_provider="toapis"` 和 exact model；完整自动 Agent 路由尚未验收。[详细接入说明](docs/TOAPIS.md)。

本教程验收范围是原生图片 Provider，不包含视频、音频、Backlot 画布及完整 production pipeline。参考改图不保证所有细节完全一致。

## 上游署名

基于 [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) 固定 SHA `e45f5b12bd46440b04f3675af9a77d0718e6a254` 的社区 fork；保留完整源码、[原英文 README](README_UPSTREAM.md)、[原中文 README](README_UPSTREAM_zh-CN.md)、赞助入口和 [AGPL-3.0](LICENSE)。独立复用异步适配器另保留 [MIT 声明](tools/TOAPIS_ADAPTER_LICENSE)。未代表上游官方集成或既有合作。

原始 JPEG 保留，PNG 是本地另存版本；费用按原始 API 任务核算，不为格式转换再次调用。实际像素与请求档位分开记录，服务端耗时来自后台截图，客户端耗时另见任务记录。
