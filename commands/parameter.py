import typer
from main import upstash

parameter = typer.Typer()


@parameter.command()
def add(project: str, event: str, name: str, description: str, type: str) -> None:
    """
    Create a new parameter. Specify, in order:
        - the project it belongs to
        - the event it belongs to
        - its name
        - its description
        - its type
    """

    project_name = f"project:{project}"

    if not upstash.exists(project_name):
        print("The project with the specified name doesn't exist")
        raise typer.Exit(code=1)

    if not upstash.json().objlen(name=project_name, path=f'$.{event}'):
        print("The event with the specified name doesn't exist")
        raise typer.Exit(code=1)

    if upstash.json().objlen(name=project_name, path=f'$.{event}.{name}'):
        print("A parameter with this name already exists")
        raise typer.Exit(code=1)

    upstash.json().strappend(
        name=project_name,
        path=f'$.{event}',
        value=f'"{name}": { "description": {description}, "type": {type} }'
    )


@parameter.command()
def delete(project: str, event: str, name: str) -> None:
    """
    Delete a parameter. Specify, in order:
        - the project it belongs to
        - the event it belongs to
        - its name
    """

    project_name = f"project:{project}"
    parameter_path = f'$.{event}.{name}'

    if not upstash.exists(project_name):
        print("The project with the specified name doesn't exist")
        raise typer.Exit(code=1)

    if not upstash.json().objlen(name=project_name, path=f'$.{event}'):
        print("The event with the specified name doesn't exist")
        raise typer.Exit(code=1)

    if not upstash.json().objlen(name=project_name, path=parameter_path):
        print("The parameter with the specified name doesn't exist")
        raise typer.Exit(code=1)

    upstash.json().delete(key=project_name, path=parameter_path)