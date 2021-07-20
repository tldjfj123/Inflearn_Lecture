# include <iostream>
using namespace std;

int main() {
	//// 공용체(union)
	//// 서로 다른 데이터형을 한번에 한가지만 보관할 수 있음.
	//// >> int면 int만, float이면 float만 보관 가능

	//union MyUnion {
	//	int intVal;
	//	long longVal;
	//	float floatVal;
	//};

	//MyUnion test;
	//test.intVal = 3;
	//cout << test.intVal << endl;
	//test.longVal = 33;
	//cout << test.intVal << endl;
	//cout << test.longVal << endl;
	//test.floatVal = 3.3;
	//cout << test.intVal << endl;
	//cout << test.longVal << endl;
	//cout << test.floatVal << endl;

	// 열거체(enum)
	// 기호 상수를 만드는 것에 대한 또 다른 방법

	enum spectrum { red, orange, yellow, green, blue, violet, indigo, ultraviolet };
	/*
	1. spectrum을 새로운 데이터형의 이름으로 만듭니다.
	2. red, orange, yellow...를 0 부터 7지 정수 값을 각각 나타내는 기호 상수로 만듭니다.
	3. 초기화 할 경우 반드시 정수형태
	*/

	spectrum a = orange;
	cout << a << endl;

	int b;
	b = blue;
	b = blue + 3;

	cout << b << endl;

}