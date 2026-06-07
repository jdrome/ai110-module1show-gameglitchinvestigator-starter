"""Regression tests for the difficulty-range bug fixed in app.py.

Original bug: get_range_for_difficulty had the Normal and Hard ranges
swapped (Normal returned 1-100, Hard returned 1-50). Combined with the
secret only ever being generated on first load while sitting on the
default "Normal" difficulty, the secret answer was always drawn from
1-100 regardless of the selected difficulty.

app.py executes Streamlit UI code at import time (which requires a live
Streamlit runtime), so we load only the pure get_range_for_difficulty
function from its source via AST instead of importing the module.
"""

import ast
import random
from pathlib import Path

import pytest

APP_PATH = Path(__file__).resolve().parent.parent / "app.py"


def _load_function(name: str):
    """Extract a single top-level function from app.py without running
    the module's Streamlit UI code."""
    tree = ast.parse(APP_PATH.read_text())
    func_node = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    module = ast.Module(body=[func_node], type_ignores=[])
    namespace = {"random": random}
    exec(compile(module, str(APP_PATH), "exec"), namespace)
    return namespace[name]


get_range_for_difficulty = _load_function("get_range_for_difficulty")


@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 50)),
        ("Hard", (1, 100)),
    ],
)
def test_range_matches_difficulty(difficulty, expected):
    """Each difficulty must map to its correct inclusive range."""
    assert get_range_for_difficulty(difficulty) == expected


def test_normal_and_hard_not_swapped():
    """Targets the exact bug: Normal must not be 1-100 and Hard must not be 1-50."""
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)
    assert get_range_for_difficulty("Normal")[1] != 100
    assert get_range_for_difficulty("Hard")[1] != 50


def test_upper_bounds_increase_with_difficulty():
    """Harder difficulties must widen the range, never shrink it."""
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


def test_all_ranges_start_at_one():
    """Every difficulty should start its range at 1."""
    for difficulty in ("Easy", "Normal", "Hard"):
        low, _ = get_range_for_difficulty(difficulty)
        assert low == 1
