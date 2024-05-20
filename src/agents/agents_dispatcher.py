"""Contains the Agent Manager class"""
import logging
import typing
import uuid

from thespian.actors import ActorSystem, ActorExitRequest

from .car_agent import CarAgent
from .traffic_light_agent import TrafficLightAgent
from .messages import MessageType, Message
from .reference_book import ReferenceBook
from src.entities.base_entity import BaseEntity


TYPES_AGENTS = {
    'CAR': CarAgent,
    'TRAFFIC_LIGHT': TrafficLightAgent,
}


class AgentsDispatcher:
    """
    Agent Manager Class
    """
    def __init__(self, scene):
        self.actor_system = ActorSystem()
        self.reference_book = ReferenceBook()
        self.scene = scene

    def add_entity(self, entity: BaseEntity):
        """
        Adds an entity to the scene, creates an agent and sends an initialization message to it
        :param entity:
        :return:
        """
        entity_type = entity.get_type()
        agent_type = TYPES_AGENTS.get(entity_type)
        if not agent_type:
            logging.warning(f'For entity type {entity_type} agent is not specified')
            return False
        self.scene.entities[entity_type].append(entity)
        self.create_agent(agent_type, entity)
        return True

    def create_agent(self, agent_class, entity):
        """
        Creates an agent of a given class with binding to an entity
        :param agent_class:
        :param entity:
        :return:
        """
        agent = self.actor_system.createActor(agent_class)
        self.reference_book.add_agent(entity=entity, agent_address=agent)
        init_data = {'dispatcher': self, 'scene': self.scene, 'entity': entity}
        init_message = Message(MessageType.INIT_MESSAGE, init_data)
        self.actor_system.tell(agent, init_message)

    def remove_entity(self, entity_type: str, entity_name: str) -> bool:
        """
        Removes an entity by type and name
        :param entity_type:
        :param entity_name:
        :return:
        """
        entities: typing.List[BaseEntity] = self.scene.get_entities_by_type(entity_type)
        for entity in entities:
            if entity.name == entity_name:
                agent_address = self.reference_book.get_address(entity)
                if not agent_address:
                    logging.error(f'{entity} agent not found')
                    return False
                self.actor_system.tell(agent_address, ActorExitRequest())
                self.scene.entities[entity_type].remove(entity)
                return True
        return False

    def remove_agent(self, agent_id=None) -> bool:
        agent_address = self.reference_book.get_address(agent_id)
        if not agent_address:
            logging.error(f'Agent with identifier {agent_id} not found')
            return False
        self.actor_system.tell(agent_address, ActorExitRequest())
        return True

    def get_agents_id(self) -> typing.List:
        """
        Returns agent IDs
        :return:
        """
        result = list(self.reference_book.agents_entities.keys())
        return result

    def get_agents_addresses(self) -> typing.List:
        """
        Returns a list of agent addresses
        :return:
        """
        result = list(self.reference_book.agents_entities.values())
        return result
