# User Manual

## 🚀 Quick Start

1.  **Setup Environment**: `make install`
2.  **Configure**:
    ```bash
    # Choose a template from params/examples/
    cp params/examples/convert.json params/params.json
    
    # Edit input paths in params/params.json
    vim params/params.json
    ```
3.  **Run**: `make run` (or `make run config=params/audio.json`)

## 📚 Advanced Configuration

*Common parameters like `input_dirs`, `output_dir`, `delete_source` are self-explanatory.*

### Special Parameters

#### `compatibility_mode` (Video Conversion)
Enable this for maximum compatibility with older TVs or hardware players.

- **Deinterlacing**: Automatically cleans up 1080i/60i content (`yadif`).
- **Standardization**: Forces `yuv420p` and Constant Frame Rate (CFR).
- **Hardware Spec**: Restricts to **High@L4.1** (Ref=4), ensuring playback on verified legacy devices.
- **Fast Start**: Optimizes MP4 header for streaming.

#### `batch_size` (Audio Extraction)
- `0`: Merge **ALL** extracted audio tracks into a **single** MP3 file.
- `N > 0`: Group every `N` videos into one MP3 (e.g., `5` = 5 videos per MP3).

#### `use_gpu`
- `true`: Uses **VideoToolbox** (Mac Hardware Acceleration). Faster, but slightly larger file size.
- `false`: Uses **libx264** (CPU). Slower, but better compression ratio.

#### `chapters` (Chapter Task)
List of `[time, title]` pairs.
Example: `[["00:00", "Start"], ["05:00", "End"]]`.

## 📖 Cookbook

### 1. Audio Extraction
**Goal**: Combine clips into a single MP3.
1.  Use `params/examples/audio.json`.
2.  Set `batch_size: 0` in config.

### 2. Video Compression (Batch)
**Goal**: Compress videos to 1080p.
1.  Use `params/examples/convert.json`.
2.  Set `resolution: "1080p"` and `use_gpu: false` (for best size).

### 3. Timelapse
**Goal**: Create high-speed videos from dashcam folders.
1.  Use `params/examples/timelapse.json`.
2.  Set `speed_ratio` (e.g., `20` for 20x speed).
3.  **Note**: `input_dirs` should be the *parent folders* containing video clips.

### 4. Merge Videos
**Goal**: Join clips without re-encoding.
1.  Use `params/examples/merge.json`.
2.  **Note**: Uses stream-copy for speed. Output is forced to `.mp4`.

### 5. Add Chapters
**Goal**: Burn chapter markers.
1.  Use `params/examples/chapter.json`.
2.  Define specific timestamps in the `tasks` list.
