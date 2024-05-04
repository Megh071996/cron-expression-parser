import click

from .expression import Expression

@click.command()
@click.argument('expression')
def on_click(expression):
    '''On click activity.'''
    parser = Expression(expression).parser()
    output = parser.build_table()
    click.echo(output)


if __name__ == '__main__':
    on_click()