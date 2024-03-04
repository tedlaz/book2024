from datetime import date


class TransactionLine:
    def __init__(self, account, value: int):
        self.account = account
        self.value: int = value

    @property
    def debit(self):
        return self.value if self.value > 0 else 0

    @property
    def credit(self):
        return -self.value if self.value < 0 else 0

    def __repr__(self):
        return f"TransactionLine(account={self.account}, value={self.value})"


class Transaction:
    def __init__(self, adate: date | str, lines: list[TransactionLine]):
        if isinstance(adate, date):
            self.date = adate
        else:
            self.date = date.fromisoformat(adate)
        self.lines = lines

    @property
    def ypoloipo(self):
        return sum([i.value for i in self.lines])

    @property
    def accounts_set(self):
        return set([i.account for i in self.lines])

    @classmethod
    def tran_from_list(cls, adate, lines):
        trlines = [TransactionLine(acc, val) for acc, val in lines]
        return cls(adate, trlines)

    @classmethod
    def tran_from_dict(cls, adate, lines):
        trlines = [TransactionLine(acc, val) for acc, val in lines.items()]
        return cls(adate, trlines)

    def __repr__(self):
        return f"Transaction(date={self.date}, lines={self.lines})"

    def __add__(self, another):

        if self.date != another.date:
            raise ValueError("Not Same Date")

        accs = {}

        for lin in self.lines:
            accs[lin.account] = accs.get(lin.account, 0) + lin.value

        for lin in another.lines:
            accs[lin.account] = accs.get(lin.account, 0) + lin.value

        return self.tran_from_dict(self.date, accs)


class TranDuo(Transaction):
    def __init__(self, adate: date | str, acc_debit, acc_credit, value):
        lines = [TransactionLine(acc_credit, value), TransactionLine(acc_debit, -value)]
        super().__init__(adate, lines)
