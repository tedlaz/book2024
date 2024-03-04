import transaction as trn


def test_transaction():
    tr1 = trn.Transaction.tran_from_list("2024-01-01", [["acc1", 110], ["acc2", -100]])
    tr2 = trn.Transaction.tran_from_list("2024-01-01", [["acc3", 110], ["acc2", -100]])
    print(tr1.ypoloipo)
    print(tr1.accounts_set)
    tr3 = tr1 + tr2
    print(tr3)


def test_trans_duo():
    tr1 = trn.TranDuo("2024-02-21", "'Tameio", "Pelates", 10)
    print(tr1)
