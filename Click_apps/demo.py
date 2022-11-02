"""
Demo Click app.
"""
import json
import click
import boto3

@click.group()
def demo():
    pass


@demo.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count:int, name:str):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name.capitalize()}!")

@demo.command()
def list_buckets():
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()["Buckets"]
    for i in buckets:
        print(i["Name"])


if __name__ == '__main__':
    demo()
