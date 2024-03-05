def capitalize_account(account: str):
    levels = [i.capitalize() for i in account.split(".")]
    return ".".join(levels)


def gr2int(greek_number: str):
    int_part, *dec_parts = greek_number.replace(".", "").split(",")
    if dec_parts:
        dec_part = dec_parts[0]
        if len(dec_part) > 2:
            dec_part = dec_part[:2]
        else:
            dec_part = dec_part + ((2 - len(dec_part[:2])) * "0")
    else:
        dec_part = "00"
    return int(int_part + dec_part)


def int2gr(number: int):
    floatn = number / 100
    nstr = f"{floatn:,.2f}"
    return nstr.replace(",", "|").replace(".", ",").replace("|", ".")


def int2gr_zero_as_space(number: int):
    if number == 0:
        return ""
    return int2gr(number)
