from datetime import date

import pytest

import book2024.transaction as trn


def test_transaction():
    jrn = "normal"
    tr1 = trn.Transaction.tran_from_list(
        "2024-01-01", jrn, "inv1", [["acc1", 110], ["acc2", -100]]
    )
    tr2 = trn.Transaction.tran_from_list(
        "2024-01-01", jrn, "inv2", [["acc3", 110], ["acc2", -100]]
    )
    assert tr1.ypoloipo == 10
    assert tr1.lines[0].debit == 110
    assert tr1.lines[0].credit == 0
    assert tr1.lines[1].debit == 0
    assert tr1.lines[1].credit == 100
    tr3 = tr1 + tr2
    assert tr3.date.isoformat() == "2024-01-01"
    assert tr3.par == "inv1,inv2"


def test_trans_duo():
    tr1 = trn.Transaction.tran_duo(
        "2024-02-21", "normal", "inv1", "Tameio", "Pelates", 10
    )
    assert tr1.lines_as_dict == {"Tameio": 10, "Pelates": -10}
    lol = tr1.as_list_of_lines
    fin = [i.model_dump() for i in lol]
    assert fin == [
        {
            "date": date(2024, 2, 21),
            "journal": "normal",
            "par": "inv1",
            "account": "Tameio",
            "value": 10,
        },
        {
            "date": date(2024, 2, 21),
            "journal": "normal",
            "par": "inv1",
            "account": "Pelates",
            "value": -10,
        },
    ]


def test_trans_duo_remove_zerovalues():
    tr1 = trn.Transaction.tran_duo("2024-02-21", "normal", "inv1", "Tameio", "mal", 10)
    tr2 = trn.Transaction.tran_duo("2024-02-21", "normal", "inv1", "mal", "Pelates", 10)
    tr3 = tr1 + tr2
    assert tr3.par == "inv1"
    assert "mal" not in tr3.list_of_accounts


def test_trans_duo2():
    tr1 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "mis.cost", "m", 1000)
    tr2 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "mis.erg", "m", 240)
    tr3 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "m", "efka", 440)
    tr4 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "m", "pis1", 600)
    tr5 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "m", "pis2", 100)

    final = tr1 + tr2 + tr3 + tr4 + tr5
    assert final.date.isoformat() == "2024-02-21"
    assert final.journal == "n"
    assert final.par == "i1"


def test_trans_add_error_journal():
    tr1 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "mis", "m", 1000)
    tr2 = trn.Transaction.tran_duo("2024-02-21", "n2", "i1", "m", "efka", 440)
    with pytest.raises(ValueError) as err:
        tr1 + tr2
    assert str(err.value) == "Not same journal"


def test_trans_add_error_date():
    tr1 = trn.Transaction.tran_duo("2024-02-21", "n", "i1", "mis", "m", 1000)
    tr2 = trn.Transaction.tran_duo("2024-02-22", "n", "i1", "m", "efka", 440)
    with pytest.raises(ValueError) as err:
        tr1 + tr2
    assert str(err.value) == "Not Same Date"
