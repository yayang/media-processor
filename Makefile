.PHONY: install test run clean help

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies using uv"
	@echo "  make test     - Run tests"
	@echo "  make clean    - Remove build artifacts and temp files"
	@echo ""
	@echo "Run Tasks:"
	@echo "  make run                            - Run with default params/params.json"
	@echo "  make run config=params/my_task.json - Run with specific config file"
	@echo ""
	@echo "Supported Tasks (configured via JSON):"
	@echo "  - audio     : Extract and merge audio tracks"
	@echo "  - convert   : Batch compress/convert videos"
	@echo "  - timelapse : Create high-speed videos from footage"
	@echo "  - chapter   : Add chapter markers to video"
	@echo "  - merge     : Merge video clips without re-encoding"
	@echo "  - subtitle  : Embed subtitles (stream copy)"
	@echo ""
	@echo "Examples:"
	@echo "  make run config=params/examples/audio.json"
	@echo "  make run config=params/examples/convert.json"

install:
	@echo "Creating virtual environment and installing dependencies..."
	uv venv --allow-existing --python 3.12
	uv sync

test:
	PYTHONPATH=src uv run pytest

# Support `make run config=path/to/file.json`
# If config is not defined, default to params/params.json
config ?= params/params.json
run:
	PYTHONPATH=src uv run main.py run --config $(config)

clean:
	@echo "🧹 Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*_processing.*" -delete
	@find . -type f -name ".DS_Store" -delete
	@echo "✨ Done!"
