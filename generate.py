#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from contextlib import contextmanager

# Test environment for when output matters
TENV = {
    "ANTHROPIC_API_KEY": "my-api-key",
    "TENX_COLOR": "true",
    "RUSKEL_COLOR": "always",
}


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(SCRIPT_DIR, "examples")
DST = os.path.join(SCRIPT_DIR, "src/examples")
EDITOR = "nvim --clean"
VHS_OUTPUT = "vid.gif"
EXAMPLES_DIR = os.path.expanduser("~/tenx/examples")


@contextmanager
def temp_example_dir(source_dir):
    print(f"entering temp dir: {source_dir}")
    dest_dir = os.path.join(EXAMPLES_DIR, source_dir)
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(EXAMPLES_DIR, exist_ok=True)
    shutil.copytree(os.path.join(SRC, source_dir), dest_dir)
    original_dir = os.getcwd()
    os.chdir(dest_dir)
    try:
        yield dest_dir
    finally:
        os.chdir(original_dir)
        shutil.rmtree(dest_dir)


def vhs(name, tape_name):
    print(f"vhs: {name}")
    shutil.copy(os.path.join(SRC, f"{tape_name}.tape"), ".")
    shutil.copy(os.path.join(SRC, "common.tape"), ".")
    env = os.environ.copy()
    env["EDITOR"] = EDITOR
    env["TENX_COLOR"] = "true"
    subprocess.run(["vhs", "--quiet", f"./{tape_name}.tape"], check=True, env=env)
    capture(name, VHS_OUTPUT)


def capture(name, path):
    source_path = os.path.abspath(path)
    extension = os.path.splitext(path)[1]
    dest_filename = f"{name}{extension}"
    dest_path = os.path.join(DST, dest_filename)
    shutil.copy2(source_path, dest_path)


def capture_cmd(name, cmd, env=None):
    """
    Capture raw cmd output to a text file. Inherits the full environment.
    """
    print(f"capture_cmd: {name}")
    dest_filename = f"{name}.txt"
    dest_path = os.path.join(DST, dest_filename)
    try:
        result = subprocess.run(
            cmd, shell=True, text=True, capture_output=True, check=True
        )
        with open(dest_path, "w") as f:
            f.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        raise


def capture_cmd_svg(
    name,
    cmd,
    env=None,
    width=80,
    fontsize=20,
    colorscheme="Tomorrow Night",
    accept_error=False,
):
    print(f"capture_cmd_svg: {name}")
    dest_filename = f"{name}.svg"
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
            check=not accept_error,
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


def fix():
    with temp_example_dir("fix"):
        capture("fix_before", "src/lib.rs")

        vhs("fix_check", "fix-check")

        vhs("fix_fix", "fix-fix")

        capture("fix_after", "src/lib.rs")


def quickstart():
    with temp_example_dir("quickstart"):
        capture("quickstart_before", "src/lib.rs")

        vhs("quickstart_quick", "quickstart-quick")

        vhs("tenx_project", "tenx-project")

        capture_cmd_svg("quickstart_session", "tenx session", env=TENV)

        capture_cmd_svg("quickstart_check", "tenx check", env=TENV)

        vhs("quickstart_check", "quickstart-check")

        vhs("quickstart_code", "quickstart-code")

        capture_cmd_svg("tenx_session", "tenx session", env=TENV)
        capture_cmd_svg("tenx_files", "tenx files", env=TENV)

        capture("quickstart_after", "src/lib.rs")

        capture_cmd_svg("quickstart_models", "tenx models", env=TENV)


def concepts():
    with temp_example_dir("concepts"):
        capture_cmd_svg("concepts_project", "tenx project", env=TENV)


def tenx():
    capture_cmd_svg("tenx_ctx", "tenx ctx --help", env=TENV)
    capture_cmd_svg("tenx_help", "tenx --help", env=TENV)
    capture_cmd_svg("tenx_code_help", "tenx code --help", env=TENV)
    capture_cmd_svg("tenx_checks", "tenx checks --all", env=TENV)


def session():
    with temp_example_dir("quickstart"):
        vhs("tenx_new", "tenx-new")


def context():
    with temp_example_dir("ruskel"):
        capture_cmd_svg("ruskel", "ruskel termsize", env=TENV)

        capture("context_before", "src/main.rs")

        vhs("ruskel_setup", "ruskel-setup")

        vhs("ruskel_code", "ruskel-code")

        capture("context_after", "src/main.rs")

        capture_cmd("ruskel_run", "cargo run")


def checks():
    with temp_example_dir("ptest"):
        capture_cmd_svg("checks_checks", "tenx checks", env=TENV)
        vhs("checks_run", "checks-run")


examples = {
    "quickstart": quickstart,
    "checks": checks,
    "concepts": concepts,
    "context": context,
    "tenx": tenx,
    "session": session,
    "fix": fix,
}


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
