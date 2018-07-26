"""
Created on 2018/7/17
@Author: Jeff Yang
"""

import requests

from zhilian.settings import PAY_LOAD, HEADERS, OPTIONS_HEADERS


def get_html(url):
    """获取网页源码"""
    session = requests.Session()
    session.options(url, headers=OPTIONS_HEADERS)
    response = session.post(url, data=PAY_LOAD, headers=HEADERS)
    # response.encoding = 'utf-8'
    # print(response.status_code)
    if response.status_code == 200:
        return response.text
    return None


if __name__ == '__main__':
    url = "https://rdapi.zhaopin.com/custom/search/resumeListV2?_=1531895624088"
    html = get_html(url)
    print(html)
