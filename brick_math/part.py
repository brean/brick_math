"""A basic part, base class for all bricks/plates/...
See https://www.ldraw.org/article/218.html for details"""
from dataclasses import dataclass


LDU_MM = 0.4


@dataclass
class Part:
    width: float = 20
    height: float = 1
    depth: float = 20
    stud_diameter: float = 12
    stud_height: float = 4
    x: float = 0
    y: float = 0
    z: float = 0

    # we have one connector at the center of the stud
    connectors: list = [
        [10, 1, 10]
    ]

    def to_mm(self):
        return [
            self.width * LDU_MM,
            self.height * LDU_MM,
            self.depth * LDU_MM
        ]
