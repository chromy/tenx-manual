#!/usr/bin/env python3

import os
import shutil
import subprocess

BASE = "../src/examples"

def save_output(output_path, cmd):
    term_transcript_cmd = f'term-transcript exec "{cmd}"'
    abs_output_path = os.path.abspath(output_path)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(abs_output_path), exist_ok=True)

    try:
        subprocess.run(
            term_transcript_cmd,
            shell=True,
            check=True,
            stdout=open(abs_output_path, "w"),
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running term-transcript: {e.stderr}")


def static(template_dir, name, command):
    dest_dir = os.path.join(BASE, name)
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(template_dir, dest_dir)

    current_dir = os.getcwd()
    os.chdir(dest_dir)

    try:
        output_path = "output.svg"
        save_output(output_path, command)
    finally:
        os.chdir(current_dir)


def main():
    # save_output(os.path.join(BASE, "help.svg"), "tenx help")
    static(
        "quickstart",
        "quickstart-fib",
        r"tenx --color oneshot --prompt \"implement fibonacci, and add a test\" ./src/lib.rs", 
    )


if __name__ == "__main__":
    main()
