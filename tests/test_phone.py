from _pytest.fixtures import fixture

from src.phone import Phone

@fixture
def phone():
    return Phone("Смартфон", 10000, 20, 5)
def test_repr(phone):
    assert repr(phone) == "Phone('Смартфон', 10000, 20, 5)"

def test_number_of_sim(phone):
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5








