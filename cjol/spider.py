"""
Created on 2018/7/17
@Author: Jeff Yang
"""

import requests
from pyquery import PyQuery as pq


def get_html(url, from_data):
    """获取网页源码"""
    headers = {
        'Cookie': 'xxxxxx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    }
    resume_url = "http://newrms.cjol.com/ResumeBank/ResumeOperation"
    response = requests.post(url, data=from_data, headers=headers)
    if response.status_code == 200:
        if url == resume_url:
            return response.json()
        else:
            return response.text
    return None


def get_resume_urls(html):
    """获取简历url"""
    doc = pq(html)
    base_url = "http://newrms.cjol.com"
    items = doc('ul .w80 a').items()
    for item in items:
        yield base_url + item.attr('href')


if __name__ == '__main__':
    url = "http://newrms.cjol.com/SearchEngine/List?fn=d"
    from_data = {
        "Keyword": "Java",
        "MinWorkExperience": "3",
        "MinEducationText": "大专",
        "MinEducation": "50",
        "ExpectedLocationText": "深圳",
        "ExpectedLocation": "2008",
        "GetListResult": "GetListResult",
        "PageSize": "20",
        "Sort": "UpdateTime desc"
    }
    html = get_html(url, from_data)
    # print(html)
    # for url in get_resume_urls(html):
    #     print(url)
    url = "http://newrms.cjol.com/ResumeBank/ResumeOperation"
    from_data = {
        "JobSeekerID": "9139471",
        "bankid": "-1",
        "Fn": "resume",
        "Lang": "CN",
    }
    html = get_html(url, from_data)
    print(html)
