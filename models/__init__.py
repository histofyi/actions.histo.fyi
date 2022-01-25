from typing import List, Dict, Optional
from pydantic import BaseModel

import json
import logging


class Action(BaseModel):
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

    def as_json(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return self.dict()



