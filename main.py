#!/usr/bin/env python3
"""Write the competition's single-line support reply."""
import os
import tempfile
from pathlib import Path

ENTRY = "I can't restore your files, but I can stay on the line while we both pretend the progress bar is thinking."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.txt"
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=output_dir, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(ENTRY)
        temporary.replace(destination)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


if __name__ == "__main__":
    main()
