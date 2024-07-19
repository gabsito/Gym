import pytest
from main import calculate_total_cost
from main import get_membership_cost
from main import get_feature_cost
from main import apply_group_discount


def test_calculate_total_cost_no_premium():
    assert calculate_total_cost(50, 30, premium_features=False) == 80


def test_calculate_total_cost_with_surcharge():
    assert calculate_total_cost(100, 50, premium_features=True) == 172.50


def test_get_membership_cost_valid():
    assert get_membership_cost('1') == 50
    assert get_membership_cost('2') == 100
    assert get_membership_cost('3') == 150


def test_get_membership_cost_invalid():
    assert get_membership_cost('InvalidPlan') == 0


def test_get_feature_cost_valid():
    assert get_feature_cost(['1', '2']) == 50


def test_get_feature_cost_invalid():
    assert get_feature_cost(['1', 'InvalidFeature']) == 0


def test_apply_group_discount_no_discount():
    assert apply_group_discount(100, 1) == 100


def test_apply_group_discount_with_discount():
    assert apply_group_discount(100, 2) == 90
