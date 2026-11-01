# FILE NAME - password_strength_test.py

# NAME: Dominick Quartaro
# DATE: October 17th, 2026
# BRIEF DESCRIPTION:Password_Strength_Test  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
print("===== PASSWORD STRENGTH CHECKER =====")
print("This tool analyzes your password and rates its strength.")
print()
print("Enter a password to check:")
password = input()
print()

upper = 0 
lower = 0
digits = 0
special = 0
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"

for letter in password:
    if letter.isupper():
        upper = upper + 1
    elif letter.islower():
        lower = lower + 1
    elif letter.isdigit():
        digits = digits + 1
    elif letter in special_chars:
        special = special + 1

length = len(password)

if length >=12:
    length_score = 25
elif length >= 8:
    length_score = 15
elif length >= 6:
    length_score = 10
else:
    length_score = 0

variety = 0
types = 0

if upper > 0:
    variety = variety + 15
    types = types + 1
if lower > 0:
    variety = variety + 15
    types = types + 1
if digits > 0:
    variety = variety + 15
    types = types + 1
if special > 0:
    variety = variety + 15
    types = types + 1

bonus = 0
if types >= 3:
    bonus = 15

score = length_score + variety + bonus

if score >= 80:
    strength = "STRONG"
elif score >= 60:
    strength ="MODERATE"
elif score >= 40:
    strength="WEAK"
else:
    strength = "VERY WEAK"

print("===== PASSWORD ANALYSIS =====")
print("Length:", length, "characters")
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Special characters:", special)
print()
print("Security Score:", str(score) + "/100")
print("Strength Assessment:", strength)
print()
print("===== IMPROVEMENT SUGGESTIONS =====")

if strength == "STRONG":
    print("- Excellent password! Remember to use different passwords for different accounts.")
else:
    if length < 12:
        print("-Use at least 12 characters for better security")
    if upper == 0:
        print("-Add uppercase letters (A-Z)")
    if digits == 0:
        print("- Add numbers (0-9)")
    if special == 0:
        print("- Add special characters (!@#$%^&*)")
        


              









########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: password

===== PASSWORD ANALYSIS =====
Length: 8 characters
Uppercase letters: 0
Lowercase letters: 8
Digits: 0
Special characters: 0

Security Score: 30/100
Strength Assessment: VERY WEAK

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add uppercase letters (A-Z)
- Add numbers (0-9)
- Add special characters (!@#$%^&*)
'''


'''
This tool analyzes your password and rates its strength.

Enter a password to check: p@SSword!

===== PASSWORD ANALYSIS =====
Length: 9 characters
Uppercase letters: 2
Lowercase letters: 5
Digits: 0
Special characters: 2

Security Score: 75/100
Strength Assessment: MODERATE

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add numbers (0-9)
'''


'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: 4$DL_dsa_dsf!#

===== PASSWORD ANALYSIS =====
Length: 14 characters
Uppercase letters: 2
Lowercase letters: 6
Digits: 1
Special characters: 5

Security Score: 100/100
Strength Assessment: STRONG

===== IMPROVEMENT SUGGESTIONS =====
- Excellent password! Remember to use different passwords for different accounts.
'''
