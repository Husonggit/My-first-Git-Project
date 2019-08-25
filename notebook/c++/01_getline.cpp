#include<iostream>

using namespace std;

int main()
{
	const int ArSize=20;
	char name[ArSize];
	char dessert[ArSize];

	cout << "Enter you name: \n";
	cin.get(name, ArSize).get();

	cout << "Enter you favourite dessert:\n";
	cin.get(dessert, ArSize).get();
	cout << "I have some dilicious " << dessert;
	cout << " for you, " << name << ".\n";
	return 0;

}