import json
import jsonschema
from jsonschema import validate

def get_schema(name):
    """Load schema and return"""
    with open(name, 'r') as file:
        schema = json.load(file)
    return schema

def get_json(name):
    """Load and return json"""
    with open(name, 'r') as file:
        data = json.load(file)
    return data

def validate_json(json_data,name):
    execute_api_schema = get_schema(name)

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    valid_message = "Given JSON data is Valid"
    return True, valid_message


# Convert json to python object.
# Valid
# jsonData = json.loads('{"id" : 10,"name": "DonOfDen","contact_number":1234567890}')
# InValid
get_json_name='1.json'
get_json_schema='1.schema'
# print(f'{get_json(get_json_name)}')
# jsonData = json.loads(get_json(get_json_name))
jsonData = get_json(get_json_name)
# jsonData = json.loads('{"event": "label_selected", "data": {"id": null, "rr_id": null, "labels": [{"slug": "flu", "type": 2, "color": {"color": "#e83e35", "label": "stress"}, "name_en": "cold/flu", "name_ru": "\u043f\u0440\u043e\u0441\u0442\u0443\u0434\u0430/\u0433\u0440\u0438\u043f\u043f", "category": "health-body", "type_stress": 2, "is_custom_tag": false, "property_where": null, "property_arousal": null, "property_pleasure": null, "property_vitality": null, "property_stability": null}], "timestamp": "2020-09-09T14:07:44"}, "created_at": "2020-09-09T11:07:45.080214Z", "environment_id": 2}')
# jsonData = json.loads(str(get_json(get_json_name)))
# validate it
is_valid, msg = validate_json(jsonData,get_json_schema)
print(msg)