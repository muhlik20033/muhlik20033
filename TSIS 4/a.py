import re

file = open('text',encoding='utf8')
text = file.read()

#Name of the company
NAMEPattern = r"Филиал.*.(?P<name>\b[A-Z]+)"
NAMEtext = re.search(NAMEPattern, text).group('name')
print('1) Name of the company:', NAMEtext, '\n')

#BIN number
BINPattern = r"БИН.(?P<BIN>\d+)"
BINtext = re.search(BINPattern, text).group('BIN')
print('2) BIN Number:', BINtext, '\n')

n=0
ITEMPattern = r"(?P<title>.+)\n(?P<quan>.+).x.(?P<unit_price>.+)\n(?P<total_price>.+)\nСтоимость\n(?P<total_price2>.+)"
ItemPattern = re.compile(ITEMPattern)
for i in re.finditer(ItemPattern, text):
    n+=1
    print('3', end='.')
    print(n, end=')')
    print('\n'+'Title: '+i.group('title')+'\n'+'Quantity: '+i.group('quan')+'\n'+'Unit Price: '+i.group('unit_price')+'\n'+'Total Price:'+i.group('total_price')+'\n')

DATE_ADDRESSPattern = r"Время:.(?P<Date>\d{2}.\d{2}.\d{4}.\d{2}.\d{2}.\d{2})\n(?P<Address>.+\n)"
DATEtext = re.search(DATE_ADDRESSPattern, text).group('Date')
ADDRESStext = re.search(DATE_ADDRESSPattern, text).group('Address')

print('4) Date: '+DATEtext+'\n'*2+'5) Address: '+ADDRESStext)