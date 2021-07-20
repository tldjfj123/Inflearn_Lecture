# include <iostream>
using namespace std;

const float PIE = 3.14;

void cheers(int n);
float circle(int x); // << 미리 정의되어 있어야 함

int main() {
	
	// 함수를 사용하기 위한 조건
	/*
	1. 함수 정의 제공
	2. 함수 원형 제공
	3. 함수 호출
	*/

	// 함수의 종류
	/*
	1. 리턴값이 있는 타입
	typeName functionName(parameterLIst){
		statement(s);
		return value;
	}

	2. 리턴값이 없는 타입
	void functionName(parameterList){
		statement(s)
		return; // << 생략 가능
	}
	*/

	int a;
	cout << "하나의 수를 입력하시오 : " << "\n";
	cin >> a;
	cheers(a);

	int b;
	cout << "원의 반지름 길이를 입력하십시오. " << endl;
	cin >> b;
	cout << "원의 넓이는 " << circle(b) << " 입니다." << endl;
}

void cheers(int n) {
	for (int i = 0; i < n; i++) {
		cout << "Cheers!" << endl;
	}
}

float circle(int x) {
	return x * x * PIE;
}