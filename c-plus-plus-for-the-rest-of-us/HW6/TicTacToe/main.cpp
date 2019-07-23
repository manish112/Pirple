#include <iostream>

using namespace std;

int main()
{
    int number;
    char check='n';
    const char PLAYER_X='X', PLAYER_O='O';
    char currentPlayer=PLAYER_X, lastPlayer=PLAYER_O;
    char board[9]={'1','2','3','4','5','6','7','8','9'};

    for(int i=0;i<1;i++){
        cout<<"\n\ncurrent board state:\n\n";

        for(int j=0;j<9;j=j+3){
            for(int k=0;k<3;k++){

                    cout<<board[j+k];
                    if(k==2){
                        cout<<"\n";
                    }else{
                    cout<<"|";
                    }
            }

            cout<<"-+-+-\n";
        }

        while(check!='y'){
        cout<<"Player "<<currentPlayer<<", enter a number between 1 and 9: ";
        cin>>number;
        if(number<1 || number>9){
            cout<<"\nNot a valid choice. Try again.\n";
        }
        else{
            check='y';
        }
        }

    }

    return 0;
}
