import requests
import parsel
import json
import requests

cookies = {
    '_gscu_1440800408': '16212967zq1xfr19',
    '_gscbrs_1440800408': '1',
    'JSESSIONID': 'E90CA4C9779934CB5CF84C446E3702D6',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gscu_1440800408=16212967zq1xfr19; _gscbrs_1440800408=1; _gscs_1440800408=162129670vhogq19|pv:1; JSESSIONID=204B6E7FBBC744E933789508D041A720',
    'Origin': 'https://homepage.zjut.edu.cn',
    'Referer': 'https://homepage.zjut.edu.cn/jsflcx2/list.htm?keyword=%25E4%25BF%25A1%25E6%2581%25AF%25E5%25B7%25A5%25E7%25A8%258B%25E5%25AD%25A6%25E9%2599%25A2&selectedletters=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'queryObj': 'teacherHome',
}
professors=[]
for page in range(1,4):
    data = {
        'pageIndex': f'{page}',
        'rows': '20',
        'conditions': '[{"orConditions":[{"field":"ownDepartment","value":"16","judge":"="},{"field":"discipline","value":"信息工程学院","judge":"like"},{"field":"title","value":"信息工程学院","judge":"like"},{"field":"career","value":"信息工程学院","judge":"like"},{"field":"exField6","value":"信息工程学院","judge":"like"}]},{"field":"language","value":"1","judge":"="},{"field":"published","value":"1","judge":"="}]',
        'orders': '[{"field":"hot","type":"desc"}]',
        'returnInfos': '[{"field":"title","name":"title"},{"field":"teachDept","name":"teachDept"},{"field":"cnUrl","name":"cnUrl"},{"field":"career","name":"career"},{"field":"headerPic","name":"headerPic"},{"field":"department","name":"department"},{"field":"ownDepartment","name":"ownDepartment"},{"field":"post","name":"post"},{"field":"career","name":"career"},{"field":"workExperience","name":"workExperience"},{"field":"visitCount","name":"visitCount"},{"field":"discipline","name":"discipline"},{"field":"exField1","name":"exField1"},{"field":"exField6","name":"exField6"}]',
        'articleType': '1',
        'level': '0',
        'pageEvent': 'doSearchByPage',
    }

    response = requests.post(
        'https://homepage.zjut.edu.cn/_wp3services/generalQuery',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

    # 检查请求是否成功
    if response.status_code == 200:
        data = response.json()  # 假设响应是 JSON 格式

        # 将 JSON 数据保存到文件中(测试使用)
        with open('professors_page{}.json'.format(page), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("JSON data has been saved to professors.json")
        # 筛选出“教授”及以上职称的人员，需要查看具体的json找字典索引
        professors.append([person for person in data['data'] if '教授' in person['career']])
    else:
        print(f"Request failed with status code {response.status_code} and message {response.text}")
# 输出筛选结果
for professor in professors[0]:
    name = professor['title']
    url = professor['cnUrl']
    print(f"Name: {name}, Home Page: {url}")

    # 访问主页
    home_page_response = requests.get(url)
    if home_page_response.status_code == 200:
        print(f"Successfully accessed the home page of {name}")
        # 这里可以进一步处理主页内容，例如解析 HTML 或者保存内容
    else:
        print(f"Failed to access the home page of {name} with status code {home_page_response.status_code}")



