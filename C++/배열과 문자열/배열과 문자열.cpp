# include <iostream>
using namespace std;

int main() {
	/*
	배열(array) : 같은 데이터형의 집합
	typeName arrayName[arraySize];
	*/

	short  month[12] = {1, 2, 3}; // 선언

	cout << month[0] << endl;

	/*
	배열 원소에 대입할 값들을 콤마로 구분하여 중괄호로 묶어 선언한다.
	초기화를 선언 이후 나중에 할 수는 없다.
	배열을 다른 배열에 통째로 대입할 수 없다.
	>> short month[5] = {.....};
	>> short year[12] = {.....};
	>> year = month; << 안된다!
	초기화 값의 갯수를 배열 원소의 갯수보다 모자라게 제공할 수 있다.
	배열을 부분적으로 초기화하면, 나머지 원소들은 0으로 초기화된다.
	배열을 초기화 할때 대괄호 속을 비워두면 컴파일러가 초기화 값의 갯수를 헤아려 배열 원소 갯수를 저장한다.
	*/

	// 문자열 : 문자의 열
	char a[6] = { 'H', 'E', 'L', 'L', 'O', '\0'};

	cout << a << endl;

	char b[] = "HELLO";

	cout << b << endl;

	return 0;
}