#chapter02-03
#객체 지향 프로그램(OOP) -> 코드의 재사용, 코드 중복 방지, 유지 보수, 대형 프로젝트
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car() :
    """
    Car class
    Author : Ahn
    Date : 21. 06. 22
    Description : Class, Static, Instance Mehod
    """

    # 클래스 변수 (모든 instance가 공유함.)
    car_count = 0
    price_per_raise = 1

    def __init__(self, company, details) :
        self._company = company
        self._details = details
        Car.car_count += 1
    
    def __str__(self) :
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self) :
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def detail_info(self) :
        print("Current ID : {}".format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self) :
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self) :
        return 'Before Car Price -> Company : {}, Price : {}'.format(self._company, self._details.get('price'))

    #Instance Method
    def get_price_culc(self) :
        return 'After Car Price -> Company : {}, Price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise) 

    # Class Method
    @classmethod
    def raise_price(cls, per) :
        if per <= 1 :
            print('Plz Enter 1 or More')
            return
        else :
            cls.price_per_raise = per
            print('Succeed! Price increased!!')

    # Static Method
    @staticmethod
    def is_bmw(inst) :
        if inst._company == 'BMW' :
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry, This car is not BMW.'





# Self의 의미
car1 = Car('Ferrari', {'Color' : 'White', 'Horsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'Horsepower' : 270, 'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
print(car1._details.get('price'))
print(car2._details.get('price'))

# 가격 정보(인상 전)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())


# ID 확인
print(id(car1))
print(id(car2))

print(car1._company == car2._company)   # 값을 비교
print(car1 is car2) #instance 자체를 비교


# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))    #dir : 해당 instance가 갖고있는 method들을 모두 보여줌

print()
print()

print(car1.__dict__)
print(car2.__dict__)




Car.raise_price(1.4)

print(car1.is_bmw(car1))
print(car2.is_bmw(car2))