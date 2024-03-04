import pathlib

from parse_transactions import parse_trans

PATH = pathlib.Path().absolute() / "tests" / "example"


def test_parser():
    trans = parse_trans(PATH / "trn01.txt")
    print(trans)
