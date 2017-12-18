#coding=utf-8
import datetime
from data_repository import DataRepository
code_list = ['002415', '002416', '000333']
starttime = '2017-01-01'
endtime = '2017-11-30'
data_repository = DataRepository.get_instance(code_list, starttime, endtime)
print(data_repository.data)

starttime = datetime.datetime