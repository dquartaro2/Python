# FILE NAME - password_strength_analyzer.py

# NAME: Dominick Quartaro
# DATE: October 25th, 2026
# BRIEF DESCRIPTION: Password_Strength_Validator



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


import random


########## ENTER YER CODE BELOW THIS LINE ##########
password = input("Enter your password: ")
print()
length = len(password)
upper = 0
lower = 0
digits = 0
special = 0

for char in password:
    if char.isupper():
        upper = upper + 1
    elif char.islower():
        lower = lower + 1
    elif char.isdigit():
        digits = digits + 1
    else:
        special = special + 1

if length <8:
    length_points = 0
elif length <= 15:
    length_points = 5
else:
    length_points = 8

if upper == 0:
    upper_points = 0
elif upper == 1:
    upper_points = 2
elif upper == 2:
    upper_points = 4
else:
    upper_points = 8

if lower == 0:
    lower_points = 0
elif lower == 1:
    lower_points = 2
elif lower == 2:
    lower_points = 4
else:
    lower_points = 8

if digits == 0:
    digits_points = 0
elif digits == 1:
    digits_points = 2
elif digits ==2:
    digits_points = 4
else:
    digits_points = 8

if special == 0:
    special_points = 0
elif special == 1:
    special_points = 2
elif special ==2:
    special_points = 4
else:
    special_points = 8

total = length_points + upper_points + lower_points + digits_points + special_points
score = total / 40
percentage = score * 100

print()
print("Password Analysis Report")
print("-------------------------")
print("LENGTH:", length_points, "points (" + str(length) + "characters)")
print("UPPERCASE:", upper_points, "points (" + str(upper) + " uppercase letter(s))")
print("LOWERCASE:", lower_points, "points (" + str(lower) + " lowercase letter(s))")
print("NUMBERS:", digits_points, "points (" + str(digits) + " number(s))")
print("SPECIAL CHARACTERS:", special_points, "points (" + str(special) + " special character(s))")
print()
print("Total Score:", score)
print("Strength Percentage:", str(percentage) + "%")








########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
Enter your password: password

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 0 points (0 uppercase letter(s))
LOWERCASE: 8 points (8 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.325
Strength Percentage: 32.5%
'''

'''
Enter your password: p@$$WORD

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 8 points (4 uppercase letter(s))
LOWERCASE: 2 points (1 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.575
Strength Percentage: 57.49999999999999%
'''

'''
Enter your password: 123PASwor

Password Analysis Report
-------------------------
LENGTH: 5 points (9 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.725
Strength Percentage: 72.5%
'''

'''
Enter your password: 123pasWOR!@#

Password Analysis Report
-------------------------
LENGTH: 5 points (12 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.925
Strength Percentage: 92.5%
'''

'''
Enter your password: 123pasWOR!@#888888888888

Password Analysis Report
-------------------------
LENGTH: 8 points (24 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (15 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 1.0
Strength Percentage: 100.0%
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This is one of your first experiences with larger programs - what are three things
   that were challenging for you?
Counting every character type correctly in one loop. Making sure the total divides by 40 so the decimal and percentage match the sample.
Keeping the five scoring locks from overwritting each other.






'''



########################################
#            ATTESTATION
########################################

'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ x] I pretty much get it.
[ ] I'm solid. Totally got it.

'''