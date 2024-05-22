from yep_lib import *
import requests
from bs4 import BeautifulSoup
import openpyxl as op
import dashscope  #调用qwenAPI

url="https://www.buaa.edu.cn/jgsz/yxsz.htm"   #北京航空航天大学院系设置的网站
url2="https://shi.buaa.edu.cn/zhangjun/zh_CN/more/118704/jsjjgd/index.htm"  #一个院士的信息 北航张军 电子信息工程学院
soup=Req_url(url2)
text=All_text(soup)
test_text="""1. 张军
2. 博导、教授，中国工程院院士，国家杰出青年科学基金获得者，教育部长江学者特聘教授
3. 1
4. 国家技术发明一等奖2项、国家科技进步一等奖1项；教育部长江学者特聘教授；中国工程院院士；国家杰出青年科学基金获得者
5. 0
6. 1
7. 0
8. 0
9. 1
10. 1
11. 1
12. 0
13. 1
14. 0
15. 1
16. 0
17. 0
18. 0
19. 民航空中交通运行监控技术与系统研究，在民航航路网运行监控、星基航路运行监视、民航飞行校验等方向
20. 主持研制了我国民航首个新一代空中交通服务平台、首套星基航路运行监视装备和首套民航机载飞行校验平台"""
information=Qwen_model(text)
print(information)
# print(test_text)
W_excel("高校模板测试.xlsx",information,2)
