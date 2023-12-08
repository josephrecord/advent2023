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


def left(point: Point) -> Point:
    return Point(point.x - 1, point.y)

def right(point: Point) -> Point:
    return Point(point.x + 1, point.y)

symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']

class Grid(dict):
    def __init__(self, lines):
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self[Point(x, y)] = char
    
    def neighbor_vals(self, point: Point) -> list[str]:
        vals: list[str] = []
        for p in neighbors8(point):
            if val := self.get(p):
                vals.append(val)
        return vals
    
    def number_span(self, point) -> tuple[Point, Point]:
        if not self.get(point).isdecimal():
            raise ValueError(f"Point must be decimal, not {self.get(point)}")
        
        entry_point = point

        # Find the start
        while self.get(point).isdecimal():
            point = left(point) # move left
        start = right(point)
        
        # Find the end
        point = entry_point
        while self.get(point).isdecimal():
            point = right(point) # move right
        end = left(point)

        return start, end


    def touching_2_numbers(self, point: Point) -> bool:
        spans = set()
        for p in neighbors8(point):
            if val := self.get(p):
                if val.isdecimal():
                    spans.add(self.number_span(p))
        if len(spans) == 2:
            return True
        return False





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

for point in grid.keys():
    if grid.get(point) == '*':
        print(neighbors8(point))
        if grid.touching_2_numbers(point):
            print("hi")
        
        

            









