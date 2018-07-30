"""
Created on 2018/7/17
@Author: Jeff Yang
"""

import requests
import re
from pyquery import PyQuery as pq


def get_html(url, from_data):
    """获取网页源码"""
    headers = {
        'Cookie': 'xxxxxxxxxxxxxxxxx',
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


def get_info(html):
    """获取简历上的信息"""
    doc = pq(html)
    # 简历编号
    resume_id = doc('.resume_info_up').text()[5:]
    print(resume_id)
    # 简历最后更新时间
    last_update_time = doc('.resume_info_down').text()[7:]
    print(last_update_time)
    pattern = re.compile('.*?学历.*?class="field_right">(.*?)</td>.*?'
                         + '.*?性别.*?class="field_right">(.*?)</td>.*?'
                         + '.*?毕业院校.*?class="field_right">(.*?)</td>.*?'
                         + '.*?年龄.*?class="field_right">(.*?)</td>.*?', re.S)
    result = re.search(pattern, html)
    # 学历
    education = result[1]
    # 性别
    gender = result[2]
    # 毕业院校
    graduate_institution = result[3]
    # 年龄
    age = result[4]
    print(education)
    # 工作经历
    work_experiences = list(doc('.work_experience').items())
    # 有些class为work_experience实际不是工作经历而是教育经历之类的
    for work_experience in work_experiences[:-1]:
        items = list(work_experience('span').items())
        # 公司
        campany = items[0].text()
        # 职位
        job_title = items[1].text()
        # 在职时间
        date_range = items[2].text()
        work_experience_describe_tr = work_experience.parent().siblings()[1]
        doc2 = pq(work_experience_describe_tr)
        # 工作简介，取前150个字
        work_experience_describe = doc2('td').text()[:151]
        print(campany)
        print(job_title)
        print(date_range)
        print(work_experience_describe)
        print('======')


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
        "JobSeekerID": "9538682",
        "bankid": "-1",
        "Fn": "resume",
        "Lang": "CN",
    }
    html = get_html(url, from_data)
    # print(html["OtherData"])
    # with open("resume.html", "w", encoding='utf-8') as f:
    #     f.write(html["OtherData"])
    get_info(html["OtherData"])
