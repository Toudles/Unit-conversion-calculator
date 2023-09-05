"""
Assignment #2, Part 3
Andrew Park
"""



print("--------------------------------------------------------------")
print("		mL Conversion Calculator")
print("--------------------------------------------------------------")

#need to turn it into an integer to make it to the second decimal place and convert it into a float.
number = int(input("How many mL would you like to convert? "))
print(format(number, ".2f"), "mL ...")

#unit converter calculator
#format them into floats with commas and second decmial place
teaspoon = format((number * 0.202884), ",.2f")
#use / instead of // to get float
tablespoon = format((number / 14.7867747), ",.2f")
microliter = format((number * 1000), ",.2f")
nanoliter = format((number * 1000000), ",.2f")

print()

#format to make it right alligned 

print("... in teaspoons", format(teaspoon, ">22s"), "tsp")
print("... in tablespoons", format(tablespoon, ">20s"), "tbsp")
print("... in microliters", format(microliter, ">20s"), "uL")
print("... in nanoliters", format(nanoliter, ">21s"), "nL")

#5 ways to crash
#1) in the beginning input, if i don't add the int infront of it and let it run until the print format,
#it'll be a logic error because it'll allow me to put the number in but will stop at the format because you can't
#you can't format a string with .2f because it's not a float or integer.

#2) Another error is when i start the formatting (.2f) with a single quote and end it with a double quote, it would be
#a syntax error because I need to follow form and use double quotes for both or use single quotes for both. 

#3) The third error that's possible is i believe a runtime error when converting the values to the different weights(?). For example
#converting the values and finding the conversions, a runtime error can happen when I make a mistake when typing out 
#the conversion numbers causing me to get wrong outcomes but the code would run perfectly fine.

#4) Another error that can occur is when I'm printing out the final values, I forget to add a comma between the format and
#tsp/tbsp etc. causing a syntax error because the code won't be able to run 

#5) The final error that could occur is a syntax error in which I forget to add an ending double quote leading to an 
#unterminated string literal. 