import pathlib

from parse_accounts import parse_accounts

PATH = pathlib.Path().absolute() / "tests" / "example"


def test_parser():
    omades, accounts = parse_accounts(PATH / "accounts.txt")
    print(omades, accounts)
