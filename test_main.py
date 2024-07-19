import pytest
import subprocess
from main import calculate_total_cost


def test_calculate_total_cost():
    assert calculate_total_cost(100, 50, False) == 150
    assert calculate_total_cost(100, 50, True) == 172.5
    assert calculate_total_cost(300, 150, False) == 450
    assert calculate_total_cost(100, 150, True) == 287.5  # 15%
    assert calculate_total_cost(150, 100, False) == 250  # $20 discount applied
    assert calculate_total_cost(200, 250, False) == 450  # $50 discount applied


if __name__ == "__main__":
    result = subprocess.run(['pytest', 'test_main.py', '--tb=short', '-v'], capture_output=True, text=True)
    with open('test_results.txt', 'w') as f:
        f.write(result.stdout)
    pytest.main()
