# include <iostream>
using namespace std;

int sumArr(int arr[], int);

const int SIZE = 8;

int main() {
	int arr[SIZE] = { 1, 2, 4, 8, 16, 32, 64, 128 };
	// arr = &arr[0]
	int sum = sumArr(arr, SIZE);

	cout << "함수의 총 합은 " << sum << " 입니다.";
}

int sumArr(int arr[], int n) {
	int total = 0;

	for (int i = 0; i < n; i++) {
		total += arr[i];
	}

	return total;
}