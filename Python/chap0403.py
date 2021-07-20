# Chapter 04-03
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(List, bytearray, array, memoryview, deque)
# 불변(tuple, str, bytes)

# HashTable >> Key에 Value를 저장하는 구조
# Python의 Dictionary가  Hash Table의 예시
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수 >> 해쉬 주소 >> Key에 대한 Value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) >> 예외 발생 (가변)

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source :
    if k in new_dict1 :
        new_dict1[k].append(v)
    else :
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source :
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의사항 >> 아래 경우는 Value 값을 나중 값으로 덮어 씌워버림.
new_dict3 = {k : v for k, v in source}

print(new_dict3)