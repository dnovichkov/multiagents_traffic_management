"""
Traffic light description
"""
import logging
import typing
from dataclasses import dataclass

from src.entities.base_entity import BaseEntity
from src.utils.point import Point


class TrafficLightEntity(BaseEntity):
    """
    Traffic Light entity
    """
    def __init__(self, init_dict_data, scene=None):
        super().__init__(scene)
        self.name = init_dict_data.get('Name')
        self.number = init_dict_data.get('Id')
        x1 = float(init_dict_data.get('x-coord'))
        y1 = float(init_dict_data.get('y-coord'))
        self.location = Point(x1, y1)
        self.radius = init_dict_data.get('Radius')

        self.uri = 'TrafficLight' + str(self.number)

    def __repr__(self):
        return 'TrafficLight ' + str(self.name)

    @staticmethod
    def get_type():
        """
        """
        return 'TRAFFIC_LIGHT'

    def get_schedule_json(self):
        """
        Schedule serialization
        :return:
        """
        result = []
        return result

    def get_possible_point(self, possible_next_point: Point) -> Point:
        """
        Check if the car can move to the given location
        :param possible_next_point:
        :return:
        """

        # TODO: view all cars in current area and check the restrictions.
        return possible_next_point
