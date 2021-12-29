####################################################################################################################################################
#
#
#   CSE 231
#   Project 10
#
#   Algorithm
#
#
#       def fix_kings(Tableau):
#
#          for loop through Tableau: 
#
#               if else statements covering all scenarios where King is moved to its left
#               if last element is king and first and second element in king:
#                   assign the last element to temp
#                   switch position of first and second element to 1 and 2
#                   assign temp to index [0]
#
#               if there is 2 kings:
#   
#                   move the two kings in the 1st and 2nd index position based on the value of the suit 
#
#
#       def initialize():
#
#           create a deck by calling cards.deck()
#           shuffle the deck 
#           initialize foundation and tableau as list
#           check = False
#           while loop till check == False
#               for loop till range(3):
#                   call cards.deal, if it returns None break
#                   append 3 cards to a list
#               append the list tableau
#           call fix_kings(Tableau)
#           create a tuple add Tableau and foundation to the tuple
#           return the tuple
#
#
#       def get_option():
#
#           prompt the user for an option
#           split the user input which creates a list
#           if index of the first option is not in the options:
#               print error and return None
#
#           if index of source and destination is wrong:
#               print error and return None
#
#           else convert first index to upper
#           return the option list
#
#
#       def valid_tableau_to_tableau(tableau,s,d):
#   
#           try :
#               if len of destination list is 3:
#                   return False
#
#               elif the difference of ranke of source and destination is not 1:
#                   return False
#               else:
#                   return True
#
#           except IndexError:
#               return False
#
#
#       def valid_tableau_to_foundation(tableau,foundation,s,d):
#   
#           if length of source is 0:
#               return False
#
#           if length of foundation == 0
#               if tableau in a Ace , return False
#
#               else: return True
#
#           elif if the suit of source card and foundation card is not same:
#               return False
#           elif if rank between source and foundation card is  1 :
#               return True
#           else: return False
#
#
#       def move_tableau_to_tableau(tableau,s,d):
#
#
#           call valid_tableau_to_tableau(tableau,s,d)
#           if valid function == True:
#               pop the item from tableau[s] and append it tableau[d], return True
#           if valid function == False:
#               return False
#   
#       def move_tableau_to_foundation(tableau, foundation,s,d):
#
#           call valid_tableau_to_foundation(tableau,foundation,s,d)
#           if valid function == True:
#               pop the item from tableau[s] and append it foundation[d], return True
#           if valid function == False:
#               return False
#           
#       def check_for_win(foundation):
#
#           count == 0
#           if len(foundation[0]) == 13:
#               count +=1
#           else: return False
#           repeat the if statements for every list in foundation and update the count
#           if count == 4:
#               return True
#
#
#       def main():
#
#           print welcome message
#           call the initialize function
#           call display function
#           print(MENU)
#    
#           create moves list
#    
#           prompt the user to enter an option by calling get_option()
#    
#           while loop till the user enter right option
#    
#           while loop till user enters "Q":
#        
#        
#               if option[0] == "MTT":
#            
#                   convert first and second index to int
#                   call valid function to check if it is valid
#            
#                   if valid function == True:
#                
#                       call the move_tableau_to_tableau(tableau, s, d)
#                       display tableau and foundation
#                       convert the option list to tuple and append it to moves list 
#                       prompt the user for an option
#                       continue
#           
#                   if valid function == False:
#                
#                       use format to print error statement
#                       prompt the user for an option 
#                       continue
#            
#               if option[0] == "MTF":
#            
#                   similar method like "MTT" but
#                   if valid is true :
#                   call check_win function:
#                   if user won, restart the game
#        
#               if option[0] == "U":
#            
#                   call undo function
#            
#                   if undo function returns True:
#                       display tableau and foundation
#                       prompt the user for an option 
#                       continue
#            
#                   if undo function returns False:
#                
#                       print no moves to undo
#                       display tableau and foundation
#                       prompt the user for an option 
#                       continue
#            
#               if option [0] == "R":
#            
#                   call the initialize function 
#                   call display function
#                   print(MENU)
#                   prompt the user for an option 
#                   continue
#        
#               if option[0] == "H":
#            
#                   print(MENU)
#                   prompt the user for an option 
#                   continue
#    
#           if option == "Q":
#               print("Thanks for playing")
#
#
#
#
#################################################################################################################################################





#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from end of Tableau pile s to end of pile d.
    MTF s d: Move card from end of Tableau pile s to Foundation d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''

  
def fix_kings(tableau):
    """
    

    Parameters
    ----------
    tableau : list of list
        17 lists in a list and each list has a length of 3.

    Returns
    -------
    None but updates the list.

    """
    
    
   
   
    count = 0
    for i in tableau:
        
       
        count += 1
        
        if count == 18:
            break
        
        if i[2].rank() == 13 and i[0].rank() != 13 and i[1].rank() != 13:
            temp = i[2]
            i[2] = i[1]
            i[1] = i[0]
            i[0] = temp
           
        
        if i[0].rank() != 13 and i[1].rank() == 13 and i[2].rank() != 13:
            temp = i[1]
            i[1] = i[0]
            i[0] = temp
            
        if i[0].rank() == 13 and i[2].rank() == 13 and i[1].rank() != 13 :
            
            if i[2].value() > i[0].value():
                temp = i[2]
                i[2] = i[1]
                i[1] = i[0]
                i[0] = temp
            else:
                
                temp = i[2]
                i[2] = i[1]
                i[1] = temp
        
        if i[0].rank() == 13 and i[1].rank() == 13 and i[2].rank() != 13 :
            
            if i[1].value() > i[0].value():
                
                temp = i[1]
                i[1] = i[0]
                i[0] = temp
        
        if i[0].rank() != 13 and i[1].rank() == 13 and i[2].rank() == 13:
            
           
                
               
                temp = i[1]
                temp_3 = i[0]
                i[1] = i[2]
                i[0] = temp
                i[2] = temp_3
                
           
    
    
    
    
   
                
def initialize():
    """
    

    Returns
    -------
    D : tuple
        first item has a list of 17 list (Tableau) and 2nd  item has a list of 4 empty list (foundation).

    """
   
    
    myDeck = cards.Deck()
    myDeck.shuffle()
    
   
    foundation_list = [[],[],[],[]]
    tableau = []
    
    
    check = False
    
    while check == False:
        t1_list = []
        for i in range(3):
            
            c = myDeck.deal()
            if c == None:
                check = True
                break
            t1_list.append(c)
    
        tableau.append(t1_list)
    
    fix_kings(tableau)
    
    D = tuple()
    
    D = (tableau,foundation_list)
    
    return D
    
    
        
            
    
    
    

def get_option():
    """
    

    Returns
    -------
    op : list
        converts the user input into list.

    """
    
    
   
    
    option = input("\nInput an option (MTT,MTF,U,R,H,Q): ")
    op = option.split()
    
    c = op[0].lower()
    
    if c != "mtt" and c != "mtf" and c != "u" and c != "r" and c != "h" and c != "q":

        if len(op) == 1:        
            print("Error in option:" , op[0])
            return None
        
        if len(op) == 2:
            print("Error in option:" , op[0], op[1])
            return None
        
    if len(op) > 1:
        if int(op [1]) < 0 or int(op[1]) > 17:
            
            print("Error in Source.")
            return None
        
        if int(op [2]) < 0 or int(op[2]) > 17:
            
            print("Error in Destination.")
            return None
    
    
    a = op[0].upper()
    op[0] = a
    
    return op
    
    
          
def valid_tableau_to_tableau(tableau,s,d):
    """
    

    Parameters
    ----------
    tableau : list of list
        17 lists in a list and each list has a length of 3.
    s : int
        position of the source card where the user wants to change.
    d : int
        position of the destination card where the user wants to change.

    Returns
    -------
    bool
        return True if the rank of s and d differ by 1 or else it will return False.

    """
  
    
    s = int(s)
    d = int(d)
    
    
    
    try:
        
        c = tableau[d][-1].rank() - tableau[s][-1].rank()
    
        if len(tableau[d]) == 3:
            return False
        
        
        
        elif c != 1 and c != -1:
            
            return False
        
        else:
            return True
    
    except IndexError:
        
        return False
    
    
def valid_tableau_to_foundation(tableau,foundation,s,d):
    """
    

    Parameters
    ----------
    tableau : list of list
        17 lists in a list and each list has a length of 3.
    foundation : list of list
        4 lists in a list.
    s : int
        position of the source card where the user wants to change.
    d : int
        position of the destination card where the user wants to change.

    Returns
    -------
    bool
        returns True if an empty foundation can only have ace moved to it and
        if the suits agree and the source's rank is one larger or else returns False.

    """
    
    
    s = int(s)
    d = int(d)
    count = 0
    
   
    
    if len(tableau[s]) == 0:
        return False
    
    if len(foundation[d]) == 0:
            
               
            if tableau[s][-1].rank() != 1:
                
               
                return False
             
            else:
                
               
                return True
        
    elif foundation[d][-1].suit() != tableau[s][-1].suit() :
            
        return False
    
        
    elif  tableau[s][-1].rank() - foundation[d][-1].rank()  == 1  :
        
        return True

    else:
        return False
    
    
   
    
def move_tableau_to_tableau(tableau,s,d):
    """
    

    Parameters
    ----------
    tableau : list of list
        17 lists in a list and each list has a length of 3.
    foundation : list of list
        4 lists in a list.
    s : int
        position of the source card where the user wants to change.
    d : int
        position of the destination card where the user wants to change.
    Returns
    -------
    bool
        if valid function is True, it updates the list and returns True 
        or else it returns False.
        

    """
    
    
    
    
    check = valid_tableau_to_tableau(tableau, s, d)
    s = int(s)
    d = int(d)
    
    if check == True:
        
        ad = tableau [s].pop()
        tableau[d].append(ad)
        return True
    
    if check == False:
        
        return False
       
        

def move_tableau_to_foundation(tableau, foundation, s,d):
    """
    

    Parameters
    ----------
    tableau : list of list
        17 lists in a list and each list has a length of 3.
    foundation : list of list
        4 lists in a list.
    s : int
        position of the source card where the user wants to change.
    d : int
        position of the destination card where the user wants to change.

    Returns
    -------
    bool
        if valid function is True, it updates the list and returns True 
        or else it returns False.

    """
   
    
    check_1 = valid_tableau_to_foundation(tableau, foundation, s, d)
    s = int(s)
    d = int(d)
    if check_1 == True:
        
        ad = tableau[s].pop()
        foundation[d].append(ad)
        return True
    
    else:
        
        return False
    
    

def check_for_win(foundation):
    """
    

    Parameters
    ----------
    foundation : list of list
        4 lists in a list.

    Returns
    -------
    bool
       returns True if all the 4 list is full and in right order
       or else it returns False.

    """
   
    
    count = 0 
    if len(foundation[0]) == 13:
        count += 1
    else:
        return False
    if len(foundation[1]) == 13:
        count += 1
    else:
        return False
    if len(foundation[2]) == 13:
        count += 1
    else:
        return False
    
    if len(foundation[3]) == 13:
        count += 1
    else:
        return False
    
    if count == 4:
        
        return True
    
   
  
    

def undo(moves,tableau,foundation):
    '''
    Undo the last move;
       Parameters:
           moves: the history of all valid moves. It is a list of tuples 
                  (option,source,dest) for each valid move performed since the 
                  start of the game. 
           tableau: the data structure representing the tableau.  
       Returns: Bool (True if there are moves to undo. False if not)
    '''
       
    if moves: # there exist moves to undo
        last_move = moves.pop()
        option = last_move[0]
        source = last_move[1]
        dest = last_move[2]
        print("Undo:",option,source,dest)
        if option == 'MTT':
            tableau[source].append(tableau[dest].pop())
        else: # option == 'MTF'
            tableau[source].append(foundation[dest].pop())
        return True
    else:
        return False

def display(tableau, foundation):
    '''Display the foundation in one row;
       Display the tableau in 3 rows of 5 followed by one row of 3.
       Each tableau item is a 3-card pile separated with a vertical bar.'''
    print("\nFoundation:")
    print(" "*15,end='') # shift foundation toward center
    # display foundation with labels
    for i,L in enumerate(foundation):
        if len(L)==0:
            print("{:d}:    ".format(i),end="  ") # padding for empty foundation slot
        else:
            print("{:d}: {} ".format(i,L[-1]),end="  ") # display only "top" card
    print()
    print("="*80)
    print("Tableau:")
    # First fifteen 3-card piles are printed; across 3 rows
    for i in range(15):
        print("{:2d}:".format(i),end='') # label each 3-card pile
        for c in tableau[i]:  # print 3-card pile (list)
            print(c,end=" ")
        print("    "*(3-len(tableau[i])),end='') # pad with spaces
        print("|",end="")
        if i%5 == 4: # start a new line after printing five lists
            print()
            print("-"*80)
    # Final row of only three 3-card piles is printed
    print(" "*15+"|",end='')  # shift first pile right
    for i in range(15,18):
        print("{:2d}:".format(i),end='') # label each 3-card pile
        for c in tableau[i]:
            print(c,end=" ")
        print("    "*(3-len(tableau[i])),end='') # pad with spaces
        print("|",end="")
    print()
    print("-"*80)
    


def main():  
    """
    
    print welcome message
    call the initialize function
    call display function
    print(MENU)
    
    create moves list
    
    prompt the user to enter an option by calling get_option()
    
    while loop till the user enter right option
    
    while loop till user enters "Q":
        
        
        if option[0] == "MTT":
            
            convert first and second index to int
            call valid function to check if it is valid
            
            if valid function == True:
                
                call the move_tableau_to_tableau(tableau, s, d)
                display tableau and foundation
                convert the option list to tuple and append it to moves list 
                prompt the user for an option
                continue
            
            if valid function == False:
                
                use format to print error statement
                prompt the user for an option 
                continue
            
        if option[0] == "MTF":
            
            similar method like "MTT" but
            if valid is true :
                call check_win function:
                    if user won, restart the game
        
        if option[0] == "U":
            
            call undo function
            
            if undo function returns True:
                display tableau and foundation
                prompt the user for an option 
                continue
            
            if undo function returns False:
                
                print no moves to undo
                display tableau and foundation
                prompt the user for an option 
                continue
            
        if option [0] == "R":
            
            call the initialize function 
            call display function
            print(MENU)
            prompt the user for an option 
            continue
        
        if option[0] == "H":
            
            print(MENU)
            prompt the user for an option 
            continue
    
    if option == "Q":
        print("Thanks for playing")
            

     
    """
   
    
    print("\nWelcome to Shamrocks Solitaire.\n")
    
    moves = []
    
    
    D = initialize()
    tableau = D[0]
    foundation = D[1]
    display(tableau,foundation)
    
    print(MENU)
    
    option = get_option()
    
    while option == None :
        
        option = get_option()
    
    while option[0] != "Q":
        
       
        
    
        if option[0] == "MTT":
            
            s = int(option[1])
            d = int(option[2])
            tab_check = valid_tableau_to_tableau(tableau,s,d)
            
            if tab_check == True:
                
                tab_move = move_tableau_to_tableau(tableau, s, d)
                display(tableau,foundation)
                
                moves.append((option[0],int(option[1]), int(option[2])))
                option = get_option()
                continue
                
            if tab_check == False:
                
                print("{}{}{}{}{}{}".format("Error in move: ", option[0] ," , " , s , " , " ,d))
                option = get_option()
                
                while option == None :
                    option = get_option()
                
                continue
        
        if option[0] == "MTF":
            s = int(option[1])
            d = int(option[2])
            tab_found_check = valid_tableau_to_foundation(tableau, foundation, s, d)
            
            if tab_found_check == True:
                
                found_move = move_tableau_to_foundation(tableau, foundation, s, d)
                win_lose = check_for_win(foundation)
                
                
                if win_lose == True:
                    
                    print("You won!")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -")
                    D = initialize()
                    tableau = D[0]
                    foundation = D[1]
                    display(tableau,foundation)
                    print(MENU)
                    option = get_option()
                    while option == None :
                        option = get_option()
                    continue
                    
                else:    
                    display(tableau, foundation)
                    
                    moves.append((option[0],int(option[1]), int(option[2])))
                    option = get_option()
                    while option == None :
                        option = get_option()
                    continue
                
            if tab_found_check == False:
                
                print("{}{}{}{}{}{}".format("Error in move: ", option[0] ," , " , s , " , " ,d))
                option = get_option()
                while option == None :
                    option = get_option()
                continue
                    
        
        if option[0] == "U":
            
            und = undo(moves, tableau, foundation)
            
            if und == False:
                print("No moves to undo.")
                display(tableau,foundation)
                option = get_option()
                while option == None :
                    option = get_option()
                continue
                
            if und == True:
                
                
                display(tableau,foundation)
                option = get_option()
                while option == None :
                    option = get_option()
                continue
                
        if option[0] == "R":
            
            D = initialize()
            tableau = D[0]
            foundation = D[1]
            display(tableau,foundation)
            option = get_option()
            while option == None :
                
                option = get_option()
            continue
        
        if option[0] == "H":
            
            print(MENU)
            option = get_option()
            while option == None :
                option = get_option()
            continue
        

    if option[0] == "Q":
       
        print("Thank you for playing.")
    
    
            
            
            
                    
                    
            
            
            
                
        
            
        
        
        
        
    

if __name__ == '__main__':
     main()