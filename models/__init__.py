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
        self.variables = variables
        self.errors = None
        try:
            self.__ActionModel = ActionModel(**self.variables)
        except ValidationError as e:
            self.errors = e.json()


    def as_json(self):
        if self.errors:
            return None, False, self.errors
        else:
            return json.dumps(self.__ActionModel.dict()), True, None


    def as_dict(self):
        if self.errors:
            return None, False, self.errors
        else:
            return self.__ActionModel.dict(), True, None
