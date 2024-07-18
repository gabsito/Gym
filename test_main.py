import pytest
from main import calculate_total_cost

def test_calculate_total_cost():
    assert calculate_total_cost(100, 50, False) == 150
    assert calculate_total_cost(100, 50, True) == 172.5
    assert calculate_total_cost(300, 150, False) == 400
    assert calculate_total_cost(100, 150, True) == 184  # 15% surcharge applied
    assert calculate_total_cost(150, 100, False) == 230  # $20 discount applied
    assert calculate_total_cost(200, 250, False) == 400  # $50 discount applied

if __name__ == "__main__":
    pytest.main()