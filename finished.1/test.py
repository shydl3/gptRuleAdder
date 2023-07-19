import sys
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import yaml
import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
root = Tk()
root.withdraw()
# print(os.getcwd())
print("请选择配置文件:\n")
time.sleep(1)
file_path = askopenfilename(initialdir=os.getcwd())
# print(file_path)

# sys.exit(1)



if file_path:
    # file_path = "./test.yml"
    print(f"正在读取配置文件{file_path}...")
    with open(file_path, "r", encoding='utf-8', errors='ignore') as raw_config:
        raw_text: dict = yaml.safe_load(raw_config)
        proxy_groups: list = raw_text['proxy-groups']  # a list including dict data
        rules: list = raw_text['rules']
        proxies: list = raw_text['proxies']
        print(f"正在获取节点信息...")
        gpt_proxies: list = []
        proxy_keywords: list = ['日本', '韩国', '新加坡', '美国', '法国', '俄罗斯', '英国', '台湾']
        for node in proxies:
            node_name = node['name']
            for keyword in proxy_keywords:
                if keyword in node_name:
                    gpt_proxies.append(node_name)
        print("正在生成Openai规则...")
        gpt_proxy_dict: dict = {'name': '🖤 ChatGPT', 'type': 'select', 'proxies': []}
        gpt_proxy_dict['proxies'] = gpt_proxies
        proxy_groups.insert(0, gpt_proxy_dict)
        new_proxy_groups: list = proxy_groups

        gpt_rule = 'DOMAIN-SUFFIX,openai.com,🖤 ChatGPT'
        rules.insert(0, gpt_rule)
        new_rules: list = rules

        raw_text['proxy-groups'] = new_proxy_groups
        raw_text['rules'] = rules

        text = str(raw_text)

        new_yml_path = './Openai-rule-added.yml'
        with open(new_yml_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"新的配置文件已生成！\n{new_yml_path}")
        print("按回车键退出...")
        input()
        sys.exit()




