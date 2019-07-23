#include <iostream>

using namespace std;

int main()
{
    int chosenSquare;

    char check='n';
    int flag=0;
    string message;
    const char PLAYER_X='X', PLAYER_O='O';
    char currentPlayer=PLAYER_X, lastPlayer=PLAYER_O;
    char board[9]= {'1','2','3','4','5','6','7','8','9'};

    for(int i=0; i<11; i++)
    {

        /*Print board*/
        cout<<"\n\ncurrent board state:\n\n";

        for(int j=0; j<9; j=j+3)
        {
            for(int k=0; k<3; k++)
            {

                cout<<board[j+k];
                if(k==2)
                {
                    cout<<"\n";
                }
                else
                {
                    cout<<"|";
                }
            }

            cout<<"-+-+-\n";
        }


        /*Check of the game needs to beterminated*/
        if(flag==1)
        {
            cout<<"\nPlayer "<<currentPlayer<<" "<<message;
            break;
        }

        if(i==9)
        {
            cout<<"\nDraw. Nobody Wins.\n\n";
            break;
        }

        /*Take input*/
        while(check!='y')
        {
            cout<<"Player "<<currentPlayer<<", enter a number between 1 and 9: ";
            cin>>chosenSquare;
            if(chosenSquare<1 || chosenSquare>9)
            {
                cout<<"\nNot a valid choice. Try again.\n\n\n";
            }
            else if(board[chosenSquare-1]=='X' || board[chosenSquare-1]=='O')
            {

                cout<<"\nThat square is not available. Try again.\n\n\n";

            }
            else
            {
                check='y';

            }
        }

        check='n';
        board[chosenSquare-1]=currentPlayer;


        /*Check if a player has won*/

        if(board[0]==board[1] && board[1]==board[2])
        {
            message="wins on the top row\n\n";
            flag=1;
        }

        if(board[3]==board[4] && board[4]==board[5])
        {
            message="wins on the middle row\n\n";
            flag=1;
        }

        if(board[6]==board[7] && board[7]==board[8])
        {
            message="wins on the lower row\n\n";
            flag=1;
        }

        if(board[0]==board[3] && board[3]==board[6])
        {
            message="wins on the left column\n\n";
            flag=1;
        }

        if(board[1]==board[4] && board[4]==board[7])
        {
            message="wins on the middle column\n\n";
            flag=1;
        }

        if(board[2]==board[5] && board[6]==board[8])
        {
            message="wins on the right column\n\n";
            flag=1;
        }

        if(board[0]==board[4] && board[4]==board[8])
        {
            message="wins on the upward diagonal\n\n";
            flag=1;
        }

        if(board[2]==board[4] && board[4]==board[6])
        {
            message="wins on the lower diagonal\n\n";
            flag=1;
        }


        /*Don't swap if a winner is decided*/
        if(flag==0)
        {
            std::swap(currentPlayer,lastPlayer);
        }

    }

    return 0;
}
