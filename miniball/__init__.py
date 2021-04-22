__author__ = "Konstantin Weddige"
from typing import cast, Iterable, List

import miniball.bindings  # type: ignore


class Miniball:
    def __init__(self, points: Iterable[Iterable[float]]):
        """Computes the smallest enclosing ball of the points.

        :param points: coordinates as nested lists.
        """
        self._result = miniball.bindings.miniball(points)

    def center(self) -> List[float]:
        """Returns a list that holds the coordinates of the center of the computed ball."""
        return cast(List[float], self._result[0])

    def squared_radius(self) -> float:
        """Returns the squared radius of the computed ball."""
        return cast(float, self._result[1])

    def relative_error(self) -> float:
        """Returns the maximum excess of any input point w.r.t. the computed
        ball, divided by the squared radius of the computed ball. The
        excess of a point is the difference between its squared distance
        from the center and the squared radius; Ideally, the return value
        is 0.
        """
        return cast(float, self._result[2])

    def suboptimatily(self) -> float:
        """Returns the absolute value of the most negative
        coefficient in the affine combination of the support points that
        yields the center. Ideally, this is a convex combination, and there
        is no negative coefficient in which case 0 is returned.
        """
        return cast(float, self._result[3])

    def is_valid(self) -> bool:
        """Returns true if the relative error is at most tol, and the
        suboptimality is 0; the default tolerance is 10 times the
        coordinate type's machine epsilon
        """
        return cast(bool, self._result[4])

    def get_time(self) -> float:
        """Returns the time in seconds taken by the constructor call for
        computing the smallest enclosing ball."""
        return cast(float, self._result[5])
