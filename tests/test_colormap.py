import random

import printbuddies


def test__Tag():
    toggle = printbuddies.Tag("pink1")
    assert f"{toggle}" == "[pink1]"
    assert toggle.o == "[/pink1]"


def test__ColorMap():
    c = printbuddies.ColorMap()
    assert f"{c.p1}" == "[pink1]"
    assert c.p1.o == "[/pink1]"
    assert c.p1.off == "[/pink1]"
    assert len(c)
    assert list(c)
    assert len(c) == len(list(c))
    assert isinstance(c[0], printbuddies.Tag)
    assert isinstance(random.choice(c), printbuddies.Tag)
