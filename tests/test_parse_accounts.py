import pathlib

from book2024.parse_accounts import parse_accounts

PATH = pathlib.Path(__file__).parent.resolve()


def test_parser():
    omades, accounts = parse_accounts(PATH / "example" / "accounts.txt")
    print(omades, accounts)
