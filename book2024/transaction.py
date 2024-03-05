from __future__ import annotations

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
    def __init__(
        self, adate: date | str, journal: str, par: str, lines: list[TransactionLine]
    ):

        self.journal = journal
        self.par = par

        if isinstance(adate, date):
            self.date = adate
        else:
            self.date = date.fromisoformat(adate)

        self.lines = lines

    @property
    def ypoloipo(self):
        return sum([i.value for i in self.lines])

    @classmethod
    def tran_from_list(cls, adate, journal, par, lines):
        trlines = [TransactionLine(acc, val) for acc, val in lines]
        return cls(adate, journal, par, trlines)

    @classmethod
    def tran_from_dict(cls, adate, journal, par, lines):
        trlines = [TransactionLine(acc, val) for acc, val in lines.items()]
        return cls(adate, journal, par, trlines)

    @classmethod
    def tran_duo(cls, adate, journal, par, acc_debit, acc_credit, value):
        lines = [TransactionLine(acc_debit, value), TransactionLine(acc_credit, -value)]
        return cls(adate, journal, par, lines)

    def __repr__(self):
        return f"Transaction(date={self.date}, journal={self.journal}, par={self.par}, lines={self.lines})"

    def __add__(self, other: Transaction):

        if self.date != other.date:
            raise ValueError("Not Same Date")

        if self.journal != other.journal:
            raise ValueError("Not same journal")

        accs = {}
        for lin in self.lines + other.lines:
            accs[lin.account] = accs.get(lin.account, 0) + lin.value
        accs = {key: val for key, val in accs.items() if val != 0}

        par_equal = self.par.lower() == other.par.lower()
        npr = self.par if par_equal else f"{self.par},{other.par}"

        return self.tran_from_dict(self.date, self.journal, npr, accs)
