#include <iostream>
#include <string>
#include <memory>

using namespace std;

int main()
{
	/*auto_ptr<string> films[5] = 
	{
		auto_ptr<string> (new string("Fowl Balls")),
		auto_ptr<string> (new string("Duck Walks")),
		auto_ptr<string> (new string("Chicken Runs")),
		auto_ptr<string> (new string("Turkey Errors")),
		auto_ptr<string> (new string("Goose Eggs"))
	};*/
	//auto_ptr<string> pwin;		//auto_ptr: 错误写法，智能指针放弃所有权后就为空指针了
	shared_ptr<string> films[5] = 
		{
		shared_ptr<string> (new string("Fowl Balls")),
		shared_ptr<string> (new string("Duck Walks")),
		shared_ptr<string> (new string("Chicken Runs")),
		shared_ptr<string> (new string("Turkey Errors")),
		shared_ptr<string> (new string("Goose Eggs"))
	};
	
	shared_ptr<string> pwin;		//shared_ptr: 正确，shared_ptr是引用计数，
	pwin = films[2];

	cout << "The nominees for best avian baseball film are\n";
	for (int i=0; i<5; i++)
		cout << *films[i] << endl;

	cout << "The winner is " << *pwin << "!\n";
	cin.get();

	return 0;

}

