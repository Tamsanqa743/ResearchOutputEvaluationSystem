import json
from jsonschema import validate, ValidationError
class validator:

    def __init__(self):
        pass

    def validate_format(self, data):
        '''Verify jason'''
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False

    def validate_schema(self, data):
        schema = {
            "type": "object",
            "properties": {
                'research_title':'string',
                'author': 'string',
                'field_of_study': 'string',
                'research_output': 'string'
            },
            "required": ["research_title", "author", "field_of_study", "research_output"]
        }

        '''perfrom validation'''
        try:
            if validate(instance=data, schema=schema): return True
        except ValidationError as e:
            print(e)
            return False