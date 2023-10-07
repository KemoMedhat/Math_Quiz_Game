from project import Generate_Problem
from project import Generate_chocies
from project import Check_Answer


def test_Generate_Problem():
    test = Generate_Problem()
    assert len(test) == 3
    assert test[0] >= 0 and test[0] <= 100
    assert test[2] >= 0 and test[2] <= 100
    assert test[1] == "*" or test[1] == "+"


def test_Generate_chocies():
    test = Generate_chocies(5, "*", 10)
    test2 = Generate_chocies(10, "+", 20)
    assert len(test) == 3
    assert 50 in test
    assert 30 in test2


def test_Check_Answer():
    assert Check_Answer(-1) == False
