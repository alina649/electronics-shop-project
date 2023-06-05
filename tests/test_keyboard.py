from _pytest.fixtures import fixture

from src.keyboard import KeyBoard

@fixture
def keyBoard():
    return KeyBoard("Смартфон", 10000, 20)

def test_language(keyBoard):
    assert str(keyBoard) == "Смартфон"
    assert str(keyBoard.language) == "EN"

    keyBoard.change_lang()
    assert str(keyBoard.language) == "RU"

    keyBoard.change_lang().change_lang()
    assert str(keyBoard.language) == "RU"



