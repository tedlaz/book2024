import pathlib

from book2024.parse_omades import parse_omades

PATH = pathlib.Path(__file__).parent.resolve()


def test_omades_parser():
    omades = parse_omades(PATH / "example" / "omades.txt")
    assert ("Εξοδα", "ejoda") in omades
