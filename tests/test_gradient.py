import random
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


def test___gradient_Blender():
    blender = printbuddies.gradient._Blender(  # type:ignore
        printbuddies.RGB(100, 100, 100), printbuddies.RGB(200, 200, 200)
    )
    text = "01234 567\t89\n0"
    steps = blender._get_num_steps(text)  # type:ignore
    step_sizes = blender._get_step_sizes(steps)  # type:ignore
    assert step_sizes == printbuddies.RGB(10, 10, 10)
    midcolor = blender._get_blended_color(5, step_sizes)  # type:ignore
    assert midcolor == printbuddies.RGB(150, 150, 150)
    richtext = blender.apply(text)
    assert richtext.startswith(str(blender.start))
    assert richtext.endswith(f"{blender.stop}{text[-1]}[/]")


@pytest.mark.parametrize(
    "start, stop",
    [
        (printbuddies.ColorMap().grey0, printbuddies.ColorMap().grey100),
        ("grey0", "grey100"),
    ],
)
def test__Gradient__parse(start: Any, stop: Any):
    gradient = printbuddies.Gradient([start, stop])
    text = "01234567890"
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


def test__Gradient_more_colors_than_text():
    colors = printbuddies.ColorMap()
    text = "Just some sample text to do a lil testing on."
    gradient = printbuddies.Gradient(
        [random.choice(colors) for _ in range(len(text) + 10)]
    )
    gradient.apply(text)
