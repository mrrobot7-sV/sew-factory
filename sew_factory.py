'''
# Riddle 1: Machines & Shirts.

It takes 5 machines, 5 minutes to make 5 t-shirts. How long 
will it take 100 machines to make 100 t-shirts?

In the answer to this question a different implementation has
been created, one that takes into account x machines and y
t-shirts.

Initially, it seems that by dividing the number of t-shirts with
the number of machines multiplied by 5 gives the proper answer
to this question. However, because a different implementation 
was in mind, added conditions had also to be taken into account, 
like even and uneven machines and t-shirts and also considering 
that more machines than t-shirts, leaves some machines out of 
the production process; a condition was added that uses those 
machines when they are double the amount of the t-shirts that need
to be created - demonstrating a possible solution for doubling
the workload, i.e. creating the t-shirts twice as fast.
'''
# time in minutes per t-shirt.
TIMETAKEN_TSHIRT = 5

# calculate the time to create a t-shirt(s) with a given number
# of machines and t-shirts to create.
def get_time_to_create_tshirt(m, t):
    if (m >= t):
        # if there are twice the amount of machines, double the workload
        if (m / t == 2):
            return float((t / m) * TIMETAKEN_TSHIRT)
        return TIMETAKEN_TSHIRT * 1.0

    if (t % m > 0):
        rest = t % m
        time_default = float(((t - rest) / m) * TIMETAKEN_TSHIRT)
        time_rest = TIMETAKEN_TSHIRT * 1.0
        return time_default + time_rest
    elif (t % m == 0):
        return float((t / m) * TIMETAKEN_TSHIRT)

# print the time it takes in minutes for a given number of
# machines and t-shirts
def print_time_to_create(m, t):    
    gttct = get_time_to_create_tshirt(m, t)
    print(f"Total time needed for {m} machines to create {t} shirts: {gttct} minutes.")

# custom exception that can be raised when the input is not a number.
class ValueNotANumberError(ValueError):
    """Raised when the input is not a number."""
    def __init__(self, message = "Error: Value is not a number."):
        self.message = message
        super().__init__(self.message)

# main method
print("Sewing Factory (calculator):")
question_m = "How many machines can be used? "
question_t = "How many t-shirts need to be made? "
question = "Quit the program (y) or do another calculation (n)? [y/n] "
valid_choice = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
quit = False
while quit == False:
    try:        
        m = input(question_m)
        if m.isalpha(): raise ValueNotANumberError()     
        t = input(question_t)   
        if t.isalpha(): raise ValueNotANumberError()       
        print_time_to_create(int(m), int(t))
        choice = input(question).lower()
        if (choice in valid_choice):
            quit = valid_choice[choice]    
        else:
            raise ValueError("Error: Invalid answer: '%s'." % choice)
    except ValueError as e:
       print(e)
       continue

# example that uses a list of values for machines and t-shirts to 
# calculate the t-shirt-creation-times in those situations

# n_machines = [5, 100, 200, 200, 100, 300, 5]
# n_tshirts = [5, 100, 100, 200, 200, 100, 100]
# for idx, t in enumerate(n_tshirts):
#     print_time_to_create(n_machines[idx], t)