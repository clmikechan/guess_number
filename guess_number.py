import random
# random.randint(a, b)  Create an integer between a and b(include both a and b)

def create_number():
    number_set = set()
    number_list = []
    while len(number_set) != 4:
        inner_count = len(number_set)
        new_number = random.randint(0, 9)
        number_set.add(new_number)
        if len(number_set) != inner_count:
            number_list.append(new_number)
    return "".join(map(lambda x: str(x), number_list))

def check_number(goal_number, guess_number):
    goal_list = [goal_number[0], goal_number[1], goal_number[2], goal_number[3]]
    guess_list = [guess_number[0], guess_number[1], guess_number[2], guess_number[3]]
    A = 0
    B = 0
    for i in range(0,4):
        if guess_list[i] == goal_list[i]:
            A += 1
        elif guess_list[i] in goal_list:
            B += 1
    return "{}A{}B".format(str(A),str(B))

