# Chapter 03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> Sequence, Iterator, Functions, Class
# Class 안에 정의할 수 있는 특별한(Built-In) 메소드

# 클래스 예제2
# (5, 2) + (4, 3) = (9,5)
# (10, 3) * 3 = (30, 9)
# (5,10) 중 높은 값 반환 >> 10

class Vector(object) :
    def __init__(self, *args) :
        '''
        Create a vector, ex) v = Vector(5, 10)
        '''
        if len(args) == 0 :
            self._x, self._y = 0, 0     #예외 처리
        else :
            self._x, self._y = args

    def __repr__(self) :
        '''
        Return the Vector Informations
        '''
        return 'Vector(%r, %r)' %(self._x, self._y)
    
    def __add__(self, other) :
        '''
        Return the vector addition of self & other
        '''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y) :
        '''
        Return the vector multiplication of self & other
        '''
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self) :
        return bool(max(self._x, self._y))
    

# Vector Instance 생성
v1 = Vector(5, 7)
v2 = Vector(27, 32)
v3 = Vector()

# Magic Method 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))
