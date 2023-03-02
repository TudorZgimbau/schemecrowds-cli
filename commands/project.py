import typer
from main import upstash

project = typer.Typer()


@project.command()
def add(name: str, description: str) -> None:
    """
    Create a new project. You need to specify, in order:
        - its name
        - its description
    """

    project_name = f"project:{name}"

    if upstash.exists(project_name):
        print("A project with this name already exists")
        raise typer.Exit(code=1)

    upstash.json().set(name=project_name, path="$", value=f'{"description": {description}}')


@project.command()
def delete(name: str) -> None:
    """
    Delete a project. Specify its name
    """

    project_name = f"project:{name}"

    if not upstash.exists(project_name):
        print("The project with the specified name doesn't exist")
        raise typer.Exit(code=1)

    upstash.delete(project_name)
