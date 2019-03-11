#include <iostream>

using namespace std;

int main()
{

    int highest=100, lowest=0, attempts=0, guess, pguess;
    char option;
    cout << "Think of a number between 1 and 100" << endl;

    while(option!='q')
    {

        attempts++;
        pguess=guess;
        guess= lowest + ((highest - lowest) * 0.5);
        cout<<"I guess "<<guess<<". Am I right?"<<endl<<"'q' to quit, 'y' if correct, 'h' if too high, 'l' if too low."<<endl;
        cin>>option;

        if(pguess==guess){
            break;
        }

        if(option=='y' || option=='Y')
        {
            cout<<"I guessed it in "<<attempts<<" attempts";
            break;
        }
        else if (option=='h' || option=='H')
        {
            highest=guess;
        }
        else if(option=='l' || option=='L')
        {
            lowest=guess;
        }
    }


    return attempts;
}
