import pytest

from book2024.book import Book
from book2024.transaction import Transaction as Trn


@pytest.fixture
def trans():
    return [
        Trn.tran_duo("2024-01-01", "in", "inv1", "20.00", "50.00", 100),
        Trn.tran_duo("2024-01-02", "in", "inv2", "20.00", "50.00", 110),
        Trn.tran_duo("2024-01-02", "in", "inv3", "24.00", "50.00", 120),
        Trn.tran_duo("2024-01-03", "in", "inv4", "20.00", "50.00", 130),
        Trn.tran_duo("2024-01-04", "in", "inv5", "20.00", "50.00", 140),
        Trn.tran_duo("2024-01-04", "in", "inv6", "20.01", "50.01", 150),
    ]


def test_book1(trans):
    book = Book(name="MyBook", transactions=trans)
    tra = Trn.tran_duo("2024-03-04", "in", "inv78", "cash", "income", 300)
    book.insert(tra)
    book.new_duo("2024-03-05", "m", "inv45", "customers", "income", 125)
    bal = book.balance_sheet()
    assert book.info == "Book(name=MyBook, TotalTransactions=8)"
    assert repr(book) == "Book(name=MyBook, TotalTransactions=8)"
    assert bal["customers"] == 125
    assert bal["cash"] == 300
    assert bal["income"] == -425
