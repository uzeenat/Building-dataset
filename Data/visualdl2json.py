import json
import os

from visualdl import LogReader

folder_json = r'C:\Users\YuanXin\Desktop\log\json'
folder_visualdl = r'C:\Users\YuanXin\Desktop\log\visualdl'
for filename in os.listdir(folder_visualdl):
    if not filename.endswith('.log'):
        continue
    filepath_visualdl = os.path.join(folder_visualdl, filename)

    reader = LogReader(
        file_path=filepath_visualdl,
    )
    tags = reader.tags()
    values = dict()
    for tag_name, tag_type in tags.items():
        assert isinstance(tag_name, str)
        assert isinstance(tag_type, str)
        if tag_type != 'scalar':
            continue
        tag_name = tag_name.replace(filepath_visualdl, '')[1:]
        data = reader.get_data(tag_type, tag_name)
        values[tag_name] = [v.value for v in data]

    filepath_json = os.path.join(folder_json, f'{filename}.json')
    os.makedirs(os.path.dirname(filepath_json), exist_ok=True)
    with open(filepath_json, 'w+') as file:
        json.dump(values, file)
