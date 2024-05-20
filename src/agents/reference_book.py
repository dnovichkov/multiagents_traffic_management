"""Contains agent address book"""
import logging


class ReferenceBook:
    """Agent address book linked to entities"""
    def __init__(self):
        self.agents_entities = {}

    def add_agent(self, entity, agent_address):
        """
        Saves the agent's address with a binding from an entity
        :param entity:
        :param agent_address:
        :return:
        """
        self.agents_entities[entity] = agent_address

    def get_address(self, entity):
        """
        Returns the agent address of the specified entity.
        :param entity:
        :return:
        """
        if entity not in self.agents_entities:
            logging.error(f'Agent {entity} is missing from the address book')
            return None
        return self.agents_entities[entity]

    def clear(self):
        """
        Clears the address book
        :return:
        """
        self.agents_entities.clear()

    def get_entity_name(self, agent_address):
        """
        Returns the name of the specified agent address.
        :param agent_address:
        :return:
        """
        if agent_address.addressDetails == 'System:ExternalRequester':
            return "Scene"
        for entity, agent in self.agents_entities.items():
            if agent_address == agent:
                return entity.name
        return str(agent_address)
