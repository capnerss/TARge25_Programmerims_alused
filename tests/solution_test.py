"""Tests for solution."""
import pytest
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False

def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(2, False) is False

def test__students_study__day_with_coffee__studying():
    """During day with coffee students study."""
    assert students_study(10, True) is True

def test__students_study__day_without_coffee__no_studying():
    """During day without coffee students do not study."""
    assert students_study(12, False) is False

def test__students_study__evening_with_coffee__studying():
    """During evening with coffee students study."""
    assert students_study(20, True) is True

def test__students_study__evening_without_coffee__studying():
    """During evening without coffee students study."""
    assert students_study(22, False) is True

def test__students_study__boundaries():
    """Test boundary conditions for times."""
    assert students_study(1, True) is False    # Öö algus
    assert students_study(4, False) is False   # Öö lõpp
    assert students_study(5, True) is True     # Päeva algus
    assert students_study(17, False) is False  # Päeva lõpp
    assert students_study(18, False) is True   # Õhtu algus
    assert students_study(24, False) is True   # Õhtu lõpp


def test__lottery__all_fives__returns_10():
    """When all numbers are 5, victory is 10."""
    assert lottery(5, 5, 5) == 10

def test__lottery__all_same_not_fives__returns_5():
    """When all numbers are same but not 5, victory is 5."""
    assert lottery(2, 2, 2) == 5
    assert lottery(9, 9, 9) == 5

def test__lottery__b_and_c_different_from_a__returns_1():
    """When b and c are different from a, victory is 1."""
    assert lottery(1, 2, 3) == 1
    assert lottery(5, 1, 1) == 1

def test__lottery__b_equals_a_but_c_different__returns_0():
    """When b equals a but c is different, victory is 0."""
    assert lottery(2, 2, 3) == 0

def test__lottery__c_equals_a_but_b_different__returns_0():
    """When c equals a but b is different, victory is 0."""
    assert lottery(4, 1, 4) == 0


def test__fruit_order__exact_match_with_big_baskets():
    """When big baskets can exactly fulfill the order."""
    assert fruit_order(0, 2, 10) == 0

def test__fruit_order__match_with_big_and_small():
    """When order needs both big and small baskets."""
    assert fruit_order(2, 2, 12) == 2

def test__fruit_order__more_big_baskets_than_needed():
    """When there are more big baskets than the order needs."""
    # Tellimus on 12kg. Vaja läheb 2 suurt (10kg) ja 2 väikest (2kg).
    assert fruit_order(3, 5, 12) == 2

def test__fruit_order__not_enough_small_baskets_returns_minus_1():
    """When there are not enough small baskets to finish the order."""
    # Tellimus 14kg. Kasutame 2 suurt (10kg), aga 4kg jaoks on vaid 1 väike korv.
    assert fruit_order(1, 2, 14) == -1

def test__fruit_order__only_small_baskets_used():
    """When order is smaller than one big basket or no big baskets available."""
    assert fruit_order(6, 0, 6) == 6
    assert fruit_order(5, 5, 4) == 4

def test__fruit_order__not_enough_total_capacity():
    """When the total capacity is smaller than the order."""
    assert fruit_order(1, 1, 10) == -1

def test__fruit_order__zero_ordered():
    """When ordered amount is 0."""
    assert fruit_order(5, 5, 0) == 0