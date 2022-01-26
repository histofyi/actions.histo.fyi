from flask import Flask
import toml
import logging

from datetime import datetime
import random

from providers import innodbProvider


from models import Action, ActionModel

app = Flask(__name__)
app.config.from_file('config.toml', toml.load)


aws_region = app.config['AWS_REGION']
innodb_table = app.config['TABLE_NAME']



@app.route('/')
def hello_world():
    timestring = datetime.now().strftime('%Y%m%d%H%M%S')
    randomstring = str(random.randint(0, 9))
    key = timestring + randomstring
    variables = {
        'identifier' : key,
        'actionStatus' : 'str',  
        'agent' : 'str',
        'startTime' : 'str',
        'endTime' : 'str',
        'error' : [],
        'instrument' : 'str',
        'object' : {},
        'participant' : 'str',
        'result' : {},
        'target' : 'str',
        'description' : 'str',
        'potentialAction' : 'str',
        'subjectOf' : 'str',
        'url' : 'str',
        'version': '0.1'
    }
    action = Action(variables)
    if not action.has_errors():
        payload, success, errors = innodbProvider(aws_region).put(innodb_table, action.as_dict())
    return {
        'action': action.as_dict(),
        'success': success,
        'errors': errors, 
        'schema':action.as_schema()
    }