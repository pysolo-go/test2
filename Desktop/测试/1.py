import requests
import re
import pandas as pd


def main():
    for i in range(1, 7):  # 翻页操作，拿到所有页的数据
        data = {
            'pageNo': i,
            'pageSize': 15,
            'isin': '',
            'bondCode': '',
            'issueEnty': '',
            'bondType': 100001,
            'couponType': '',
            'issueYear': 2023,
            'rtngShrt': '',
            'bondSpclPrjctVrty': ''
        }  # 请求携带参数
        resp = requests.post(url, headers=headers, data=data).text  # 发起请求
        ISIN = re.findall('"isin":"(.*?)"', resp)  # 通过正则拿到数据
        for i in ISIN:  # 遍历数据保存进列表
            list1.append(i)
        BondCode = re.findall('"bondCode":"(.*?)"', resp)
        for i in BondCode:
            list2.append(i)
        Issuer = re.findall('"entyFullName":"(.*?)"', resp)
        for i in Issuer:
            list3.append(i)
        BondType = re.findall('"bondType":"(.*?)"', resp)
        for i in BondType:
            list4.append(i)
        IssueDate = re.findall('"issueStartDate":"(.*?)"', resp)
        for i in IssueDate:
            list5.append(i)
        LatestRating = re.findall('"debtRtng":"(.*?)"', resp)
        for i in LatestRating:
            list6.append(i)
        # print(ISIN, BondCode, Issuer, BondType, IssueDate, LatestRating)


def save():
    df['ISIN'] = list1
    df['BondCode'] = list2
    df['Issuer'] = list3
    df['BondType'] = list4
    df['IssueDate'] = list5
    df['LatestRating'] = list5  # 通过pandas构建表单

    df.to_csv(f'./1.csv', encoding='utf_8_sig',
              # 保存时不保存df中的行索引
              index=False)  # 保存成csv文件


if __name__ == '__main__':
    url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }  # 请求头

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []

    df = pd.DataFrame()

    main()  # 函数调用
    save()
