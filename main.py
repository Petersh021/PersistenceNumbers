# Global variables definition :

third_counter = 0  # count recursion number
main_list = []
y = 1  # store the multipication of numbers of one number
sub_counter = 0


# Body of recursion function ################################################################

def persistence(n: int) -> int:
    global main_list, sub_counter, y, third_counter, final_counter
    final_counter = 0

# Seprate Section ###########################################################################

    if n < 10:
        third_counter = 0
        return third_counter
    elif n >= 10:
        counter = 0
        sub_counter = 0
        z = 0
        y = int(1)
        main_list = []
        while n > 0:
            m = int(n % 10)
            n = int(n / 10)
            counter += 1
            sub_list = [m]
            x = sub_list.pop()
            main_list.insert(counter, x)

# Multipication  Section ####################################################################

        for z in range(len(main_list)):
            z = main_list[sub_counter - len(main_list)]
            y *= z
            sub_counter += 1
# Recursion Section #########################################################################
        if y >= 10:
            third_counter += 1
            persistence(y)
# Final phase "return" ######################################################################
        else:
            third_counter += 1
            final_counter = third_counter
            third_counter = 0
        return final_counter

