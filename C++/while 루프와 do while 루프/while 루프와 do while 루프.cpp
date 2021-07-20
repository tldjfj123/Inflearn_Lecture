# include <iostream>
using namespace std;

int main() {
	// while문, do while문
	string str = "Panda";
	int i = 0;
	while (str[i] != '\0') {
		cout << str[i] << endl;
		++i;
	}

	bool a = true;
	bool b = false;
	while (b) {
		cout << "Hello!!" << endl;
	}

	int j = 0;
	do {
		cout << "while문 입니다.\n";
		++j;
	} while (j < 3);
	// 조건이 틀리더라도 최소 한번은 진행함
}