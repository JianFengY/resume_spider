"""
Created on 2018/7/17
@Author: Jeff Yang
"""

PAY_LOAD = {
    "start": 0,
    "rows": 30,
    "S_DISCLOSURE_LEVEL": 2,
    "S_EXCLUSIVE_COMPANY": "xxxxxxxxxxxx",
    "S_KEYWORD_JOBNAME": "JAVA",
    "S_EDUCATION": "5,1",
    "S_WORK_YEARS": "191907,201507",
    "S_DESIRED_CITY": "765",
    "S_ENGLISH_RESUME": "1",
    "isrepeat": 1,
    "sort": "complex"
}

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.3",
    "Connection": "keep-alive",
    "Content-Length": "265",
    # "Content-Type": "text/plain",
    "Cookie": "xxxxxxxxxxxxx",
    "Host": "rdapi.zhaopin.com",
    "Origin": "https://rd5.zhaopin.com",
    "Referer": "https://rd5.zhaopin.com/custom/searchv2/result",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "zp-route-meta": "uid=707482016,orgid=15435712"
}

OPTIONS_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Control-Request-Headers": "zp-route-meta",
    "Access-Control-Request-Method": "POST",
    "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.3",
    "Connection": "keep-alive",
    "Host": "rdapi.zhaopin.com",
    "Origin": "https://rd5.zhaopin.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}