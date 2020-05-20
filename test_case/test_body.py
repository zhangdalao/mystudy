import re
import requests
from common.get_mysql import *
url ='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-05-18&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'

headers ={
    'Cookie':'JSESSIONID=948580BF138CF9222E0DC0AC2927B2F3; BIGipServerotn=1978138890.64545.0000; RAIL_EXPIRATION=1590095020303; RAIL_DEVICEID=RJPrhbHHIuM9ob6F3GehUJaDIPsPThnPaDYjon0-wNFNWR1-g9khCqGjwYaQFvYEix2shq19gqR47bVlbxt9LrxdgHng-FL0Svz18Fm9_1y8R5en_IjgapkzbLwNjHjqKU18FEIvMGOtVrQe_yq5S8j4Wfq33NEV; BIGipServerpassport=803733770.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2020-05-18; _jc_save_toDate=2020-05-18; _jc_save_wfdc_flag=dc'
}

r = requests.get(url=url,headers=headers)
#print(r.json())
# print(r.json()['httpstatus'])
# print(r.json()['status'])
# print(r.json()['data']['map']['AOH'])
# print(r.json()['data']['result'][5])
# print(r.status_code)
assert r.status_code==200
print(r.content.decode('utf8'))
#执行添加，删除等操作时，可以最后加上assert sql去判断数据库是否添加成功
assert get_sql('select * from table'),"数据库中没有这个数据"


