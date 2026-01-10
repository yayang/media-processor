# Media Processor

**Media Processor** is a comprehensive CLI tool designed for efficient batch processing of video and audio files. Built with Python and automated via `make`, it simplifies complex FFmpeg operations into structured, configurable tasks.

## ✨ Key Features

- **🎥 Video Conversion**: Batch compress videos to standard formats (1080p/720p) with optional GPU acceleration.
- **⏱️ Timelapse Generation**: Create high-speed timelapse videos from folders of raw footage.
- **🎵 Audio Tools**: Extract audio tracks and merge them into single or batched MP3 files.
- **📝 Subtitle & Chapters**: Automatically embed subtitles and burn chapter markers.
- **🚀 High Performance**: Supports hardware acceleration and stream-copy merging for maximum speed.
- **🛠️ Configurable**: Fully driven by JSON configuration files for reproducible workflows.

## 🚀 Quick Start

1.  **Install Dependencies**:
    ```bash
    make install
    ```

2.  **Configure**:
    Copy an example configuration to start:
    ```bash
    cp params/convert.example.json params/params.json
    ```

3.  **Run**:
    ```bash
    make run
    ```
    Or specify a config file directly:
    ```bash
    make run config=params/audio.json
    ```

## 📖 Documentation

For full usage details, parameter references, and advanced workflows, please consult the [User Manual](docs/user_manual.md).
