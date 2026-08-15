from datetime import date
from seasons import minutes
import pytest

def test_valid_outputs():
    assert minutes(date(2000, 1, 1), date(2001, 1, 1)) == 527040
    assert minutes(date(2024, 1, 1), date(2026, 1, 1)) == 1052640

def test_invalid_outputs():
    with pytest.raises(TypeError):
        minutes("cat", "dog")
        minutes("2 January 2006", "2 January 2007")
    assert minutes(date(2027, 1, 1), date(2026, 1, 1)) == -525600
