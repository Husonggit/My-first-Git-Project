#include <cstdlib>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class A 
{
    public:
    int m_a;
};
 
class B 
{
    public:
    int m_b;
};
 
class C : public A, public B {};

unique_ptr<int> make_init(int n)
{
	return unique_ptr<int> (new int(n));
}

void show(unique_ptr<int> & pi)
{
	const char* a = {"hello.baool"};
	cout << *a << ' ';
}



int mian()
{
	/*C c;
	printf("%p, %p, %p", &c, reinterpret_cast<B*>(&c), static_cast <B*>(&c));*/
	int size = 19;
	std::vector<unique_ptr<int> > vp(size);
	for(int i=0; i<vp.size(); i++)
	{
		vp[i] = make_init(rand() % 1000);
	}

	vp.push_back(make_init(rand() % 1000));

	for_each(vp.begin(), vp.end(), show);
}