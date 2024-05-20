"""
Car description
"""
import logging
import typing
from dataclasses import dataclass

from src.entities.base_entity import BaseEntity


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
