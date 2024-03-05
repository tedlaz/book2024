import re

LINE_STARTS_WITH_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def parse_trans(filename: str):
    transactions = []
    with open(filename, encoding="utf-8") as file:

        for line in file.readlines():

            line = line.strip()

            if len(line) < 3:
                continue

            if LINE_STARTS_WITH_ISO_DATE.findall(line):
                date, journal, acc_debit, acc_credit, value, *rest = line.split()
                transactions.append(
                    {
                        "journal": journal,
                        "date": date,
                        "acc_debit": acc_debit,
                        "acc_credit": acc_credit,
                        "value": value,
                        "rest": " ".join(rest),
                    }
                )
    return transactions
