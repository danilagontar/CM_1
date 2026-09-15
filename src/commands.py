commands = {"ls", "cd", "exit"}

def execute_ls(arguments: list[str]) -> str:
    return format_stub("ls", arguments)

def execute_cd(arguments: list[str]) -> str:
    return format_stub("cd", arguments)

def format_stub(name: str, arguments: list[str]) -> str:
    if not arguments:
        return name

    return f"{name} {' '.join(arguments)}"