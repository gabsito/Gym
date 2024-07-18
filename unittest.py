# test_gym_membership.py

import pytest
from main import calculate_total_cost, get_membership_cost, get_feature_cost, apply_group_discount

def test_calculate_total_cost_no_premium():
    assert calculate_total_cost(50, 30, premium_features=False) == 80

def test_calculate_total_cost_with_discount():
    assert calculate_total_cost(150, 100, premium_features=False) == 230

def test_calculate_total_cost_with_surcharge():
    assert calculate_total_cost(100, 50, premium_features=True) == 172.50

def test_get_membership_cost_valid():
    assert get_membership_cost('Basic') == 50
    assert get_membership_cost('Premium') == 100
    assert get_membership_cost('Family') == 150

def test_get_membership_cost_invalid():
    with pytest.raises(ValueError, match="Invalid membership plan"):
        get_membership_cost('InvalidPlan')

def test_get_feature_cost_valid():
    assert get_feature_cost(['Personal Training', 'Group Classes']) == 50

def test_get_feature_cost_invalid():
    with pytest.raises(ValueError, match="Invalid feature: InvalidFeature"):
        get_feature_cost(['Personal Training', 'InvalidFeature'])

def test_apply_group_discount_no_discount():
    assert apply_group_discount(100, 1) == 100

def test_apply_group_discount_with_discount():
    assert apply_group_discount(100, 2) == 90