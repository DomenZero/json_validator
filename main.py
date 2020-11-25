import os # for read files
import json
import jsonschema
from jsonschema import validate

# read all files in a folder
def read_all_files(files_folder):
    i=int(0)
    for dirpath, dirs, files in os.walk(files_folder):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            with open(fname) as myfile:
                i += 1
                print(myfile.read())
                print(f'_______{filename}__\n')
        print(f'How many files in the {files_folder} directory?: {i}')


# Load a schema and return its
def get_schema(name):

    with open(name, 'r') as file:
        schema = json.load(file)
    return schema

# Load a json script and return its
def get_json(name):
    with open(name, 'r') as file:
        data = json.load(file)
    return data

# Good or Bad JSON
def validate_json(json_data,name):
    execute_api_schema = get_schema(name)

    try:
        validate(instance=json_data, schema=execute_api_schema)
        # validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Attention: JSON data is BAD"
        return False, err

    valid_message = "Attention: JSON data is correct"
    return True, valid_message

# Good or Bad JSON
def validate_json_2(json_data,execute_api_schema):
    # execute_api_schema = get_schema(name)

    try:
        validate(instance=json_data, schema=execute_api_schema)
        # validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Attention: JSON data is BAD"
        return False, err

    valid_message = "Attention: JSON data is correct"
    return True, valid_message
# Compare a JSON script with a JSON schema
def compare_json_script_schema(get_json_name,get_json_schema):
    jsonData = get_json(get_json_name)
    is_valid, msg = validate_json(jsonData, get_json_schema)
    print(msg)
#
def compare_json_script_schema_2(get_json_script,get_json_schema):
    is_valid, msg = validate_json_2(get_json_script, get_json_schema)
    print(msg)

def read_all_folders(files_script_folder,files_schema_folder):
    i = int(0)
    for dirpath, dirs, files in os.walk(files_script_folder):
        for filename_script in files:
            fname_script = os.path.join(dirpath, filename_script)
            with open(fname_script) as script_file:
                # i += 1
                # print(script_file.read())
                data = json.load(script_file)
                for dirpath1, dirs1, files1 in os.walk(files_schema_folder):
                    for filename_schema in files1:
                        fname_schema = os.path.join(dirpath1, filename_schema)
                        with open(fname_schema) as schema_file:
                            i += 1
                            # print(schema_file.read())
                            schema = json.load(schema_file)
                            is_valid, msg = validate_json_2(data, schema)
                            print(f'___{fname_script}____{fname_schema}__\n')
        print(f'How many files in the directories?: {i}')

# Convert json to python object.
# Valid
# jsonData = json.loads('{"id" : 10,"name": "DonOfDen","contact_number":1234567890}')
# Define test
get_json_script_folder='./event/'
get_json_schema_folder='./schema/'
# read_all_files(get_json_script_folder)
get_json_name='1.json'
get_json_schema='1.schema'
# Test 1 file
# jsonData = get_json(get_json_name)
# jsonSchema = get_schema(get_json_schema)
# is_valid, msg = validate_json_2(jsonData,jsonSchema)


# end define test
# compare_json_script_schema(get_json_name,get_json_schema)
# print(read_all_folders(get_json_script_folder))

read_all_folders(get_json_script_folder,get_json_schema_folder)

# print(f'{get_json(get_json_name)}')
# jsonData = json.loads(get_json(get_json_name))
# read_all_files(get_json_script_folder)
# read_all_files(get_json_schema_folder)


# jsonData = get_json(get_json_name)
# jsonData = json.loads('{"event": "label_selected", "data": {"id": null, "rr_id": null, "labels": [{"slug": "flu", "type": 2, "color": {"color": "#e83e35", "label": "stress"}, "name_en": "cold/flu", "name_ru": "\u043f\u0440\u043e\u0441\u0442\u0443\u0434\u0430/\u0433\u0440\u0438\u043f\u043f", "category": "health-body", "type_stress": 2, "is_custom_tag": false, "property_where": null, "property_arousal": null, "property_pleasure": null, "property_vitality": null, "property_stability": null}], "timestamp": "2020-09-09T14:07:44"}, "created_at": "2020-09-09T11:07:45.080214Z", "environment_id": 2}')
# jsonData = json.loads(str(get_json(get_json_name)))
# validate it
# is_valid, msg = validate_json(jsonData,get_json_schema)
# print(msg)