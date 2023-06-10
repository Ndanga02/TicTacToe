#!/usr/bin/env python
# coding: utf-8

# In[45]:


def display_list(list_name):
    print('HERE IS THE CURRENT LIST')
    print(list_name)


# In[33]:


def chooseNumber():
    choice = 'hello'
    
    while choice not in ['0','1','2']:
        choice = input('Enter number between 0,2:')
        if choice not in ['0','1','2']:
                print('wrong input.Try Again')
    return int(choice)            


# In[34]:


def replaceChoice(list_name,position):
    choice = input('Enter string:')
    list_name[position] = choice


# In[35]:


def game_status_choice():
    choice = 'hello'
    
    while choice not in ['Y','N']:
        choice = input('Play On? Y or N:')
        if choice not in ['N','Y']:
                print('I dont understand. Choose Y/N:')
    if choice == 'Y':
        return True
    else:
        return False


# In[38]:


game_status = True
mylist = [0,1,2]

while game_status:
        display_list(mylist)
        position = chooseNumber()
        replaceChoice(mylist,position)
        display_list(mylist)
        game_status = game_status_choice()


# In[46]:


game_status = True
mylist = [0, 1, 2]

def play_game(game_status):
    while game_status:
        display_list(mylist)
        position = chooseNumber()
        replaceChoice(mylist, position)
        display_list(mylist)
        game_status = game_status_choice()

play_game(game_status)


# In[ ]:




