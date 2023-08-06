from __future__ import annotations
from typing import List

import pandas as pd


class IntervalFrame:
    def __init__(self, intervals: List[Interval]):
        """Class to hold and preprocess intervals.

        Assumes values are sorted by "start" THEN "end".

        Args:
            intervals: A list of Interval objects.

        Attributes:
            intervals (List[Interval]): A list of Interval objects.
            _result (List[Interval]): A list to hold the intervals after processing.
        """
        self.intervals = intervals
        self._result: List[Interval] = []

    def preprocess(self) -> None:
        """" Preprocesses the intervals.

        Takes all unique start and end points from the intervals, and forms new intervals.
        Checks for overlap between new intervals and original intervals.
        If overlap occurs, frequency of new interval is increased by the frequency of original interval.
        """
        points = set()

        for interval in self.intervals:
            points.add(interval.start)
            points.add(interval.end)

        sorted_points = sorted(list(points))

        for start, end in zip(sorted_points, sorted_points[1:]):

            new_interval = Interval(start=start, end=end, freq=0)  # initialise a new interval with 0 frequency

            for interval in self.intervals:

                if Interval.overlap(new_interval, interval):
                    new_interval.freq += interval.freq

            if new_interval.freq <= 0:
                continue

            self._result.append(new_interval)

    def to_dataframe(self) -> pd.DataFrame:
        """ Converts the processed intervals to a Pandas DataFrame.

        Raises:
            ValueError: If the preprocess method has not been run first.

        Returns:
            pd.DataFrame: A DataFrame where each row is an interval and columns are "start", "end", and "frequency".
        """
        if not self._result:
            raise ValueError("Please run `preprocess()` first")

        return pd.DataFrame([interval.to_list() for interval in self._result], columns=["start", "end", "frequency"])


class Interval:
    def __init__(self, start: int, end: int, freq: int):
        self.start = start
        self.end = end
        self.freq = freq

    def to_list(self) -> List[int]:
        return [self.start, self.end, self.freq]

    @staticmethod
    def overlap(interval_1: Interval, interval_2: Interval) -> bool:
        """ Checks if two intervals overlap.

        Args:
            interval_1: The first interval.
            interval_2: The second interval.

        Returns:
            bool: True if intervals overlap, otherwise False.
        """
        return interval_1.start < interval_2.end and interval_2.start < interval_1.end


if __name__ == "__main__":
    data = pd.DataFrame(
        {"start": [0, 5, 8, 1, 22, 100], "end": [10, 15, 20, 60, 40, 200], "freq": [1, 2, 3, 2, 5, 1]}
    )

    data.sort_values(by=["start", "end"], inplace=True)

    frame = IntervalFrame(
        [
            Interval(
                start=row[1]["start"],
                end=row[1]["end"],
                freq=row[1]["freq"]
            ) for row in data.iterrows()
        ]
    )

    frame.preprocess()

    df = frame.to_dataframe()
    print(df)