import sys
from os import system
from Node import * 
from time import sleep 
import random 

def display_menu(menu):
    """
    Display a menu where the key identifies the name of a function.
    :param menu: dictionary, key identifies a value which is a function name
    :return:
    """
    print(Fore.LIGHTBLUE_EX + "  -> " + Fore.WHITE + " Binary Tree Options " + Fore.LIGHTBLUE_EX + " <-\n\n")
    
    try : 
        print("Main tree -> " , tree.data ,"\n\n")
    except :
        print("Tree is not defined\n\n")
    
    try : 
         print("Second tree -> " , lary.data ,"\n\n")
    except :
        print("Second tree is not defined\n\n")
        

    for k, function in menu.items():
        print(Fore.MAGENTA ,"|",k,"| -> ", Fore.YELLOW ,function.__name__)


def Binarytree():
    system("clear")
    print("you have selected menu option BinaryTree making") # Simulate function output.
    Nodes = []
    global tree
    select = input("Manually(1) or random(2) ? ")
    if select == "1" :
        system("clear")
        while True : 
            n = int(input("Enter the node : "))
            system("clear")
            if (n != -1) : 
                Nodes.append(n)
        
            else : 
                Tree = BinaryTree(Nodes)
                tree = Tree 
                break
    
    elif select == "2" : 
        system("clear")
        rang = int(input("How many nodes do you want to be generated ? "))
        
        for i in range(rang):
            r = random.randint(0,100)
            if r in Nodes : 
                continue 
            else : 
                Nodes.append(r)
        Tree = BinaryTree(Nodes)
        tree = Tree 
        
    
    print(Tree.data)
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout

def Comparing() : 
    system("clear")
    print("you have selected menu option Comparing") # Simulate function output.
    Nodes = []
    global lary 
    while True : 
        n = int(input("Enter the node : "))
        system("clear")
        if (n != -1) : 
            Nodes.append(n)
        
        else : 
            Lary = BinaryTree(Nodes)
            lary = Lary 
            break
    print(Lary.data)
    input("Press Enter to compare\n")
    
    if lary.PrintTree(str(1)) == tree.PrintTree(str(1)) : 
        print("True")
    else : 
        print("False")
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout

        
def Draw():
    system("clear")
    print("you have selected menu option drawing") # Simulate function output.
    
    try : 
        tree.draw()
    except : 
        print("There is no tree or it's been deleted")
        
    input("Press Enter to Continue\n")
    
    system('clear')  # clears stdout


def MAX_and_MIN():
    system("clear")
    print("you have selected menu option max and min") # Simulate function output.
    
    print(tree.MAX_MIN())
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout

def CountLeafs() : 
    system("clear")
    print("you have selected menu option count leafs") # Simulate function output.
    
    print(tree.numberOfLeafs(tree.root))
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout

def DeleteTree() : 
    system("clear")
    print("you have selected menu option delete tree") # Simulate function output.
    
    print(tree.delete_tree())
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout
    
def numberOfFloors() : 
    system("clear")
    print("you have selected menu option number of floors") # Simulate function output.
    
    print(tree.floors_number())
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout
        
def traversal() : 
    system("clear")
    
    while True : 
        print(Fore.LIGHTBLUE_EX + "  -> " + Fore.WHITE + " Traversal Types " + Fore.LIGHTBLUE_EX + " <-")
        print(Fore.MAGENTA , "\n\n  | 1 | ->",Fore.YELLOW," inorder\n",Fore.MAGENTA,"| 2 | ->",Fore.YELLOW," preorder\n",Fore.MAGENTA,"| 3 | ->",Fore.YELLOW," postorder\n",Fore.MAGENTA,"| 4 | ->",Fore.YELLOW," levelorder\n",Fore.MAGENTA,"| 5 | ->",Fore.YELLOW," Exit\n\n")
        select = int(input("Please enter your selection number : "))
        system("clear")
        if (select == 5 ) : 
            break
        else : 
            print(tree.PrintTree(str(select)))
            input("Press Enter to Continue\n")
        system('clear')  # clears stdout
    

def Search() : 
    system("clear")
    print("you have selected menu option search") # Simulate function output.
    
    SearchCase = int(input("\n\nPlease enter your number : "))
    print(tree.search(tree.root , SearchCase))
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout
    
def CheckForFullTree() : 
    system("clear")
    print("you have selected menu option Checking for full tree ") # Simulate function output.
    print(tree.FullTree())
    
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout
    
def Contributors() : 
    system("clear")
    print(Fore.RESET,"\nAmirhossein Sabry 40011573\nKimia Keivanloo 40015753\n\nWWW.GEEKFORGEEKS.COM \u2764\uFE0F")
    sleep(5)
    input("Press Enter to Continue\n")
    system('clear')  # clears stdout
    
def done():
    system('clear')  # clears stdout
    print("Goodbye")
    sys.exit()

def get_word():
      return tree


def main():
    # Create a menu dictionary where the key is an integer number and the
    # value is a function name.
    functions_names = [Binarytree,Comparing, Draw, MAX_and_MIN, CountLeafs , DeleteTree , numberOfFloors ,traversal, Search ,CheckForFullTree, Contributors ,done]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input(Fore.LIGHTMAGENTA_EX + "\nPlease enter your selection number: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function


if __name__ == "__main__":
    from colorama import * 
    print("\n",Fore.WHITE , Back.RED ,"Please define the tree before using other options !!!",Back.RESET , "\n")
    
    main()
