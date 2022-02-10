'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3])
print(a[1:4])

Prediction: I'm not sure 
Actual: print(a[0:3]) = ['a', 'b', 'c] and for print(a[1:4]) = ['b', 'c', 'd']

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: I'm not sure because idk what len is 
Actual: prints ['b']

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a)
print(b)

Prediction: will print everything in 'a' but b in the brackets a is equal to 
Actual: print(a) = ['a', 'c', 'd', 'e'] ; print(b) = None

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a)
print(b)

Prediction: print(b) will be invalid because the parenthesis is empty
Actual: print(a) = ['haha','b','c','d'] and print('b') = e

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: print(a) = ['a', 'b', 'c', 'd', 'e'] and print(b) = ['a', 'b', 'c', 'd', 'e','abc']
Actual: print(a) = ['a', 'b', 'c', 'd', 'e'] and print(b) = ['a', 'b', 'c', 'd', 'e','abc']

Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a)
print(b)

Prediction: I'm not 100% sure (other than a will print as it normally has been)
Actual: print (a) = ['a', 'b', 'c', 'd', 'e'] and print(b) = None
2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''


#only one turn is being used 


#print starting board 


board = [[1,2,3] , [4,5,6] , [7,8,9]]


print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print("---------")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")


#Players turn 

turn = int(input("Pick a number and that's where your   x   will go."))


if turn == 1:
    board[0][0] = 'x'
elif turn == 2:
    board[0][1] = 'x'
elif turn == 3: 
    board[0][2] = 'x'
elif turn == 4:
    board[1][0] = 'x'
elif turn == 5:
    board[1][1] = 'x'
elif turn == 6:
    board[1][2] = 'x'
elif turn == 7:
    board[2][0] = 'x'
elif turn == 8:
    board[2][1] = 'x'
elif turn == 9:
    board[2][2] = 'x'

#update board

print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print("---------")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")