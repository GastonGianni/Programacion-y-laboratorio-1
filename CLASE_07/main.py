# Modulo re (RegExp)
import re

texto = 'uno 1 dos 2 tres 3 cuatro'

#---- split()
print(re.split('[0-9]+', texto))
#['uno ', ' dos ', ' tres ', ' cuatro']
print(re.split('[a-z ]+', texto))
#['', '1', '2', '3', '']

#---- search()
print(re.search('[0-9]+', texto))
#<re.Match object; span=(4, 5), match='1'>
print(re.search('[a-z ]+', texto))
#<re.Match object; span=(0, 4), match='uno '>

#---- findall()
print(re.findall('[0-9]+', texto))
#['1', '2', '3']
print(re.findall('[a-z]+', texto))
#['uno', 'dos', 'tres', 'cuatro']


#---- sub()
# print(re.sub())

# print(re.sub())


