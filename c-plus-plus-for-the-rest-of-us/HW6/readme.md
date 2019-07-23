Tic Tac Toe, sometimes called Noughts and Crosses, is a children’s strategy game that can be won, lost or tied in 9 turns or less. [Learn More Here]. The object of the game is to place three Xs or Os in a straight line, vertically, horizontally or diagonally. The game and its rules are sufficiently simple that a text-based version can be created in less than a 130 lines of C++ code.

In our game, empty squares will display the square number. Filled squares will display an X or O. Each player will be prompted in turn to enter the square number (1 to 9). This will continue until a win condition is detected or a stalemate (meaning a draw or a tie) occurs, and no more empty squares exist. If a player enters an illegal number or the number of an occupied square, they will be asked to try again.

1. Create a new, default console project named ‘TicTacToe’ and remove the default “hello world” message.

2. Declare two constants of type char: PLAYER_X and PLAYER_O. Initialize to ‘X’ and ‘O’ respectively.

3. Declare two character variables lastPlayer and currentPlayer. Initialize to PLAYER_O and PLAYER_X respectively, so that player X always takes the first turn.

4. Declare an array of characters that will represent the board. Initialize the array to character values ‘1’ through ‘9’.

5. Use a ‘for’ loop to control the maximum number of turns available. Perform all the remaining game logic within this loop. Note: be sure you have a sufficiently large loop to catch a stalemate and then finish.

6. Display the current board state as follows:
  a. Display a blank line then the message “current board state:” on its own line, then another blank line
  b. Use a pair of nested loops Y and X to control the rows and columns.
  c. Calculate the array index from Y and X coordinates and display the character in that position in the array.
  d. Indent the whole grid display 4 spaces for readability.
  e. Separate each column with a pipe symbol (|) (two per row).
  f. Separate each row with a minus symbol (-) (two per column).
  g. Use the plus sign (+) to represent the intersection between row and column separators.
  h. Follow the grid with a blank line.

7. Check for a winner with nine IF statements. If the three squares specified match the last player, display the last player and winning row (For example, “Player X wins on the top row!”) and exit the loop.
  a. If squares 0,1,2 match, display as “top row” and exit the loop.
  b. If squares 0,4,8 match, display as “upward diagonal” and exit the loop.
  c. And so on for all 9 winning combinations.

8. If the maximum number of turns has taken place, and no winner was found, display the message “Draw. Nobody Wins.” And exit the loop.

9. To handle player input issues, enclose the input code in a potentially infinite while loop. Only exit the loop if input was successful:
  a. Declare an integer variable, chosenSquare.
  b. Display a message “Player {n}, enter a number between 1 and 9: ”
  c. Use cin >> chosenSquare to capture the user’s response.
  d. Note: Humans use a 1-based system but the array is zero based, so decrement the input.
  e. If the user entered a number outside the range specified, display a message “Not a valid choice. Try Again.”
  f. If the user entered a number of a square already containing an ‘X’ or an ‘O’, display the message “That square is not available. Try again.”
  g. If the user entered the number of a valid unoccupied square, update the array so that the square contains the current player’s symbol, and exit the retry loop.

10. In the main body of the for loop, use the std::swap function to switch the current and last player.

11. Before the program terminates, output two line breaks to ensure final game messages are separated from the ‘press any key to continue’ message.

12. Test the program thoroughly. Be sure to test several stalemate games as well as several winning games.


When done, the program’s output should look something like this:

```
current board state:
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
Player X, enter a number between 1 and 9: 5
current board state:
    1|2|3
    -+-+-
    4|X|6
    -+-+-
    7|8|9
Player O, enter a number between 1 and 9: 5
That square is not available. Try again.
Player O, enter a number between 1 and 9: 2
current board state:
    1|O|3
    -+-+-
    4|X|6
    -+-+-
    7|8|9
Player X, enter a number between 1 and 9: 1
current board state:
    X|O|3
    -+-+-
    4|X|6
    -+-+-
    7|8|9

Player O, enter a number between 1 and 9: 9
current board state:
    X|O|3
    -+-+-
    4|X|6
    -+-+-
    7|8|O
Player X, enter a number between 1 and 9: 11
Not a valid choice. Try again.
Player X, enter a number between 1 and 9: 10
Not a valid choice. Try again.
Player X, enter a number between 1 and 9: 4
current board state:
    X|O|3
    -+-+-
    X|X|6
    -+-+-
    7|8|O
Player O, enter a number between 1 and 9: 7
current board state:
    X|O|3
    -+-+-
    X|X|6
    -+-+-
    O|8|O
Player X, enter a number between 1 and 9: 6
current board state:
    X|O|3
    -+-+-
    X|X|X
    -+-+-
    O|8|O
Player X wins on the middle row!
Process returned 0 (0x0)   execution time : 33.306 s
Press any key to continue.

```