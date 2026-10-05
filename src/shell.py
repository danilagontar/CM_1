import os
import socket

from src.commands import commands, execute_cd, execute_ls
from src.parser import parse_command


class Shell:
    def __init__(
        self,
        vfs_path: str | None = None,
        prompt: str | None = None,
        startup_script: str | None = None,
    ) -> None:
        self.username = self._get_username()
        self.hostname = socket.gethostname()
        self.vfs_path = vfs_path
        self.prompt = prompt
        self.startup_script = startup_script
        self.running = True

    @staticmethod
    def _get_username() -> str:
        return os.getenv("USER", os.getenv("USERNAME", "user"))

    def get_prompt(self) -> str:
        if self.prompt is not None:
            return self.prompt

        return f"{self.username}@{self.hostname}:~$ "

    def start(self) -> None:
        if self.startup_script is not None:
            self.run_script()

        if self.running:
            self.run()

    def run(self) -> None:
        while self.running:
            try:
                command = input(self.get_prompt())
                self.execute(command)
            except EOFError:
                self.running = False
            except KeyboardInterrupt:
                print()

    def run_script(self) -> None:
        try:
            with open(
                self.startup_script,
                "r",
                encoding="utf-8",
            ) as file:
                for line in file:
                    command = line.strip()

                    if not command:
                        continue

                    print(f"{self.get_prompt()}{command}")

                    if not self.execute(command):
                        self.running = False
                        return
        except FileNotFoundError:
            print(
                f"Error: startup script not found: "
                f"{self.startup_script}"
            )
            self.running = False
        except OSError as error:
            print(f"Error: cannot read startup script: {error}")
            self.running = False

    def execute(self, command_line: str) -> bool:
        name, arguments = parse_command(command_line)

        if not name:
            return True

        if name == "exit":
            self.running = False
            return True

        if name not in commands:
            print(f"Error: unknown command: {name}")
            return False

        self._execute_supported_command(name, arguments)
        return True

    def _execute_supported_command(
        self,
        name: str,
        arguments: list[str],
    ) -> None:
        if name == "ls":
            print(execute_ls(arguments))
            return

        if name == "cd":
            print(execute_cd(arguments))
            return