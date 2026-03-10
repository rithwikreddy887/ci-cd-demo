from app.utils import add, multiply

def test_combined_operations():
    result = multiply(add(2,3), 2)
    assert result == 10
    