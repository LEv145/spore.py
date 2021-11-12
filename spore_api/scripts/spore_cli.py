#!./venv/bin/python3
from typing import Optional
import asyncclick as click

from spore_api import SporeClient
from spore_api.enums import AssetType, ViewType


_client = SporeClient()


@click.group()
async def cli():
    """CLI for Spore REST API"""


@cli.command()
async def get_stats():
    async with _client as client:
        result = await client.get_stats()
        click.echo(result.to_json())


@cli.command()
@click.argument("asset_id", type=int)
async def get_creature(asset_id: int):
    async with _client as client:
        result = await client.get_creature(
            asset_id=asset_id
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("username", type=str)
async def get_user_info(username: str):
    async with _client as client:
        result = await client.get_user_info(
            username=username
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("username", type=str)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
async def get_user_assets(username: str, start_index: int, length: int):
    async with _client as client:
        result = await client.get_user_assets(
            username=username,
            start_index=start_index,
            length=length
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("username", type=str)
async def get_user_sporecasts(username: str):
    async with _client as client:
        result = await client.get_user_sporecasts(
            username=username
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("username", type=str)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
async def get_user_achievements(username: str, start_index: int, length: int):
    async with _client as client:
        result = await client.get_user_achievements(
            username=username,
            start_index=start_index,
            length=length
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("username", type=str)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
async def get_user_buddies(username: str, start_index: int, length: int):
    async with _client as client:
        result = await client.get_user_buddies(
            username=username,
            start_index=start_index,
            length=length
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("username", type=str)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
async def get_user_subscribers(username: str, start_index: int, length: int):
    async with _client as client:
        result = await client.get_user_subscribers(
            username=username,
            start_index=start_index,
            length=length
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("asset_id", type=int)
async def get_asset_info(asset_id: int):
    async with _client as client:
        result = await client.get_asset_info(
            asset_id=asset_id
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("asset_id", type=int)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
async def get_asset_comments(asset_id: int, start_index: int, length: int):
    async with _client as client:
        result = await client.get_asset_comments(
            asset_id=asset_id,
            start_index=start_index,
            length=length
        )
        click.echo(result.to_json())


@cli.command()
@click.argument("sporecast_id", type=int)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
async def get_sporecast_assets(sporecast_id: int, start_index: int, length: int):
    async with _client as client:
        result = await client.get_sporecast_assets(
            sporecast_id=sporecast_id,
            start_index=start_index,
            length=length
        )
        click.echo(result.to_json())


@cli.command()
@click.argument(
    "view_type",
    type=click.Choice(ViewType._member_names_, case_sensitive=False)
)
@click.argument("start_index", type=int, default=1)
@click.argument("length", type=int, default=10)
@click.argument(
    "asset_type",
    type=click.Choice(AssetType._member_names_, case_sensitive=False),
    required=False
)
async def assets_search(view_type: str, start_index: int, length: int, asset_type: Optional[str]):
    async with _client as client:
        result = await client.assets_search(
            view_type=ViewType[view_type],
            start_index=start_index,
            length=length,
            asset_type=(
                asset_type
                if asset_type is None else
                AssetType[asset_type]
            )
        )
        click.echo(result.to_json())


if __name__ == "__main__":
    cli()
