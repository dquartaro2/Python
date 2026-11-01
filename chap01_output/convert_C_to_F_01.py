# FILE NAME - convert_C_to_F_01.py

# NAME: Dominick Quartaro
# DATE: September 21st, 2026
# BRIEF DESCRIPTION:Convert_C_to_F_Lab  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

def convert_C_to_F():
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "degrees Celsius is", fahrenheit, "degrees Farenheit.")
convert_C_to_F()












########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?
A float in simple terms is a number that can have a decimal point and without float, pyton would crash tyring to solve this.





2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

It is important because float gives us the ability to turn text into numbers in order to solve formulas. Float allows us to use C * 9 / 5 + 32 and we tried to use string, the math wouldn't happen.
Input() simply gives us text but float allows us to transform that text into decimal form.



'''
