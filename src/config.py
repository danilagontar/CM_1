import argparse
from dataclasses import dataclass


@dataclass
class Config:

    vfs_path: str | None
    prompt: str | None
    startup_script: str | None


def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(
        description="UNIX-like shell emulator"
    )

    parser.add_argument(
        "--vfs",
        dest="vfs_path",
        help="Path to the virtual file system",
    )
    parser.add_argument(
        "--prompt",
        help="Custom REPL prompt",
    )
    parser.add_argument(
        "--script",
        dest="startup_script",
        help="Path to the startup script",
    )

    arguments = parser.parse_args()

    return Config(
        vfs_path=arguments.vfs_path,
        prompt=arguments.prompt,
        startup_script=arguments.startup_script,
    )