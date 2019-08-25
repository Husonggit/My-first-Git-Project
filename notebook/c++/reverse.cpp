#include <iostream>

using namespace std;
//整个句子反转

void allReverse(char s[]){
	int i=0,j=strlen(s)-1;//别忘了减1
	char temp ;

	while(j > i){
		temp = s[i];
		s[i]=s[j];
		s[j]=temp;
		j--;
		i++;
	}
	cout<<s<<endl;
}//allReverse
 
//所有单词反转
void partialReverse(char s[]){
	int i=0,begin,end;
	char temp;
	while(s[i]){
		if(s[i]!=' '){
			begin = i;
			while(s[i] && s[i]!=' '){
				i++;
			}
			i=i-1;
			end = i;
	    }//if
		while(begin<end){
		temp = s[begin];s[begin]=s[end];s[end]=temp;
		begin++;
		end--;
		}//while
		i++;
	}//while
	cout<<s<<endl;
}//partialReverse
 
 
int main(){
 
	char s[1024]="0";
	gets(s);

	cout << s << endl;

	allReverse(s);
	
	partialReverse(s);
}
 
//++C EVOL EHS
//C++ LOVE SHE
