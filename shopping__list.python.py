#

#a list to hold on the items
my_list=[]

#defining functions.
def show_exit():
    print (" ENTER YOUR ITEMS AND  WRITE \"DONE\" TO EXIT THE APP")
def show_list():
    print (" AND WRITE \"SHOW\" TO SEE ITEMS IN YOUR LIST")
def help_list():
    print (" AND WRITE \"HELP\'TO SEE WORKING OF HELP AND DONE")
def add_to_list(user_list):
    my_list.append(user_list)

#calling functions    
show_exit()
help_list()
show_list()

#while loop starting as we want to take item input again and again to store it into a list.
while(True):

    #input for the list from the user.
    user_list=raw_input("enter your items for list")

    #if or when user will write DONE as in input the program will break or quit.
    if(user_list=="DONE"):
        break
    #or instead od DONE user writes SHOW it will show items in list till entered.    
    elif(user_list=="SHOW"):
        print(my_list)
    #or instead of show or done user inputs help it will show working of done and show... (either done either help either show)
    elif(user_list=="HELP"):
        show_exit(),show_list()
        continue

    #here else is used if user does not inputs  done,show and help it will append the value into the variable but if user writes done,show,help the user will not append these 3 into user_list variable hence condition will move to else part instead of if or elif..
    else:
        #appending values into list.
        add_to_list(user_list)
    
            

print("YOUR ITEM LIST IS : ")     

# for each value of variable my_list its data will be stored in user_list. 
for user_list in my_list:


    print(user_list)
        




















