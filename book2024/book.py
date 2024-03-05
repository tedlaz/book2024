from .transaction import Transaction as Trn


class Book:
    def __init__(self, *, name: str, transactions: dict | None = None):
        self.name = name
        self.transactions: list[Trn] = []
        if transactions:
            self.transactions = transactions

    @property
    def info(self):
        return f"Book(name={self.name}, TotalTransactions={len(self.transactions)})"

    def __repr__(self):
        return f"Book(name={self.name}, TotalTransactions={len(self.transactions)})"

    def insert(self, transaction: Trn):
        """Insert existing transaction"""
        self.transactions.append(transaction)

    def new_duo(self, dat, journal, per, deb, cred, val):
        """Insert New transaction"""
        trn = Trn.tran_duo(dat, journal, per, deb, cred, val)
        self.transactions.append(trn)

    def balance_sheet(self) -> dict:
        result = {}
        for trn in self.transactions:
            for line in trn.lines:
                result[line.account] = result.get(line.account, 0) + line.value
        return result
