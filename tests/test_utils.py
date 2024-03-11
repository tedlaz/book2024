import book2024.utils as utl


def test_gr2int():
    assert utl.gr2int("3") == 300
    assert utl.gr2int("3.000") == 300000
    assert utl.gr2int("3.000,") == 300000
    assert utl.gr2int("3.000,14") == 300014
    assert utl.gr2int("-3.000,14") == -300014
    assert utl.gr2int("-3.000,145") == -300014


def test_int2gr():
    assert utl.int2gr(0) == "0,00"
    assert utl.int2gr(-0) == "0,00"
    assert utl.int2gr(32) == "0,32"
    assert utl.int2gr(1) == "0,01"
    assert utl.int2gr(-1) == "-0,01"
    assert utl.int2gr(100) == "1,00"
    assert utl.int2gr(101) == "1,01"
    assert utl.int2gr(110101) == "1.101,01"


def test_int2gr_zero_as_space():
    assert utl.int2gr_zero_as_space(0) == ""
    assert utl.int2gr_zero_as_space(-0) == ""
    assert utl.int2gr_zero_as_space(1000) == "10,00"


def test_capitalize_account():
    assert utl.capitalize_account("δοκιμή.ξανά") == "Δοκιμή.Ξανά"
    assert utl.capitalize_account("δοκιΜή.ξανά") == "Δοκιμή.Ξανά"


def test_add_dic2_to_dic1():
    dic1 = {"a": 10, "b": 20}
    dic2 = {"b": 5, "c": 30}
    utl.add_dic2_to_dic1(dic1, dic2)
    assert dic1 == {"a": 10, "b": 25, "c": 30}
