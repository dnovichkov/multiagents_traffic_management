from collections import defaultdict
import typing
import logging
import pathlib
import datetime

from src.agents.messages import MessageType


class Scene:
    """
    Scene class for storing virtual world entities
    """
    def __init__(self):
        self.entities = defaultdict(list)
        self.current_time = 0
        self.activity_messages = []

    def get_entities_by_type(self, entity_type) -> typing.List:
        """
        Returns entities of the given type that are not in the process of being deleted
        :param entity_type:
        :return:
        """
        all_entities = self.entities.get(entity_type, [])
        not_deleting_entities = [entity for entity in all_entities if not entity.is_deleting]
        return not_deleting_entities

    def add_msg(self, msg):
        self.activity_messages.append(msg)

    def create_activity_log(self):
        # This method should be moved to other file
        res_strings = []
        for msg in self.activity_messages:
            if len(msg) < 3:
                logging.warning("Possible_error with msg %s", msg)
                continue
            _type = msg[2]
            if _type is MessageType.INIT_MESSAGE:
                continue

            sender_name = msg[0]
            rec_name = msg[1]
            data = msg[3]  # pylint: disable=unused-variable
            sender_name = sender_name.replace('\"', '\'').replace(' ', "\\r")
            rec_name = rec_name.replace('"', '\'').replace(' ', "\\r")
            data_string = ''
            if isinstance(data, dict):
                for key, value in data.items():
                    data_string += f'{key}: {value}, \\n'
            res_string = '"' + sender_name + '\"\t' + ' -> ' + '\t"' + rec_name + '"' + ': \t' + str(_type.name)
            if data_string:
                res_string+='\\n ' + data_string
            res_strings.append(res_string)
        activity_filename = "activity" + "_" + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f") + ".txt"

        path = pathlib.Path("activities/")
        file_path = path / activity_filename
        path.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding='utf-8') as file:

            print('@startuml', file=file, sep="\n")
            print(*res_strings, file=file, sep="\n")
            print('@enduml', file=file, sep="\n")
