# FILE NAME - convert_C_to_F_02.py

# NAME: Dominick Quartaro
# DATE: October 3rd, 2026
# BRIEF DESCRIPTION:Convert_C_to_F conversion 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====")
print()
print("1. Convert from Celsius to Fahrenheit")
print("2. Convert from Fahrenheit to Celsius")
print()
print("Please choose from the above menu:")
choice = input()
print("Enter a temperature to convert:")
temperature = float(input())
print()

if choice == "1":
    result = temperature * 9 / 5 + 32
    print(temperature, "degrees Celsius is", result, "degrees Fahrenheit.")
else:
    result = (temperature - 32) * 5 / 9
    print(temperature, "degrees Fahrenheit is", result, "degrees Celsius.")










########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
One lesson that I learned or focused my learning on was that temperature has to be converted with Float(). Also using if/else branch for a menu choice.






'''