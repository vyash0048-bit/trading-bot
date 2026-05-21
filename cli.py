import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

app = typer.Typer(help="Binance Futures Testnet Trading Bot", invoke_without_command=True)
console = Console()
logger = setup_logger()

@app.command("order")
def order(
    symbol: str = typer.Option(..., help="Trading pair e.g. BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price (required for LIMIT orders)"),
):
    """Place a market or limit order on Binance Futures Testnet."""

    console.rule("[bold blue]Order Request Summary")
    rprint(f"  Symbol    : [cyan]{symbol.upper()}[/cyan]")
    rprint(f"  Side      : [green]{side.upper()}[/green]")
    rprint(f"  Type      : [yellow]{order_type.upper()}[/yellow]")
    rprint(f"  Quantity  : {quantity}")
    if price:
        rprint(f"  Price     : {price}")
    console.rule()

    try:
        validate_inputs(symbol, side, order_type, quantity, price)

        client = BinanceClient()
        response = place_order(client, symbol, side, order_type, quantity, price)

        console.rule("[bold green]✅ Order Placed Successfully")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field", style="dim")
        table.add_column("Value")

        fields = ["orderId", "symbol", "side", "type", "status",
                  "origQty", "executedQty", "avgPrice", "price"]
        for f in fields:
            if f in response:
                table.add_row(f, str(response[f]))

        console.print(table)

    except ValueError as e:
        rprint(f"\n[red]❌ Validation/API Error:[/red] {e}")
        logger.error(f"Order failed: {e}")
        raise typer.Exit(code=1)

    except Exception as e:
        rprint(f"\n[red]❌ Unexpected Error:[/red] {e}")
        logger.exception("Unexpected error during order placement")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()