import json

import requests
from  bs4 import BeautifulSoup#网页美味汤

def get_data(soup):
    # 定位包含子标题的 <ul> 标签
    subcolumn_lists = soup.find_all("ul", class_="wp_subcolumn_list")
    # 初始化一个字典来存储结果
    results = {}
    # 定义要提取的子标题列表
    target_titles = ["科研项目", "个人简介"]
    # 遍历所有找到的 <ul> 标签
    for subcolumn_list in subcolumn_lists:
        sublists = subcolumn_list.find_all("li", class_="wp_sublist")
        for sublist in sublists:
            title_tag = sublist.find("h3", class_="sublist_title")
            if title_tag:
                title = title_tag.get_text(strip=True)
                # 仅提取目标子标题部分内容
                if title in target_titles:
                    content_div = sublist.find("div", class_="wp_entry")
                    if content_div:
                        content = content_div.get_text(strip=True)
                        results[title] = content

    # 打印结果
    for title, content in results.items():
        print(f"Title: {title}")
        print(f"Content: {content}")
        print("-" * 40)

    # 将结果保存到文件
    with open('selected_subtitles_and_contents.txt', 'w', encoding='utf-8') as f:
        for title, content in results.items():
            f.write(f"Title: {title}\n")
            f.write(f"Content: {content}\n")
            f.write("-" * 40 + "\n")

    print("Selected information has been saved to selected_subtitles_and_contents.txt")

if __name__ == "__main__":
    url = 'http://www.homepage.zjut.edu.cn/yuli'
    response = requests.get(url)
    response.encoding='utf-8'
    soup = BeautifulSoup(response.text, "lxml")

    # 查找研究方向
    research_direction = soup.find("span", id="researchFields")
    research_direction_str="".join([item["fieldValue"] for item in json.loads(research_direction.text)["data"]])
    print(research_direction_str)
