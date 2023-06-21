from rich import print
from rich.box import ROUNDED
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.console import Console
# import traceback from rich
from rich.traceback import install
install(show_locals=True)
console = Console()


def create_columns(*args):
    columns = Columns(args)
    console.print(columns)

#def create_card(title: str, content: str, footer: str):
#    """
#    Creates a card with a given title, content, and footer.
#
#    :param title: A string representing the title of the card.
#    :type title: str
#    :param content: A string representing the content of the card.
#    :type content: str
#    :param footer: A string representing the footer of the card.
#    :type footer: str
#    :return: A Panel object with the given title, content, and footer.
#    :rtype: Panel
#    """
#    title_text = Text(title, style="bold blue")
#    footer_text = Text(footer, style="bold green")
#    panel = Panel(content, title=title_text, footer=footer_text, box=ROUNDED)
#    return panel

def create_card(title: str, content: str, footer: str):
    """
    Creates a card with a given title, content, and footer.

    :param title: A string representing the title of the card.
    :type title: str
    :param content: A string representing the content of the card.
    :type content: str
    :param footer: A string representing the footer of the card.
    :type footer: str
    :return: A Panel object with the given title, content, and footer.
    :rtype: Panel
    """
    title_text = Text(title, style="bold blue")
    footer_text = Text(footer, style="bold green")
    panel = Panel([content, title_text, footer_text], box=ROUNDED)
    return panel


card = create_card("Title", "This is the content of the card", "Footer")
print(card)
create_columns(
    create_card("Title 1", "Content 1", "Footer 1"),
    create_card("Title 2", "Content 2", "Footer 2")
)

