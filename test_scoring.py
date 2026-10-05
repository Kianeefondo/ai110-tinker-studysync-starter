"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating
from scoring_helpers import apply_streak_bonus


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_apply_streak_bonus_adds_two_points_per_day():
    assert apply_streak_bonus(55, 3) == 61


def test_apply_streak_bonus_is_capped_at_100():
    assert apply_streak_bonus(95, 3) == 100


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).
