from src.commands import execute_cd, execute_ls
from src.parser import parse_command

def test_parse_command() -> None:
    name, arguments = parse_command("ls test.txt")
    assert name == "ls"
    assert arguments == ["test.txt"]

def test_environment_variable_expansion() -> None:
    name, arguments = parse_command("cd $HOME")
    assert name == "cd"
    assert arguments[0] != "$HOME"

def test_ls_stub() -> None:
    assert execute_ls([]) == "ls"

def test_ls_with_argument() -> None:
    assert execute_ls(["file.txt"]) == "ls file.txt"

def test_cd_stub() -> None:
    assert execute_cd(["test"]) == "cd test"

def test_cd_without_argument() -> None:
    result = execute_cd([])
    assert result == "Error: cd: missing argument"

def test_unknown_command() -> None:
    from src.commands import commands
    assert "unknown" not in commands