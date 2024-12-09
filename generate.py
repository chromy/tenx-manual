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
EDITOR = "nvim --clean"


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
    env = os.environ.copy()
    env["EDITOR"] = EDITOR
    subprocess.run(["vhs", f"./{tape_name}.tape"], check=True, env=env)


def capture(example, suffix, path):
    source_path = os.path.abspath(path)
    extension = os.path.splitext(path)[1]
    dest_filename = f"{example}_{suffix}{extension}"
    dest_path = os.path.join(DST, dest_filename)
    shutil.copy2(source_path, dest_path)


def capture_cmd(example, suffix, cmd, env=None):
    dest_filename = f"{example}_{suffix}.txt"
    dest_path = os.path.join(DST, dest_filename)
    command_env = {"PATH": os.environ["PATH"]}
    if env:
        command_env.update(env)
    try:
        result = subprocess.run(
            cmd, shell=True, env=command_env, text=True, capture_output=True, check=True
        )
        with open(dest_path, "w") as f:
            f.write(f"$ {cmd}\n")
            f.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        raise


def capture_cmd_svg(
    example,
    suffix,
    cmd,
    env=None,
    width=80,
    fontsize=20,
    colorscheme="Solarized Dark - Patched",
):
    dest_filename = f"{example}_{suffix}.svg"
    dest_path = os.path.join(DST, dest_filename)
    command_env = {"PATH": os.environ["PATH"]}
    if env:
        command_env.update(env)
    try:
        # Get command output
        result = subprocess.run(
            cmd,
            shell=True,
            env=command_env,
            text=True,
            capture_output=True,
            check=True,
        )
        # Prepare input with colored prompt
        prompt = "\033[32m$\033[0m "  # Green $ followed by space
        full_output = f"{prompt}{cmd}\n{result.stdout}"

        # Convert to SVG
        process = subprocess.Popen(
            [
                "ansisvg",
                "--colorscheme",
                colorscheme,
                "--width",
                str(width),
                "--fontsize",
                str(fontsize),
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=False,
        )
        svg_output, stderr = process.communicate(full_output.encode())
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, cmd, stderr=stderr)
        with open(dest_path, "wb") as f:
            f.write(svg_output)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("STDERR:")
        print(e.stderr)
        raise


def quickstart():
    with temp_example_dir("quickstart"):
        capture("quickstart", "before", "src/lib.rs")

        vhs("quickstart-quick")
        capture("quickstart", "quick", "vid.gif")

        capture_cmd_svg(
            "quickstart",
            "session",
            "tenx session",
            env={"ANTHROPIC_API_KEY": "my-api-key", "TENX_COLOR": "true"},
        )

        capture_cmd_svg(
            "quickstart",
            "check",
            "tenx check",
            env={"ANTHROPIC_API_KEY": "my-api-key", "TENX_COLOR": "true"},
        )


        vhs("quickstart-code")
        capture("quickstart", "code", "vid.gif")
        capture("quickstart", "after", "src/lib.rs")

        capture_cmd_svg(
            "quickstart",
            "models",
            "tenx models",
            env={"ANTHROPIC_API_KEY": "my-api-key", "TENX_COLOR": "true"},
        )


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
