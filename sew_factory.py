# Riddle 1: Machines & Shirts
'''
It takes 5 machines, 5 minutes to make 5 t-shirts
NOTE: Therefore, each machine needs 5 minutes to make 1 t-shirt.

Question: 
How long will it take 100 machines to make 100 t-shirts?


Question:
How long will it take x machines to make y t-shirts?


Answer: 
Its probably best to reverse the question to, "How long
will it take to make y t-shirts with x machines?" By 
dividing the number of t-shirts with the number of machines
you know how many t-shirts can be made per machine, multiplied 
by the constant of 5 minutes per t-shirt you'll get the total 
time it takes to create the t-shirts.
'''

# time in minutes per t-shirt.
TIMETAKEN_TSHIRT = 5

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

print("Riddle 1: Machines & Shirts:")
n_machines = [5, 100, 200, 200, 100, 300, 5]
n_tshirts = [5, 100, 100, 200, 200, 100, 100]
for idx, t in enumerate(n_tshirts):
    print_time_to_create(n_machines[idx], t)