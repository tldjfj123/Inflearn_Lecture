# Chapte06-01
# 병행성(Concurrency)
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유 >> iter(x) 함수 호출
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for c in t :
    print(c)

# while
w = iter(t)

while 1 :
    try :
        print(next(w))
    except StopIteration :
        break

print()

# 반복형 확인

from collections import abc

print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()
print()

# next
class WordSpliter :
    def __init__(self, text) :
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self) :
        print('Called __next__')
        try :
            word = self._text[self._idx]
        except IndexError :
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self) :
        return 'WordSplit(%s)' % (self._text)


wi = WordSpliter('Do today what you could do tomorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 >> 데이터 양 증가, 증가 후 메모리 사용량 증가 >> 제너레이터 사용 권장
# 2. 단위 실행 가능한 Corotine 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator :
    def __init__(self, text) :
        self._text = text.split(' ')
    
    def __iter__(self) :
        for word in self._text :
            yield word
        return

    def __repr__(self) :
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)
print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

print()
print()