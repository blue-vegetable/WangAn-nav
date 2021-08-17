import json


def add_website(dic, type, id, name, url):
    for kind in dic['kinds']:
        if kind['id'] == id:
            kind['sites'].append({'name': name, 'Url': url})
            break
    else:
        dic['kinds'].append(
            {'type': type, 'id': id, 'sites': [{'name': name, 'Url': url}]})


with open("./config/config_websites.json", "r") as f:
    dic = json.load(f)
    add_website(dic, '武大2', 'WHU2', '瞎写的', 'www.baidu.com')
    print(dic)
