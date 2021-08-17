import json


def add_website(dic, type, id, sites):
    for kind in dic['kinds']:
        if kind['id'] == id:
            for site in sites:
                kind['sites'].append(site)
            break
    else:
        dic['kinds'].append(
            {'type': type, 'id': id, 'sites': sites})


def process_name_url(names, urls):
    sites = []
    for i in range(len(names)):
        sites.append({'name': names[i], 'Url': urls[i]})
    return sites


# type = "武大"
# id = "WHU"
# names = ['信息门户', '老教务系统', '新教务系统', '珞珈在线', '武大图书馆']
# urls = ['https://ehall.whu.edu.cn/new/index.html', 'http://bkjw.whu.edu.cn/',
#         'https://bkxk.whu.edu.cn/xtgl/login_slogin.html?language=zh_CN',
#         'http://www.mooc.whu.edu.cn/portal', 'https://www.lib.whu.edu.cn/']

# type = "邮箱"
# id = "e-mails"
# names = ['武大邮箱', '微软邮箱', '网易邮箱', '谷歌邮箱', 'QQ邮箱']
# urls = ['https://email.whu.edu.cn/', 'https://outlook.live.com/mail',
#         'https://mail.163.com/',
#         'https://www.google.com/gmail/', 'https://mail.qq.com/']

type = "学习"
id = "study"
names = ['GITHUB', 'LEETCODE', 'bilibili', '中国大学mooc', 'coursera']
urls = ['https://github.com/', 'https://leetcode-cn.com/problemset/all/',
        'https://www.bilibili.com/',
        'https://www.icourse163.org/', 'https://www.coursera.org/']

with open("./config/config_websites.json", "r", encoding='utf-8') as f:
    dic = json.load(f)
    add_website(dic, type, id, process_name_url(names, urls))
with open("./config/config_websites.json", "wt+", encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=4)
