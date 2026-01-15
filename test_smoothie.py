import sys
import pytest
from pathlib import Path
from smoothie import smoothie
sys.path.append(str(Path(__file__).parent.parent / "src"))


def test_smoothie():
    assert smoothie(["banana", "strawberry", "yogurt"]) == "Icy Water smoothie with banana, strawberry, yogurt"
    assert smoothie(["banana", "strawberry", "banana"]) == "Icy Water smoothie with banana, strawberry"
    assert smoothie(["yogurt", "strawberry", "banana"]) == "Icy Water smoothie with banana, strawberry, yogurt"
    assert smoothie([]) == "Icy Water!"
    assert smoothie(["raspberry", "blueberry"], base = "apple juice", ice = False) == "Apple Juice smoothie with blueberry, raspberry"
    assert smoothie([], ice = False) == "Just Water!"
    assert smoothie(["banana", 1, True, 6.7]) == "I don't know how to make that smoothie!"
    assert smoothie(["vanilla syrup"], "coffee", False) == "Coffee smoothie with vanilla syrup"
    with pytest.raises(TypeError):
        smoothie(["banana"], 1, True)
    ...  # Continue adding tests here
