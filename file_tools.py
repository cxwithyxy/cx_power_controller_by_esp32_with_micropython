import ujson
def read_file_string(filepath):
    code = ""
    with open(filepath, 'r') as file :
        code = file.read()
    return code

def read_json(filepath):
    json_string = read_file_string(filepath)
    return ujson.loads(json_string)