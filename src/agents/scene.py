from collections import defaultdict
import typing


class Scene:
    """
    Scene class for storing virtual world entities
    """
    def __init__(self):
        self.entities = defaultdict(list)

    def get_entities_by_type(self, entity_type) -> typing.List:
        """
        Returns entities of the given type that are not in the process of being deleted
        :param entity_type:
        :return:
        """
        all_entities = self.entities.get(entity_type, [])
        not_deleting_entities = [entity for entity in all_entities if not entity.is_deleting]
        return not_deleting_entities
