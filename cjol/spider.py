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
        'Cookie': 'Hm_lvt_36534f4826de8bde820fa4722f1fa7e8=1532484882,1532574156,1532657115,1532915441; ASP.NET_SessionId=otq2fw5bizthkp5jstryuux2; newrms_masterct=newrms08_ct; Hm_lpvt_36534f4826de8bde820fa4722f1fa7e8=1532915476; IsLoginFromSMS=0; CjolRmsSsoFormV7=922827D935A9F67173DC5617FC06BFBED2D6C3D39994A07708ACF1677D3AB200C378A4C615A421FDE203418B4C70FA8D98FEC26F691B5F8062EEDC18D81F569E8F729BF31135ADBAF40F4A185E7C5F5D741A2FA845C41F8E808FAD897725DD89D49594303AA33721B70834EC414E48F1DB66D0ACE36C6B31AB79A23E2A7F1F82111F0102C2D560522EDEE421468AD3913F971EB5288BDE29D3503957E29EC75D03EF708B309F2071FD64F84EAED969CE933DC2424DD3B9285BE254174ED52799DE8149A1CCD038A1411C3A726121579F66996475A2754BE7AEF98E8388267E4556DEE7E362840443E00F3717B95380CF1D2897C506C2BB624AA96D2D9BBE545F4681F572D2A1C0C489F4866F503CD7B473E47972E03470E08AB594858B14F6788CB16AA9F80828238A5E4A14FB5998B51E0EA6C31C61F0212AC7B79B584618DC74D411A0E8EBFDA098D978CABF996DFACAA3FF8F00ACB5B2B1C45D7741F83293AF0158B7036B6A89D656EE925CEEA57CADC8A59AD128961165A2663DAE3DD82356F429E49F913324FDC793E46DA56F3D5C6F9EF78571324CE79C79DD3F77C559F2973B0F140096211D683BFAE35D052F7D12B18E4303CB1C89206E3C87E04E8E5D0C433881CBAF1B68465F87E8FAC0E77B08EBC5B8C3D3C071735C7396887FE4728F087B661AF1FBA0C65F80F4AD17904C622483EF14B1CC54AAB1F205E68C56737DC40EF09CAA26C541B70AE202CBBF7B34B31AE8658E11CD7502659590BB6AD14D69A1602A2576BECA9D4F4E52FE596BBCC43C9C32CDEA17361FF2509432DDA73F166E94D46757FF6CDBE8116B0F332DF4390F7C3B4908CE73C0344756D3CBCBEE3BDA5ACF95F303C61B6E7DE10C827803F6A9152C67528DFFEC5EC459B52902A124E2EE51C35C261C1681A966ED1E837BEF6C3AE6B751354606ED3955B91733E668B77CDA75FC1211CB3B840B7D2CA38A562C312355A83FC25A0B91F175F64FA4A0F50885DC1D53E7FD2BF1F798541D2F0D276487F8A053CA125EFAE94BDFBB6AA542774AFDFEB47FA212518B8810A82C9B808E99A84A52DDFC63DFE7B0FC45EA6FEB42705851C4B7723AE9443F56B8B9312F776B9C3E0D320FAE8D117E26046828E2C7D062A899629C0FC4579FF54F1EF9BEBAD50C9BD67C81A9FA937070E472F3759C6FE00FD6624AC1BACB1ABDC80915B2AA96FC7E440DC9767B2CA8A6302147208E9A1442258B9B20C6A6B83F81B434E9D64377E5B39747A6DC812F1062200B6D161754E331A3BA7DFDFF2D1CA3CBF6045F567A265E63314C13CB198AFCCAB1EDC2036603EC34B72E0F75B1A1AE0D54E69447D1CC36C7373FC0967F2A6C4DD848642E0CA6CDCF011AF40E815A31F5690B855A8428FE80C55B09E7CE95858981621E0FF67EFFDC8658A79A87F4BD442A95387B1809756E56121BAF67F9CBC54C02BA193721A784E35D122485DD0582D6CBE1324EE102D827553CF7C7BFC38499C70095FE27495EA42B3BD20A03F5C87B47C8B9BF8C50E3E9998AA39427B780C768ABDF42335F77C4614A8FA5F0B11DBBB5AFB9770164FA316419D2874A547612A987D69EFA0E6413B342AC824BFC55F129E7781B1D5F9DD76B0A53FB2F8EDA61C4B78EA8465EC8FC7F5BE5D9A5563E539576A5663DF2FBAABC392B0E5D39826C9D98D8123D79299D6BB07EECD4815DA676F483F6AB1B8ACAAA769B79809BED4419ACE6CABA35F735C20C2F9C8DA058CE731718B7D9FB5083222AD012B2EAACFBD5C2ED9C641C2C6E5967BC2B9588B7F0BED41A909DA7F1DB0F3A3CAE431FA2E6E3; CompanyID=155756; RmsCjolProdSso=MTU1NzU2Q09NQTMzOTgwNTF8RjA5QTYwOTAwRDI2MEM0Qjc2NkZFMjcyMTMyRTVENzR8Q3wxMjYxNDI%3d; 201803isPopup=1; status_id=-1; isPopup=true',
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
