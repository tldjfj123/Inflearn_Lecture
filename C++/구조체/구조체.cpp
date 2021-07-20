# include <iostream>
using namespace std;

int main() {
	// 구조체 : 다른 데이터형이 허용되는 데이터의 집합
	// cf) 배열 : 같은 데이터 형의 집합

	// 축구선수
	struct Player
	{
		string name;
		string position;
		float height;
		float weight;
	};

	Player A = { 
		"Park", "MF", 178, 78
	};

	cout << A.name << endl;
	cout << A.position << endl;
	cout << A.height << endl;
	cout << A.weight << endl;

	Player B[2] = {
		{"S", "E", 1, 1},
		{"F", "U", 2, 2}
	};

	cout << B[0].height << endl;
}