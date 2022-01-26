from typing import List, Dict, Optional
from pydantic import BaseModel
from pydantic import ValidationError

import json
import logging


class ActionModel(BaseModel):
    identifier : str
    actionStatus : str  
    agent : str
    startTime : str
    endTime : str
    error : List[str]
    instrument : str
    object : Dict[str, int]
    participant : str
    result : Dict[str, int]
    target : str
    description : str
    potentialAction : str
    subjectOf : str
    url : str
    version : str

    



class Action():

    __ActionModel = None

    def __init__(self, variables):
        self.__variables = variables
        self.__errors = None
        try:
            self.__ActionModel = ActionModel(**variables)
        except ValidationError as e:
            self.__errors = e.json()

    def has_errors(self):
        if self.__errors:
            return self.__errors
        else:
            return False


    def as_json(self):
        if self.__errors:
            return None
        else:
            return json.dumps(self.__ActionModel.dict())


    def as_dict(self):
        if self.__errors:
            return None
        else:
            return self.__ActionModel.dict()


    def as_schema(self):
        return ActionModel.schema()