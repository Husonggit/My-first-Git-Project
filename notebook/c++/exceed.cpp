#include <iostream>
#include <climits>

using namespace std;

int main()
{
	short n = SHRT_MAX;
	unsigned short m = SHRT_MAX;

	n = n + 2;
	m = m + 2;

	cout << n << endl;
	cout << m <<endl;

	return 0;
}