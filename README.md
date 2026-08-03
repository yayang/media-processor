# Media Processor

**Media Processor** 是一个面向视频与音频批处理的 CLI 工具。项目基于 Python 实现，并通过 `make` 统一调度，把较复杂的 FFmpeg 操作收敛为结构化、可配置的任务流程。

## ✨ 核心能力

- **🎥 视频转换**: 批量压缩视频到标准规格（1080p/720p），可选 GPU 加速。
- **⏱️ 延时视频生成**: 从原始素材目录中生成高速 timelapse 视频。
- **🎵 音频处理**: 提取音轨，并合并为单个或批量 MP3 文件。
- **📝 字幕与章节**: 自动封装字幕并烧录章节标记。
- **🚀 性能优先**: 支持硬件加速和 stream copy 合并，尽量减少处理耗时。
- **🛠️ JSON 驱动**: 通过 JSON 配置文件定义任务，便于复现和复用处理流程。

## 🚀 快速开始

1. **安装依赖**:
   ```bash
   make install
   ```

2. **准备配置**:
   复制一个示例配置作为起点:
   ```bash
   cp params/convert.example.json params/params.json
   ```

3. **执行任务**:
   ```bash
   make run
   ```
   也可以直接指定配置文件:
   ```bash
   make run config=params/audio.json
   ```

## 📖 文档

完整用法、参数说明和进阶工作流见[用户手册](docs/user_manual.md)。
