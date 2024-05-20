"""
Car description
"""
import logging
import typing
from dataclasses import dataclass

from src.entities.base_entity import BaseEntity
from src.utils.point import Point


@dataclass
class ScheduleItem:
    """
    Schedule record item
    """
    rec_type: str
    start_time: int
    end_time: int
    cost: float
    all_params: dict


class CarEntity(BaseEntity):
    """
    Car entity
    """
    def __init__(self, init_dict_data, scene=None):
        super().__init__(scene)
        self.name = init_dict_data.get('Name')

        self.number = init_dict_data.get('Id')
        self.uri = 'Car' + str(self.number)

        self.schedule: typing.List[ScheduleItem] = []
        direction = init_dict_data.get('Direction')
        self.next_point = direction.split('->')[-1]
        self.from_direction = direction.split('->')[0]
        self.distance = init_dict_data.get('DistanceToPoint')
        self.appear_time = init_dict_data.get('AppearTime')
        self.length = init_dict_data.get('CarLength')
        self.speed = init_dict_data.get('Speed')
        x1 = float(init_dict_data.get('x-coord'))
        y1 = float(init_dict_data.get('y-coord'))
        self.init_point = Point(x1, y1)

    def __repr__(self):
        return 'Car ' + str(self.name)

    @staticmethod
    def get_type():
        """
        """
        return 'CAR'

    def get_schedule_json(self):
        """
        Schedule serialization
        :return:
        """
        result = []
        return result
