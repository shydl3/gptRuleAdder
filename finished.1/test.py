import yaml
import sys

# sys.stdout.encoding = 'gbk'
file_path = "./test.yml"
with open(file_path, "r", encoding='utf-8', errors='ignore') as raw_config:
    raw_text: dict = yaml.safe_load(raw_config)
    # print(type(raw_text))
    # for line in raw_text:
    #     print(line)
    # print(raw_config)
    proxy_groups: list = raw_text['proxy-groups']  # a list including dict data
    rules: list = raw_text['rules']
    proxies: list = raw_text['proxies']
    # print(rules)
    # for i in proxy_groups:
    #     print(f"{i}\n")

    gpt_proxies: list = []
    proxy_keywords: list = ['日本', '韩国', '新加坡', '美国', '法国', '俄罗斯', '英国', '台湾']
    for node in proxies:
        node_name = node['name']
        for keyword in proxy_keywords:
            if keyword in node_name:
                # print(node_name)
                gpt_proxies.append(node_name)
    # for each in gpt_proxies:
    #     print(each)
    # print(gpt_proxies)
    # GPT nodes (in list form) have been filtered by here

    test_proxies: dict = {'name': '🖤 ChatGPT', 'type': 'select', 'proxies': []}


    # new_proxy_groups = proxy_groups.insert(0, gpt_proxies)
    test_proxies['proxies'] = gpt_proxies
    # print(test_proxies)

    proxy_groups.insert(0, test_proxies)
    # print(proxy_groups)
    # for i in new_proxy_groups:
    #     print(f"{i}\n")
    # proxy_groups have been rewritten
    new_proxy_groups: list = proxy_groups





    gpt_rule = 'DOMAIN-SUFFIX,openai.com,🖤 ChatGPT'
    rules.insert(0, gpt_rule)
    # print(rules)
    # rules have been rewritten
    new_rules: list = rules


    raw_text['proxy-groups'] = new_proxy_groups
    raw_text['rules'] = rules

    text = str(raw_text)

    new_config = yaml.dump(raw_text)
    # print(new_config)
    new_yml_path = './GPT-rule.yml'
    with open(new_yml_path, 'w') as file:
        file.write(text)


    # save_path = './save.txt'
    # with open(save_path, 'w') as file:
    #     file.write(proxies)





