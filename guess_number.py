from random import randint
# random.randint(a, b)  Create an integer between a and b(include both a and b)

def create_number():
    number_list = [0,1,2,3,4,5,6,7,8,9]
    ret_list = []
    for i in range(4):
        ret_list.append(number_list.pop(randint(0,len(number_list) - 1)))

    return ''.join([str(x) for x in ret_list])

def check_number(goal_number, guess_number):
    A = 0
    B = 0
    for i in range(4):
        if guess_number[i] == goal_number[i]:
            A += 1
        elif guess_number[i] in goal_number:
            B += 1
    return "{}A{}B".format(A,B)
