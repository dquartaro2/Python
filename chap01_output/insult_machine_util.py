import random

# You need to add at least five more insults (for a total of at least six)
# Insert your insults into the strings in the list.
insults = [
    'You look like a bunch of rocks',
    'You debug by hoping it never fixes itself',
    'Your logic is missing in action',
    'Even the error message feels bad for you',
    'You type slower than a turtle',
    'Your code has more bugs than a picnic'
]

def welcome():
    print("---------------------------------")
    print("Welcome to the Insulternator 3500")
    print("---------------------------------")
    print()


      


def show_all_insults():
    print(insults)

    
    


def one_insult():
    print(random.choice(insults))

    
    

    
def two_insults():
    one_insult()
    one_insult()
    

    


def insult_specific_name(name):
    print(name + ", here is your insult:", random.choice(insults))
    
    


def insult_x_number_of_insults(num):
    for i in range(num):
        one_insult()
    
    
    


def goodbye():
    print()
    print("---------------------------------------------")
    print("Thank you for playing the Insulternator 3500!")
    print("---------------------------------------------")
    
    

       



