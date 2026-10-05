from src.config import parse_arguments
from src.shell import Shell


def main() -> None:
    config = parse_arguments()

    print(f"VFS path: {config.vfs_path}")
    print(f"Prompt: {config.prompt}")
    print(f"Startup script: {config.startup_script}")

    shell = Shell(
        vfs_path=config.vfs_path,
        prompt=config.prompt,
        startup_script=config.startup_script,
    )

    shell.start()


if __name__ == "__main__":
    main()