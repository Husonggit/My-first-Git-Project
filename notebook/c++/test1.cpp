#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	
	const int A = 20;
	char name[A];
	char dessert[A];

	cout << "Enter you name: " << endl;
	cin.getline(name, A);
	cout << "Enter your favorite food: " << endl;
	cin.getline(dessert, A);

	cout << "I love you, " << name << " and I want marray you, ";
	cout << name << ". Don't you? If you want I will give you the food of ";
	cout << dessert << ".\n";


	return 0;
} 










