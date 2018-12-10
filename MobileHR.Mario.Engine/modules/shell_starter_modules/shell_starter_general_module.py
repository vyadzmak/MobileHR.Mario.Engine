import click
import models.settings.config as config
@click.group()
def general_commands_cli():
    pass

@general_commands_cli.command()
def version():
    click.echo(config.version_code
                )


@general_commands_cli.command()
@click.option('--name', required=True, type=str)
@click.option('--age', required=False, type=int)
def input_params(name,age):
    click.echo("Name = "+name+"; age = "+str(age)
                )