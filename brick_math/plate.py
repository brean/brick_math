from .part import Part


DEFAULT_PLATE_32x32 = Part(
    width=32*20, depth=32*20, connectors=[
        [x, 1, z] for x in range(32) for z in range(32)
    ])
