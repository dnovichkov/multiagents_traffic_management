from functools import lru_cache


class BaseEntity:
    """Base entity"""

    def __init__(self, scene=None):
        self.uri = 'UNKNOWN_URI'
        self.scene = scene
        self.name = "Base Entity Name"
        # Flag that indicates if the entity is being deleted
        self.is_deleting = False

    def __repr__(self):
        return 'Entity ' + str(self.name)
