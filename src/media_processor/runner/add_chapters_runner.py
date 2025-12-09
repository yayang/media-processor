import os
from pathlib import Path

from media_processor.service.media_process import chapter_processor

# --- 📍 路径导航系统 ---

# 1. 锁定当前脚本的位置 (锚点)
# 路径: .../src/media_processor/runner/add_chapters_runner.py
CURRENT_FILE = Path(__file__).resolve()

# 2. 向上溯源找到【项目根目录】
# parents[0] = runner
# parents[1] = media_processor
# parents[2] = src
# parents[3] = 项目根目录
PROJECT_ROOT = CURRENT_FILE.parents[3]

# 所有生成带章节视频的存放位置
OUTPUT_DIR = PROJECT_ROOT / "output" / "Chaptered_Videos"

# --- ⚙️ 任务配置区域 (TaskList) ---

# 这里配置具体的视频和章节
# 格式: { "file": "路径", "chapters": [ ("时间", "标题"), ... ] }
TASKS = [
    # {
    #     "file": "/Users/yang/Movies/Vlogs/MyVlog_01.mp4",
    #     "chapters": [
    #         ("00:00", "Intro"),
    #         ("01:30", "Talk"),
    #         ("03:45", "B-Roll"),
    #         ("05:00", "Ending")
    #     ]
    # }
]


# --------------------

def main():
    output_root = Path(OUTPUT_DIR)
    output_root.mkdir(parents=True, exist_ok=True)

    print(f"=== Starting Chapter Injection ===")
    print(f"Output Dir: {OUTPUT_DIR}\n")

    for task in TASKS:
        source_path = Path(task["file"])
        chapters_data = task["chapters"]

        if not source_path.exists():
            print(f"⚠️  Source file not found: {source_path}")
            continue

        # 自动生成输出文件名 (原文件名_chapters.mp4)
        output_filename = f"{source_path.stem}_chapters{source_path.suffix}"
        output_path = output_root / output_filename

        # 调用处理器
        chapter_processor.inject_chapters(
            video_path=source_path,
            output_path=output_path,
            chapters=chapters_data
        )

    print("\n🎉 All Tasks Completed.")


if __name__ == "__main__":
    main()