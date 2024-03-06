import pathlib

from book2024.parse_accounts import parse_accounts

PATH = pathlib.Path(__file__).parent.resolve()


def test_parser():
    accounts = parse_accounts(PATH / "example" / "accounts.txt")
    assert ("Ταμείο.Μετρητά.Τσέπη", "+") in accounts
