class Car() :
    """
    Car class
    Author : Ahn
    Date : 21. 06. 22
    사용법 : 
    """

    # 클래스 변수 (모든 instance가 공유함.)
    car_count = 0

    def __init__(self, company, details) :
        self._company = company
        self._details = details
        Car.car_count += 1
    
    def __str__(self) :
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self) :
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self) :
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    def __del__(self) :
        Car.car_count -= 1


# Self의 의미
car1 = Car('Ferrari', {'Color' : 'White', 'Horsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'Horsepower' : 270, 'price' : 5000})
car3 = Car('Audi', {'color' : 'Silver', 'Horsepower' : 500, 'price' : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)   # 값을 비교
print(car1 is car2) #instance 자체를 비교


# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))    #dir : 해당 instance가 갖고있는 method들을 모두 보여줌

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()
car3.detail_info()

# 비교
print(car1.__class__)
print(id(car2.__class__) == id(car1.__class__))

# 에러 
# Car.detail_info() -> self인자를 직접 전달 해줘야함.
Car.detail_info(car1)
Car.detail_info(car2)

# 공유 확인
print(car1.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제 확인
print(Car.car_count)

# instance namespace에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(instance 검색 후 -> 상위(class 변수, 부모 class 변수))

