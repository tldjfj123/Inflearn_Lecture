# include <iostream>
using namespace std;

const int SIZE = 30;
int main() {
	/*int a;
	cin >> a;
	switch(a)
	{
	case 1 :
		cout << "입력하신 값은 1입니다.\n";
		break;
	case 2 :
		cout << "입력하신 값은 2입니다.\n";
		break;
	case 3 :
		cout << "입력하신 값은 3입니다.\n";
		break;
	default :
		cout << "입력하신 값은 1, 2, 3 이외의 다른 값 입니다.\n";
	}

	cout << "입력 및 계산이 끝났습니다.\n";*/

	cout << "문장을 입력하십시오.\n";
	char line[SIZE];
	cin.get(line, SIZE);
	cout << "입력하신 문장은 ";
	int spaces = 0;
	for (int i = 0; line[i] != '\0'; i++) {
		cout << line[i];

		if (line[i] != ' ') {
			continue;
		}
		spaces++;
	}

	cout << "입니다/\n";
	cout << "입력하신 문장에서 공백을 제외한 문자 수는 " << spaces << "개 입니다.\n";
	cout << "While문이 끝났습니다.\n";

}