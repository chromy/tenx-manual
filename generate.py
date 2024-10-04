#!/usr/bin/env python3
import sys
import os
import shutil
import tempfile
import subprocess
from contextlib import contextmanager

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

SRC = os.path.join(SCRIPT_DIR, "examples")
DST = os.path.join(SCRIPT_DIR, "src/examples")


@contextmanager
def temp_example_dir(source_dir):
    with tempfile.TemporaryDirectory() as temp_dir:
        dest_dir = os.path.join(temp_dir, source_dir)
        shutil.copytree(os.path.join(SRC, source_dir), dest_dir)
        original_dir = os.getcwd()
        os.chdir(dest_dir)
        try:
            yield dest_dir
        finally:
            os.chdir(original_dir)


def vhs(tape_name):
    shutil.copy(os.path.join(SRC, f"{tape_name}.tape"), ".")
    shutil.copy(os.path.join(SRC, "common.tape"), ".")
    subprocess.run(["vhs", f"./{tape_name}.tape"], check=True)


def capture(example_name, path, prefix=None):
    source_path = os.path.abspath(path)
    filename = os.path.basename(path)
    if prefix:
        dest_filename = f"{example_name}_{prefix}_{filename}"
    else:
        dest_filename = f"{example_name}_{filename}"
    dest_path = os.path.join(DST, dest_filename)
    shutil.copy2(source_path, dest_path)


def quickstart():
    with temp_example_dir("quickstart"):
        capture("quickstart", "src/lib.rs", prefix="before")
        vhs("quickstart")
        capture("quickstart", "vid.gif")
        capture("quickstart", "src/lib.rs", prefix="after")


examples = {"quickstart": quickstart}

def main(example_name=None):
    if example_name:
        if example_name in examples:
            examples[example_name]()
        else:
            print(f"Error: Example '{example_name}' not found.")
    else:
        for name, func in examples.items():
            print(f"generating: {name}")
            func()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
