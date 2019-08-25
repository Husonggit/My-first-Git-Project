#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
     string str;
     string str1;

     vector<string> vec;

     getline(cin, str);
     
     for (int i = 0; i < str.length()+1; i++)
     {   	
     	if(str[i] == ' ' || str[i] == '\0')
     	{
        	vec.push_back(str1);
        	str1 = " ";
     	}
     	str1 += str[i];
     }

     string str2;
     for (int i = vec.size() - 1; i >= 0; --i)
     {
     	str2 += vec[i];
     	//str2 += ' ';
     }

     cout << str2 << endl;

     return 0;
}
