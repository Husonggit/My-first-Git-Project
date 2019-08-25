#include <iostream>
#include <string>
#include <memory>

class Report
{
private:
	std::string str;
public:
	Report(const std::string s) :str(s)
	{
		std::cout << "Object created! \n";
	}
	~Report()
	{
		std::cout << "Object deleted! \n";
	}
	void comment() const
	{
		std::cout << str << std::endl;
	}
};

using namespace std;
int main()
{
	{
		auto_ptr<Report> ps (new Report("using auto_ptr"));
		ps->comment();
	}


	{
		shared_ptr<Report> ps (new Report("using shared_ptr"));
		ps->comment();

	}
	
	{
		unique_ptr<Report> ps (new Report("using unique_ptr"));
		ps->comment();
	}

	return 0;


}