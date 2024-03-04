def parse_accounts(filename: str):
    omades = {}
    accounts = []

    with open(filename, encoding="utf-8") as file:

        for line in file.readlines():

            line = line.strip()

            if len(line) < 3:
                continue

            if line.startswith(">"):
                _, omada, typos = line.split()
                omades[omada] = typos

            if line[0] in "+-*":
                account_type, account = line.split()
                accounts.append((account, account_type))

    return omades, accounts
