
# KUMAR SAMBHAV MAHIPAL
# UID - 116908108
# ENPM661 - PLANNING FOR AUTONOMOUS ROBOTS
# PROJECT 1 - 8 PUZZLE SOLVER 
# BRUTE FORCE SEARCH ALGORITHM 

import numpy as np
import copy 
import time

Goal_Node = [[1, 2, 3], [4, 5, 7], [7, 8, 0]]
Node_State = []
Parent_Node_Index = []
Nodes_Information = []
path = []
Node_Path = []

# Defining a function to accept the Initial state from the user
def Accept_Initial_Node():
    Temporary_Node = []
    Initial_Node = []
    Temporary_Node = list(map(int, input("Enter the Elements of the Node with space after each element \n ").strip().split()))[:9]
    if len(Temporary_Node) is not 9:
        Accept_Initial_Node()
    Initial_Node.append(Temporary_Node[:3])
    Initial_Node.append(Temporary_Node[3:6])
    Initial_Node.append(Temporary_Node[6:9])
    return Initial_Node

# Defining a function to check the Solvability of the accepted Initial State
def Solvability_Check(Start_Node):
    Test_Node = []
    Inversion_Count = 0
    for a in range(len(Start_Node)):
        for b in range(len(Start_Node[a])):
            if Start_Node[a][b] is 0:
                continue
            Test_Node.append(Start_Node[a][b])
    print(Test_Node)
    for a in range(len(Test_Node) - 1):
        for j in range(i + 1,len(Test_Node)):
            if(Test_Node[i] > Test_Node[b]):
                Inversion_Count += 1
    if(Inverion_Count % 2 is 0):
        return True
    else :
        return False
    
# Defining a function to locate the Blank Tile
def Blank_Tile_Location(Current_Node):
    for a in range(len(Current_Node)):
        for b in range(len(Current_Node[a])):
            if Current_Node[a][b] is 0:
                return a,b
            
# Defining a function to move the Blank Tile towards the left
def Action_To_Move_Left(Current_Node):
    a,b = Blank_Tile_Location(Current_Node)
    if b is not 0:
        New_Node = copy.deepcopy(Current_Node)
        New_Node[a][b], New_Node[a][b - 1] = New_Node[a][b - 1], New_Node[a][b] 
        return Blank_Tile_Location(New_Node), New_Node

# Defining a function to move the Blank Tile towards the right
def Action_To_Move_Right(Current_Node):
    a,b = Blank_Tile_Location(Current_Node)
    if b is not 2:
        New_Node = copy.deepcopy(Current_Node)
        New_Node[a][b], New_Node[a][b + 1] = New_Node[a][b + 1], New_Node[a][b] 
        return Blank_Tile_Location(New_Node), New_Node

            
# Defining a function to move the Blank Tile towards the upper position 
def Action_To_Move_Up(Current_Node):
    a, b = Blank_Tile_Location(Current_Node)
    if a is not 0:
        New_Node = copy.deepcopy(Current_Node)
        New_Node[a][b], New_Node[a - 1][b] = New_Node[a - 1][b], New_Node[a][b] 
        return Blank_Tile_Location(New_Node), New_Node
    
# Defining a function to move the Blank Tile towards the bottom position
def Action_To_Move_Down(Current_Node):
    a,b = Blank_Tile_Location(Current_Node)
    if a is not 2:
        New_Node = copy.deepcopy(Current_Node)
        New_Node[a][b], New_Node[a + 1][b] = New_Node[a + 1][b], New_Node[a][b] 
        return Blank_Tile_Location(New_Node), New_Node
    
# Defining a function to check if a node is new and add it to the list
def Add_Node(New_Node):
    if not (New_Node in Node_State):
        Node_State.append(New_Node)
        Parent_Node_Index.append(Node_State.index(Current_Node))
       

 # Defining a function to find the Solution Path using the Brute Force Search
def Puzzle_Solver(Initial_Node):
    Node_State.append(Initial_Node)
    Parent_Node_Index.append(len(Node_State) - 1)
    global Current_Node
    Current_Node = copy.deepcopy(Initial_Node)
    while(Current_Node != Goal_Node):
        if Action_To_Move_Left(Current_Node) is not None:
            Add_Node(Action_To_Move_Left(Current_Node)[1])
        if Action_To_Move_Right(Current_Node) is not None:
            Add_Node(Action_To_Move_Right(Current_Node)[1])
        if Action_To_Move_Up(Current_Node) is not None:
            Add_Node(Action_To_Move_Up(Current_Node)[1])
        if Action_To_Move_Down(Current_Node) is not None:
            Add_Node(Action_To_Move_Down(Current_Node)[1])

        Current_Node = Node_State[Node_State.index(Current_Node) + 1]
        Nodes_Information.append([Node_State.index(Current_Node), Parent_Node_Index[Node_State.index(Current_Node)], 0])
    return Current_Node

# Defining a function to Generate the Path Sequence to be followed to reach the goal position
def Path_Generation(Current_Node):
    path.append(Node_State.index(Current_Node))
    while(path[0] != 0):
        path.insert(0, Parent_Node_Index[Node_State.index(Current_Node)])
        Current_Node = Node_State[path[0]]
        print(path)

    for a in range(len(path)):
        Node_Path.append(Node_State[path[a]])

    print("Node Information", Nodes_Information)
    print("Node Path", Node_Path)

# Defining a function to Generate the required output files in the defined format
def Output_File_Generation():    
    file = open("NodesInfo.txt", "wt")
    for a in range(len(Nodes_Information)):
        for b in range(len(Nodes_Information[0]) ):
            file.write(str(Nodes_Information[a][b]) + ' ')
        file.write('\n')
        
    file.close()

    file = open("Nodes.txt", "wt")
    for a in range(len(Node_State)):
        for b in range(len(Node_State[a])):
            for c in range(len(Node_State[a][b])):
                file.write(str(Node_State[a][c][b]) + ' ')
        file.write("\n")
                
    file.close()

    file = open("nodePath.txt","wt")
    for a in range(len(Node_Path)):
        for b in range(len(Node_Path[a])):
            for c in range(len(Node_Path[a][b])):
                file.write(str(Node_Path[a][c][b]) + ' ')
        file.write("\n")
        
    file.close()

#Provided Fucntion to Print the Matrix
def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

# Provided Function to Print the Solution 
def PrintSolution():    
    fname = 'NodePath.txt'
    data = np.loadtxt(fname)
    #if len(data[1]) is not 9):
     #   print("Format of the text file is incorrect, retry ")
    #else:
    for a in range(0, len(data)):
        if a == 0:
                print("Start Node")
        elif a == len(data)-1:
                print("Achieved Goal Node")
        else:
            print("Step ",a)
            print()
            
Initial_Node = Accept_Initial_Node()
Solution_Node = Puzzle_Solver(Initial_Node)
Path_Generation(Solution_Node)
Output_File_Generation()
PrintSolution()



