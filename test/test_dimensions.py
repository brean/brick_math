from brick_math.brick import DEFAULT_BRICK_1x1x3


def test_mm_conversions():
    assert DEFAULT_BRICK_1x1x3.to_mm() == [8.0, 3.2, 8.0]
