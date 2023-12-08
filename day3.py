from __future__ import annotations

import re

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int



def neighbors4(p: Point) -> list[Point]:
    return [
        Point(p.x, p.y + 1),
        Point(p.x, p.y - 1),
        Point(p.x + 1, p.y),
        Point(p.x - 1, p.y),
        ]

def diagnoals(p: Point) -> list[Point]:
    return [
        Point(p.x + 1, p.y + 1),
        Point(p.x - 1, p.y + 1),
        Point(p.x + 1, p.y - 1),
        Point(p.x - 1, p.y - 1),
        ]

def neighbors8(p: Point) -> list[Point]:
    return neighbors4(p) + diagnoals(p)

symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']

class Grid(dict):
    def __init__(self, lines):
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self[Point(x, y)] = char
    
    def neighbor_vals(self, point: Point) -> list[str]:
        neighbors = neighbors8(point)
        return [self.get(p, None) for p in neighbors]
        



class Number:
    def __init__(self, match: re.Match, row: int) -> None:
        self.match = match
        self.row = row
    
    def points(self) -> list[Point]:
        points: list[Point] = []
        for col in range(*self.match.span()):
            points.append(Point(col, self.row))
        return points

    def adjacent_points(self) -> list[Point]:
        adj_points: list[Point] = []
        for own_point in self.points():
            adj_points.extend(neighbors8(own_point))
        return adj_points

    def adjacent_vals(self) -> list[str]:
        vals = []
        for adj_point in self.adjacent_points():
            if val := grid.get(adj_point):
                vals.append(val)
        return vals


    @property
    def valid(self) -> bool:
        for val in self.adjacent_vals():
            if val in symbols:
                print(f"Match {self.val} at {self.points()} touching {val}")
                return True
        print(f"NO match {self.val} at {self.points()}")
        return False

    @property
    def val(self) -> int:
        return int(self.match.group())



with open("input3.txt") as f:
    lines = f.readlines()

ans = 0

grid = Grid(lines)

for y, line in enumerate(lines):
    nums = [Number(m, y) for m in re.finditer(r"\d+", line)]
    for num in nums:
        if num.valid:
            ans += num.val

            









