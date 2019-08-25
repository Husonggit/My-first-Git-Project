#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cctype>

using namespace std;

const int num=26;
const string wordlist[num] = {"apiary","beetle", "cereal", "danger", "ensign", "florid", "garage", "health", "insult", "jackal", "keeper", 
							"loaner", "manage", "nonce", "onset", "plaid", "quilt", "remote", "stolid", "train", "useful", "valid", "whence", 
							"xenon", "yearn", "zippy"};


int main()
{
	srand(time(0));		//种下随机数种子
	using std::tolower;  //s[i] = tolower(s[i]);
	
	char play;
	cout << "Will you play a word game? <y/n>";
	cin >> play;
	play = tolower(play);

	while(play == 'y')
	{
		string target = wordlist[rand() % num];
		int length = target.length();
		string attempt(length, '-');
		string badchars;
		int guesses = 6;

		cout << "Guess my secret word. It has " << length << " letters, and you guess\n";
		cout << "one letter at a time. You get " << guesses << " wrong guesses.\n";

		cout << "====Your word: " << attempt << endl;

		while(guesses > 0 && attempt != target)
		{
			char letter;
			cout << "----Guess a letter: ";
			cin >> letter;
			
			if(badchars.find(letter) != string::npos || attempt.find(letter) != string::npos)
			{
				cout << "You already guessed that. try again.\n";
				continue;
			}
			int loc = target.find(letter);
			if(loc == string::npos)
			{
				cout << "Oh, bad gusss! \n";
				--guesses;
				badchars += letter;	//add to string
			}
			else 
			{
				cout << "Good guess! \n";
				attempt[loc] = letter;	//check if letter appears again
				loc = target.find(letter, loc+1);
				while(loc != string::npos)
				{
					attempt[loc] = letter;
					loc = target.find(letter, loc + 1);

				}
			}
			cout << "Your word: " << attempt << endl;
			if(attempt != target)
			{
				if(badchars.length() > 0)
					cout << "Bad choices: " << badchars << endl;
				cout << guesses << " bad guesses left. \n";

			}

		}
		if(guesses > 0)
			cout << "That's right! \n";
		else
			cout << "Sorry, the word is " << target << ". \n";
		cout << "Will you play another? <y/n>";
		cin >> play;
	}

	cout << "Bey!!! \n";

	return 0;

}









