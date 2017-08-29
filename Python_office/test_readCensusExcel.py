import os
import census2014
os.chdir('D:\\Python_office')
print(census2014.allData['AK']['Anchorage'])
anchoragePop =census2014.allData['AK']['Anchorage']['pop']
print(str(anchoragePop))
