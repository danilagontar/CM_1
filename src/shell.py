import os
import socket

from src.commands import commands, execute_cd, execute_ls
from src.parser import parse_command


class Shell:
    def __init__(self) -> None:
        self.username = self._get_username()
        self.hostname = socket.gethostname()
        self.running = True

    @staticmethod
    def _get_username() -> str:
        return os.getenv("USER", os.getenv("USERNAME", "user"))

    def get_prompt(self) -> str:
        return f"{self.username}@{self.hostname}:~$ "

    def run(self) -> None:
        while self.running:
            try:
                command = input(self.get_prompt())
                self.execute(command)
            except EOFError:
                self.running = False
            except KeyboardInterrupt:
                print()

    def execute(self, command_line: str) -> None:
        name, arguments = parse_command(command_line)
        if not name:
            return
        if name == "exit":
            self.running = False
            return
        if name not in commands:
            print(f"Error: unknown command: {name}")
            return
        self._execute_supported_command(name, arguments)

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