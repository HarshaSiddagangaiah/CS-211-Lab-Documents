"""Closed intervals of integers
Harsha, 2023-01-10, CS 211
"""


class Interval:
    """An interval m..n represents the set of intervals at least m and at most n."""

    def __init__(self, low: int, high: int):
        """Interval(low,high) is the interval low..high"""
        """assert low > high, "low must not exceed high"""
        if low > high:
            raise ValueError("low must not exceed high")
        self.low = low
        self.high = high

    def contains(self, i: int) -> bool:
        """Integer i is within the closed interval"""
        return i >= self.low and i <= self.high

    def overlaps(self, other: "Interval") -> bool:
        """i.overlaps(j) iff i and j have some elements in common"""
        if self.low > other.high:
            return False
        if self.high < other.low:
            return False
        return True

    def __eq__(self, other: "Interval") -> bool:
        """Intervals are equal if they have the same low and high bounds"""
        return self.low == other.low and self.high == other.high

    def join(self, other: "Interval") -> "Interval":
        """Create a new Interval that contains the union of elements in self and other.
        Precondition: self and other must overlap.
        """
        assert (self.overlaps(other))
        return Interval(min(self.low, other.low), max(self.high, other.high))







