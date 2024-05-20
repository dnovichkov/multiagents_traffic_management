""" Contains an implementation of a point on a plane"""
import math


class Point:
    """
    Class of a point on a plane
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + '; ' + str(self.y) + ')'

    def get_distance_to_other(self, other_point):
        """
        Returns the distance to another point
        :param other_point:
        :return:
        """
        order_distance = math.dist((self.x, self.y), (other_point.x, other_point.y))
        return order_distance


def is_point_between(point_start, point_end, point_between) -> bool:
    """
    Checks if a point is between two other points
    :param point_start:
    :param point_end:
    :param point_between:
    :return:
    """
    if point_start.get_distance_to_other(point_end) <= point_between.get_distance_to_other(point_end):
        return True
    return False
