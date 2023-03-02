import typer
from main import upstash

event = typer.Typer()


@event.command()
def add(project: str, name: str, description: str) -> None:
    """
    Create a new event. Specify, in order:
        - the project it belongs to
        - its name
        - its description
    """

    project_name = f"project:{project}"

    if not upstash.exists(project_name):
        print("The project with the specified name doesn't exist")
        raise typer.Exit(code=1)

    if upstash.json().objlen(name=project_name, path=f'$.{name}'):
        print("An event with this name already exists")
        raise typer.Exit(code=1)

    upstash.json().strappend(name=project_name, path="$", value=f'"{name}": { "description": {description} }')


@event.command()
def remove(project: str, name: str) -> None:
    """
    Delete an event. Specify the project it belongs to and its name.
    """

    project_name = f"project:{project}"
    event_path = f'$.{name}'

    if not upstash.exists(project_name):
        print("The project with the specified name doesn't exist")
        raise typer.Exit(code=1)

    if not upstash.json().objlen(project_name, event_path):
        print("The event with the specified name doesn't exist")
        raise typer.Exit(code=1)

    upstash.json().delete(key=project_name, path=event_path)