#include <iostream>
using namespace std;

int main()
{
	int tell[10] = {1,2,3,4,5,6,7,8,9,10};
	int * p1 = &tell[8];
	cout << "p1 = " << p1 << endl;
	int * p2 = &tell[1];
	cout << "p2 = " << p2 << endl;
	int p3 = p1 - p2;  //指针相减，值为元素数目
	cout << "输出指针差：" << p3 << endl;

	cout << tell << endl;
	cout << &tell << endl;
	cout << &tell[1] << endl;
	cout << "------------------" << endl;

	char flower[10] = "rose";
	cout << (int *)flower << endl;
	cout << flower << "s are red" << endl;	//flower是指向字符串的首地址，cout将会打印地址对应的字符，然后继续打印后面的字符知道遇到\0

	return 0;
}