# Chapter 04-04
# 시퀀스형
# Hash Table >> 적은 Resource로 많은 Data를 효율적으로 관리
# Dict >> Key 중복 허용 X, Set >> 중복 허용 X
# Dict 및 Set 심화

# Immutable Dic 
from types import MappingProxyType

d = {'key1' : 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# # 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'
print(d)

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Kiwi'}
s2 = set({'Apple', 'Orange', 'Apple', 'Kiwi'})
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Kiwi'})

s1.add('Melon')
print(s1)

# #추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# Byte Code >> Python Interpretor 실행
from dis import dis

print('--------')
print(dis('{10}'))
print('---------')
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)

print('-------')

from unicodedata import name

print({chr(i) for i in range(0, 256)})

