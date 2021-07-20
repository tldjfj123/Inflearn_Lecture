# include <iostream>
using namespace  std;

int main() {
	// 논리 표현식
	// 논리합, 논리곱, 논리 부정 연산자

	// 논리합 || >> or 연산자
	// 논리곱 && >> and 연산자
	// 논리 부정 ! >> not 연산자

	cout << "당신의 나이를 입력하십시오.";
	int age;
	cin >> age;

	if (age < 0 || age > 100) {
		cout << "구라치면 안됩니다.\n";
	}
	else if (20 <= age && age <= 29) {
		cout << "20대\n";
	}
	else {
		cout << "나이를 잘 모르겠습니다.\n";
	}
}