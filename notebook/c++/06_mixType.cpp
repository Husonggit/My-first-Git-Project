#include <iostream>

struct stu
{
	int year;
};

int main()
{
	using namespace std; 
	stu s01, s02, s03;
	s01.year = 1998;

	stu *pa = &s02;
	pa->year = 1999;

	cout << "s01的值为：" << s01.year << "----------" << "s02的值为：" << s02.year << endl;

	stu t[3];
	t[0].year = 2003;

	
	cout << "数组t.year: " << t->year << endl;

	const stu *arp[3] = {&s01, &s02, &s03};
	cout << "结构指针数组arp[1]: " << arp[1]->year << endl;

	const stu **ppa = arp;
	cout << "指向结构指针的指针ppa: " << (*ppa)->year << endl;

	auto ppb = ppa;
	cout << "auto类型 (ppb+1): " << (*(ppb+1))->year << endl;

	return 0;

}