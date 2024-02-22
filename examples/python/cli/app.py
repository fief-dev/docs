import click
from fief_client import Fief
from fief_client.integrations.cli import FiefAuth, FiefAuthNotAuthenticatedError

fief = Fief(  # (1)!
    "https://fief.mydomain.com",
    "YOUR_CLIENT_ID",
)
fief_auth = FiefAuth(fief, "./credentials.json")  # (2)!


@click.group()
def cli():
    pass


@cli.command()
def login():
    fief_auth.authorize()  # (3)!


@cli.command()
def hello():
    try:
        userinfo = fief_auth.current_user()  # (4)!
        click.echo(f"Hello {userinfo['email']} 👋")
    except FiefAuthNotAuthenticatedError as e:  # (5)!
        raise click.UsageError("You're not authenticated") from e


@cli.command()
@click.argument("api_route")
def call_api(api_route: str):
    try:
        access_token_info = fief_auth.access_token_info()  # (6)!
        access_token = access_token_info["access_token"]
        click.echo(f"Make API call to {api_route} with access token {access_token}...")
    except FiefAuthNotAuthenticatedError as e:
        raise click.UsageError("You're not authenticated") from e


if __name__ == "__main__":
    cli()
