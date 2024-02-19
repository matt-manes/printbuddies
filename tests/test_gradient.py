import random
from math import isclose
from typing import Any

import pytest

import printbuddies


def test__RGB_str():
    color = printbuddies.RGB(100.8, 100.3, 100.1)
    assert str(color) == "[rgb(101,100,100)]"


def test__RGB_arithmetic():
    color1 = printbuddies.RGB(100, 100, 100)
    color2 = printbuddies.RGB(25, 50, 75)
    sub = color1 - color2
    assert sub.r == 75
    assert sub.g == 50
    assert sub.b == 25
    add = color1 + color2
    assert add.r == 125
    assert add.g == 150
    assert add.b == 175
    div = color2 / 10
    assert div.r == 2.5
    assert div.g == 5
    assert div.b == 7.5
    mul = color2 * 0.1
    assert mul.r == 2.5
    assert mul.g == 5
    assert mul.b == 7.5


def test__RGB_from_name():
    color = printbuddies.RGB(name="pink1")
    assert color.r
    assert color.g
    assert color.b


@pytest.mark.parametrize("steps", [2, 22, 101, 35927])
def test___Blender__get_sequence(steps: int):
    blender = printbuddies.gradient._Blender(  # type:ignore
        printbuddies.RGB(51, 101, 231), printbuddies.RGB(113, 21, 254)
    )
    sequence = blender.get_sequence(steps)  # type: ignore
    for i, color in [(0, blender.start), (-1, blender.stop)]:
        assert str(sequence[i]) == str(color)


@pytest.mark.parametrize(
    "colors",
    [
        ([printbuddies.ColorMap().grey0, printbuddies.ColorMap().grey100]),
        (["grey0", "grey100"]),
        (["pink1", "green", "orchid1", "bright_red", (0, 0, 255)]),
        (["pink1", "turquoise2", "red"]),
    ],
)
def test__Gradient__parse(colors: list[Any]):
    gradient = printbuddies.Gradient(colors)
    text = "0123456789 013asdfas dseifjs; lofie"
    richtext = gradient.apply(text)
    assert richtext.startswith(str(gradient[0]))
    assert richtext.endswith(f"{gradient[-1]}{text[-1]}[/]")


def test__Gradient_append():
    gradient = printbuddies.Gradient(["red", "blue"])
    assert len(gradient) == 2
    gradient.append("pink1")
    assert len(gradient) == 3
    assert gradient[-1].name == "pink1"


def test__Gradient_from_gradient():
    gradient = printbuddies.Gradient(["red", "blue"])
    assert gradient[0].name == "red"
    assert gradient[1].name == "blue"
    gradient = printbuddies.Gradient(gradient[::-1])
    assert gradient[0].name == "blue"
    assert gradient[1].name == "red"


def test__Gradient_insert():
    gradient = printbuddies.Gradient(["red", "blue", "green"])
    assert gradient[1].name == "blue"
    gradient.insert(1, "pink1")
    assert gradient[1].name == "pink1"


def test__Gradient_extend():
    gradient = printbuddies.Gradient(["red", "blue"])
    gradient.extend(["green", "pink1", "magenta"])
    assert len(gradient) == 5
    assert gradient[-1].name == "magenta"


def test__Gradient___set_item__():
    gradient = printbuddies.Gradient(["red", "blue", (123, 123, 123)])
    gradient[1] = "pink1"
    assert gradient[1].name == "pink1"


def test__Gradient__get_sequence():
    gradient = printbuddies.Gradient(["red", "orange1", "blue", "pink1", "green"])
    sequence = gradient.get_sequence(13)
    check: list[str] = [str(color) for color in sequence]
    assert len(sequence) == len(set(check))


def test__Gradient_more_colors_than_text():
    colors = printbuddies.ColorMap()
    text = "Just some sample text to do a lil testing on."
    gradient = printbuddies.Gradient(
        [random.choice(colors) for _ in range(len(text) + 10)]
    )
    import rich

    rich.print(gradient.apply(text))
