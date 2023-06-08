"""Write a programm that accepts input from users and solves an 
algebraic math question for them """

"""OUTLINE
1. Display and ask them what problem topic they would want to solve
2. Ask them to supply the known variables (int) and the unknown (str)
3. The program solves and return the answer to them"""

"""FOCUS
1. Simple Interes
2. Compound Interest
3. Linear Equation
4. Quadratic Equation
5. Simultaneous Equation
6. Ratio 
7. Proportion
8. etc"""



#SIMPLE INTEREST
from simple_interest_functions import *

def simple_interest_calculation():
    while True:
        print("\nWhat would you like to find?")
        response = input(
        "Enter: \n\t 'I' for the Interest \n\t 'P' for the Principal Amount \n\t 'R' for the Rate \n\t 'T' for the Time \n\t 'q' to quit.\n")
        if response.lower() == 'i':
            compute_interest()
        elif response.lower() == 'p':
            compute_principal()
        elif response.lower() == 'r':
            compute_rate()
        elif response.lower() == 't':
            compute_time()
        elif response .lower()== 'q':
             break           
        else:
             print("Invalid Response!")
             
simple_interest_calculation()

