import os
import shlex


def expand_variables(command: str) -> str:
    return os.path.expandvars(command)

def parse_command(command: str) -> tuple[str, list[str]]:
    expanded = expand_variables(command)
    parts = shlex.split(expanded)

    if not parts:
        return "", []

    return parts[0], parts[1:]