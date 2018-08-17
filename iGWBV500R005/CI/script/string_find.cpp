#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	string a("husong is a good man. and I don't want a good man.");
	string b("man");

	int nu1 = a.find(b);
	cout << "nu1 = " << nu1 << " " << a.at(nu1) << endl;

	//cout << string::npos << endl;
	if(nu1 == string::npos)
		cout << "not found 1" << endl;

	int nu2 = a.find(b, nu1+1);
	cout << "nu2 = " << nu2 << " " << a.at(nu2) << endl;
	if(nu2 == string::npos)
		cout << "not found 2!" << endl;

	return 0;

}