import xlsxwriter
import json
from pprint import pprint
import requests

# page = "0"
# data = []
# name = "全国 PPI"
# print(name.split()[0])
# zb = "工业生产者出厂价格指数(上年同月=100)"
# zb = "居民消费价格指数(上月=100)"
# zb = "地区生产总值_累计值(亿元)"
db = "月度数据"
pages = 2
re = requests.get(
    "https://mat1.gtimg.com/news/feiyanarea/shanghai.json", verify=False)
data = re.text
pprint(data)

# workbook = xlsxwriter.Workbook('上海疫情数据.xlsx')
# worksheet = workbook.add_worksheet('2016-2022')

# worksheet.write_row(row=0, col=0, data=[
#                     'date', 'confirm', 'dead', 'heal', 'wzz', 'confirm_sum', 'dead_sum', 'heal_sum', 'wzz_sum'])
# # worksheet.write_row(row=0, col=1, data=[
# #                     str(x) + "年" for x in range(2016, 2023)])

# # worksheet.write_column(row=1, col=0, data=[
# #                        "一月", " 二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"])

# row = 1
# col = 0

# # tmp = 0
# # count = 0

# for i in data:
#     worksheet.write_row(row=row, col=col,
#                         data=[str(i['year']) + '.' + i['date'], int(i['newConfirm']), int(i["newHeal"]), int(i['newDead']), int(i['wzz_add']), int(i['confirm']), int(i['heal']), int(i['dead']), int(i['wzz'])])
#     row += 1
# #     if count % 4 == 0:
# #         tmp = 0
# #     if data[len(data) - i - 1]['zb'] == zb and data[len(data) - i - 1]['db'] == db and data[len(data) - i - 1]['reg'] == name.split()[0] and data[len(data) - i - 1]['data'] != "":

# #         for k in range(3):
# #             worksheet.write_row(row=row, col=col,
# #                                 data=[data[len(data) - i - 1]['sj'], (float(data[len(data) - i - 1]['data']) - tmp) / 3])
# #             row += 1
# #         tmp = float(data[len(data) - i - 1]['data'])
# #         count += 1
# #         # GDP
# #         '''

# #         worksheet.write_row(row=row, col=col,
# #                             data=[data[len(data) - i - 1]['sj'], data[len(data) - i - 1]['data']])
# #         row += 1
# #         count += 1
# #         '''
# # #     if row == 13:
# # #         row = 1
# # #         col += 1

# # # pprint(data)
# workbook.close()
