"""
Created on 2018/7/17
@Author: Jeff Yang
"""

import requests
import re
import json
from openpyxl import Workbook
from pyquery import PyQuery as pq

from cjol.settings import COOKIES


def get_html(url, from_data):
    """获取网页源码"""
    headers = {
        'Cookie': COOKIES,
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


def get_resume_ids(html):
    """获取简历编号"""
    doc = pq(html)
    items = doc('ul .w80 a').items()
    pattern = re.compile('detail-(\d+?)\?Key=')
    for item in items:
        resume_id = re.search(pattern, item.attr('href'))
        yield resume_id[1]


def get_resume_info(html):
    """获取简历上的信息"""
    # 没有匹配到学历等4个基本信息就跳过，用正则程序会卡住
    if any(str not in html for str in ['学历', '性别', '毕业院校', '年龄']):
        return
    resume_info = {}
    doc = pq(html)
    # 简历编号
    resume_id = doc('.resume_info_up').text()[5:]
    # print(resume_id)
    resume_info['resume_id'] = resume_id
    # 简历最后更新时间
    last_update_time = doc('.resume_info_down').text()[7:]
    # print(last_update_time)
    resume_info['last_update_time'] = last_update_time
    pattern = re.compile('.*?学历.*?class="field_right">(.*?)</td>.*?'
                         + '.*?性别.*?class="field_right">(.*?)</td>.*?'
                         + '.*?毕业院校.*?class="field_right">(.*?)</td>.*?'
                         + '.*?年龄.*?class="field_right">(.*?)</td>.*?', re.S)
    result = re.search(pattern, html)
    # # 没有匹配到学历等4个基本信息就跳过
    # if not result:
    #     return
    # 学历
    education = result[1]
    resume_info['education'] = education
    # 性别
    gender = result[2]
    resume_info['gender'] = gender
    # 毕业院校
    graduate_institution = result[3]
    resume_info['graduate_institution'] = graduate_institution
    # 年龄
    age = result[4][:3]
    resume_info['age'] = age
    # print(education)
    # 工作经历
    experiences_list = []
    work_experiences_tr = doc('td:contains("工作经历")').parent().next()
    work_experiences = work_experiences_tr('.work_experience').items()
    # 有些class为work_experience实际不是工作经历而是教育经历之类的
    for work_experience in work_experiences:
        experience_dict = {}
        items = list(work_experience('span').items())
        # 公司
        company = items[0].text()
        experience_dict['company'] = company
        # 职位
        job_title = items[1].text() if len(items) > 1 else ''
        experience_dict['job_title'] = job_title
        # 在职时间
        date_range = items[2].text() if len(items) > 1 else ''
        experience_dict['date_range'] = date_range
        # 工作简介，取前150个字
        work_experience_describe_tr = work_experience.parent().siblings()[1]
        doc2 = pq(work_experience_describe_tr)
        work_experience_describe = doc2('td').text()[:151]
        experience_dict['work_experience_describe'] = work_experience_describe
        experiences_list.append(experience_dict)
        # print(company)
        # print(job_title)
        # print(date_range)
        # print(work_experience_describe)
        # print('======')
    resume_info['work_experiences'] = experiences_list
    return resume_info


def get_resume_info_by_id(resume_id):
    """通过简历ID获取某简历信息"""
    url = "http://newrms.cjol.com/ResumeBank/ResumeOperation"
    from_data = {
        "JobSeekerID": resume_id,
        "bankid": "-1",
        "Fn": "resume",
        "Lang": "CN",
    }
    html = get_html(url, from_data)
    # print(html["OtherData"])
    # with open("resume.html", "w", encoding='utf-8') as f:
    #     f.write(html["OtherData"])
    resume_info = get_resume_info(html["OtherData"])
    # print(data)
    if not resume_info:
        return
    return resume_info


if __name__ == '__main__':
    url = "http://newrms.cjol.com/SearchEngine/List?fn=d"
    with open('resume.json', 'a', encoding='UTF-8') as f:
        for page_num in range(1, 101):
            from_data = {
                "Keyword": "Java",
                "MinWorkExperience": "3",
                "MinEducationText": "大专",
                "MinEducation": "50",
                "ExpectedLocationText": "深圳",
                "ExpectedLocation": "2008",
                "GetListResult": "GetListResult",
                "PageSize": "20",
                "Sort": "UpdateTime desc",
                "PageNo": page_num
            }
            html = get_html(url, from_data)
            for resume_id in get_resume_ids(html):
                print('正在获取简历：', resume_id)
                resume_info = get_resume_info_by_id(resume_id)
                if resume_info:
                    json.dump(resume_info, f, ensure_ascii=False)
                    f.write('\n')
            print(' === Page', page_num, 'done! ===')
