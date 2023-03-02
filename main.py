import typer
from commands import event, project, parameter
from redis import Redis

upstash = Redis(
    host='',
    port=0,
    password='',
    ssl=True
)

app = typer.Typer()

"""
 project:<name>
 {
    "description": ,
    <event1>: {
        "description": ,
        <param1>: {
            "description": ,
            "type": ,
        }
    }
 }
"""

app.add_typer(event.event, name="event", help="Manage events in a project")
app.add_typer(project.project, name="project", help="Manage projects")
app.add_typer(parameter.parameter, name="parameter", help="Manage parameters in an event")

if __name__ == "__main__":
    app()
