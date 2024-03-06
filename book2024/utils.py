def capitalize_account(account: str):
    """
    abc.def.get becomes Abc.Def.Get
    """
    levels = [i.capitalize() for i in account.split(".")]
    return ".".join(levels)


def gr2int(greek_number: str):
    """
    Transform a number of type 999.999,99 string to 99999999 integer
    """
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
    """
    Transform an integer of type 99999999 to 999.999,99 string
    """
    floatn = number / 100
    nstr = f"{floatn:,.2f}"
    return nstr.replace(",", "|").replace(".", ",").replace("|", ".")


def int2gr_zero_as_space(number: int):
    """
    Like int2gr except for 0 witch becomes empty space("")
    """
    if number == 0:
        return ""
    return int2gr(number)
