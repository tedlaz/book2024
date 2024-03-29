import pathlib

from book2024.parse_transactions import parse_trans

PATH = pathlib.Path(__file__).parent.resolve()


def test_parser():
    trans = parse_trans(PATH / "example" / "trn01.txt")
    atrn = trans[0]
    assert atrn["value"] == "125,43"
