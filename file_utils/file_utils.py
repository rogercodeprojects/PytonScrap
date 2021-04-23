import json

def write_json_file(json_file_name, data):
    file = open(json_file_name,'w')
    json.dump(data, file)
    file.close()

def write_utf8_json_file(json_file_name, data):
    file = open(json_file_name,'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii= False)
    file.close()

def append_to_json_file(json_file_name, data):
    file = open(json_file_name,'a')
    json.dump(data, file)
    file.close()

def append_to_utf8_json_file(json_file_name, data):
    file = open(json_file_name,'a', encoding='utf-8')
    json.dump(data, file, ensure_ascii= False)
    file.close()

def read_json_file(json_file_name):
    file = open(json_file_name)
    data = json.load(file)
    file.close()
    return data
def read_utf8_json_file(json_file_name):
    file = open(json_file_name, encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

