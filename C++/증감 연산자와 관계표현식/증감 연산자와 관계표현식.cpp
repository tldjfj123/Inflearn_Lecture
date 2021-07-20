# include <iostream>
using namespace std;

int main() {
	for (int i = 0; i < 5; i++) {
		cout << i << "번째 입니다!" << endl;
	}
	/*
	< : 작다
	<= : 작거나 같다
	> : 크다
	>= : 크거나 간다
	== : 같다
	!= : 같지 않다

	*/

	// 증가 연산자, 감소 연산자
	int a = 10;
	int b = 10;

	cout << "a는 " << a << " , b는 " << b << endl;
	cout << "a++는 " << a++ << endl;
	cout << "++b는 " << ++b << endl;
	cout << "a는 " << a << " ,b는 " << b << endl;
	// 전치연산자 : 변수의 값을 먼저 증가시키고 판단함. << 이걸 주로 사용하는게 좋음
	// 후치연산자 : 변수의 값을 먼저 판단 후, 증가시킴.
}