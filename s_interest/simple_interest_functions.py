from tkinter import END


def interest():
    while True:
        try:
            principal = float(input("Enter the principal amount: "))
        except ValueError:
            print("Incorrect input!")
        else:
            while True:
                try:
                    rate = float(input("Enter the rate: "))
                except ValueError:
                    print("Incorrect input!")
                else:
                    while True:
                        try:
                            time = float(input("Enter the time: "))
                        except ValueError:
                            print("Incorrect input!")
                        else:
                            if rate >= 1:  rate /= 100      
                            s_interest = principal*time*rate
                            print("The interest amount is", s_interest)
                            if s_interest:
                                break
                    if s_interest:
                        break
            if s_interest:
                break
def principal():
    
    while True:
        try:
            rate = float(input("Enter the rate: "))
        except ValueError:
            print("Incorrect input!")
        else:        
            if rate == 0:
                print("rate can't be Zero")
            else:  
                while True:
                    try:           
                        time = float(input("Enter the time: "))
                    except ValueError:
                        print("Incorrect input!")
                    else:
                        if time == 0:
                            print("time can't be Zero")
                        else: 
                            while True:
                                try:   
                                    s_interest = float(input("Enter the interest: "))
                                except ValueError:
                                    print("Incorrect input!")
                                else:
                                    if rate >= 1:  rate /= 100
                                    principal =((s_interest)/((time)*(rate)))
                                    ans = "The principal amount is", principal
                                    print(ans)   
                                    if ans or ans == 0:
                                        break
                            if ans or ans == 0:
                                break
                if ans or ans == 0:
                    break

def rate():
    while True:
        try:
            principal = float(input("Enter the principal amount: "))
        except ValueError:
            print("incorrect input")
        else:
            if principal == 0:
                print("Principal can't be Zero")
            else:
                while True:
                    try:
                        time = float(input("Enter the time: "))
                    except ValueError:
                        print("incorrect input")
                    else:
                        if time == 0:
                            print("Time can't be Zero")
                        else:
                            while True:
                                try:
                                    s_interest = float(input("Enter the interest: "))    
                                except ValueError:
                                    print("incorrect input")
                                else:                                        
                                    rate = s_interest/(principal*time)
                                    print("The interest rate is", rate*100, "%")
                                    if rate or rate == 0:
                                        break
                            if rate or rate == 0:
                                break
                if rate or rate == 0:
                    break        



def time():
    while True:
        try:
            principal = float(input("Enter the principal amount: "))
        except ValueError:
            print("incorrect input")
        else:
            if principal == 0:
                print("Principal can't be Zero")
            else:
                while True:
                    try:
                        rate = float(input("Enter the rate: "))  
                    except ValueError:
                        print("incorrect input")        
                    else:
                        if rate == 0:
                            print("rate can't be Zero")
                        else:
                            while True:
                                try:
                                    s_interest = float(input("Enter the Simple Interest Amount: "))
                                except ValueError:
                                    print("incorrect input")
                                else:
                                    if rate >= 1:  rate /= 100
                                    time = s_interest/(principal*rate)
                                    print("The time taken is", time)
                                    if time or time == 0:
                                        break
                            if time or time == 0:
                                break
                if time or time == 0:
                    break
                                            