# include <iostream>
# include <climits>
using namespace std;

int main() {

	// 정수형 : 소수부가 없는 수
	// 음의 정수, 0, 양의 정수
	// short, int, long, long long

	int n_int = INT_MAX;
	short n_short = SHRT_MAX;
	long n_long = LONG_MAX;
	long long n_llong = LLONG_MAX;

	cout << "int는 " << sizeof n_int << "바이트 이다." << endl;
	cout << "이 바이트의 최댓값은 " << n_int << " 이다." << endl;

	cout << "short는 " << sizeof n_short << "바이트 이다." << endl;
	cout << "이 바이트의 최댓값은 " << n_short << " 이다." << endl;

	cout << "long은 " << sizeof n_long << "바이트 이다." << endl;
	cout << "이 바이트의 최댓값은 " << n_long << " 이다." << endl;

	cout << "long long은 " << sizeof n_llong << "바이트 이다." << endl;
	cout << "이 바이트의 최댓값은 " << n_llong << " 이다." << endl;

	unsigned int a;	// 음의 범위를 양의 영역에 더해줌.
	unsigned short b;
	unsigned long c;
	unsigned long long d;

	// 실수형 : 소수부가 있는 수 >> float 사용

}