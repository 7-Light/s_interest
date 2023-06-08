def get_input_from_user(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Incorrect input! Try again.")


def compute_interest():
    principal = get_input_from_user("Enter the principal amount: ")
    rate = get_input_from_user("Enter the rate: ")
    time = get_input_from_user("Enter the time: ")
    
    if rate >= 1:  rate /= 100      
    s_interest = principal * time * rate

    print("The interest amount is", s_interest)


def compute_principal():
    rate, time = 0, 0

    while rate <= 0:
        rate = get_input_from_user("Enter the rate: ")
        if rate <=  0:
            print("rate should be greater than zero")

    while time <= 0:
        time = get_input_from_user("Enter the time: ")
        if time <= 0:
            print("time should be greater than zero.")

    s_interest = get_input_from_user("Enter the interest: ")

    if rate >= 1:  rate /= 100
    principal = s_interest / (time * rate)

    print("The principal amount is", principal)


def compute_rate():
    principal, time = 0, 0

    while principal <= 0:
        principal = get_input_from_user("Enter the principal amount: ")
        if principal <=  0:
            print("principal should be greater than zero")

    while time <= 0:
        time = get_input_from_user("Enter the time: ")
        if time <= 0:
            print("time should be greater than zero.")

    s_interest = get_input_from_user("Enter the interest: ")

    rate = s_interest * 100 / ( principal * time)
    print(f"The interest rate is {rate}%")


def compute_time():
    principal, rate = 0, 0

    while principal <= 0:
        principal = get_input_from_user("Enter the principal amount: ")
        if principal <=  0:
            print("principal should be greater than zero")

    while rate <= 0:
        rate = get_input_from_user("Enter the rate: ")
        if rate <= 0:
            print("rate should be greater than zero.")

    s_interest = get_input_from_user("Enter the interest: ")

    if rate >= 1:  rate /= 100
    time = s_interest / (principal * rate)
    print("The time taken is", time)
