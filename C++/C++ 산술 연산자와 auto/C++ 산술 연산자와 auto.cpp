# include <iostream>
using namespace std;

int main() {

	/*
	+ : 두 개의 피연산자의 합을 계산한다.
	- : 첫번째 피연산자에서 두번째 피연산자의 차를 계산한다.
	* : 두 개의 피연산자의 곱을 계산한다.
	/ : 첫번째 피 연산자에서 두번째 피연산자를 나눈다.
	     -> 두개의 피연산자가 모두 정수이면 결과값은 '몫' 이다.
	% : 첫번째 피연산자를 두번째 피연산자로 나누어 나머지를 구한다.
	       -> 부동 소수점(실수)에서는 사용할 수 없다.
	*/

	int a = 10;
	int b = 3;

	int c = a + b;
	int d = a - b;
	int e = a * b;
	int f = a / b;
	int g = a % b;

	cout << c << " " << d << " " << e << " " << " " << f << " " << g << endl;

	// C++ 가 복잡한 산술 연산을 수행할 수 있을까 ?? >> YES!
	
	int x = 10;
	int y = 3; 
	int z = 5;

	int multiple = x / y * z;

	cout << multiple << endl;

	float xx = 9.0;
	int yy = 5;

	cout << xx / yy << endl;

	// auto

	auto n = 100; // n = int
	auto q = 1.5; // q = float
	auto w = 1.3e12L; // w = long long
	
	// 3개의 float형 변수 만들려 한다.
	auto k = 0.0;
	float h = 0;
	auto g = 0; // >> int로 인식

	return 0;
}
