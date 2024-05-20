"""
Traffic light description
"""
import logging
import typing
from dataclasses import dataclass

from src.entities.base_entity import BaseEntity


class TrafficLightEntity(BaseEntity):
    """
    Traffic Light entity
    """
    def __init__(self, init_dict_data, scene=None):
        super().__init__(scene)
        self.name = init_dict_data.get('Name')
        self.number = init_dict_data.get('Id')

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
