from guess_number import create_number
from guess_number import check_number

while True:
    your_answer = raw_input("Enter your answera number:")
    try:
        if len(your_answer) != 4:
            print "Please enter 4 different digits!"
            continue
        elif len(set([int(your_answer[0]), int(your_answer[1]), int(your_answer[2]), int(your_answer[3])])) != 4:
            print "Please enter 4 different digits!"
            continue
        else:
            break
    except ValueError:
        print "Please enter 4 different digits!"
        continue
my_answer = create_number()
process_dictionary = dict()
error_set = set()
winner = ""
cnt = 0
while True:
    #my guess
    while True:
        my_number = create_number()
        if len(process_dictionary) > 0:
            for reference in process_dictionary:
                if check_number(my_number, reference) != process_dictionary[reference]:
                    error_set.add(my_number)
                    break
        if my_number not in error_set:    
            break
    my_result = check_number(your_answer,my_number)
    if my_result != "4A0B":
        process_dictionary[my_number] = my_result
    #your guess
    your_number = raw_input("Enter your guess number:")
    your_result = check_number(my_answer,your_number)
    #process
    cnt += 1
    print "The {}-th time(s): my answer was {}, and I got {}; your answer was {}, and you got {}".format(cnt, my_number, my_result, your_number, your_result)
    if my_result == "4A0B" and your_result == "4A0B":
        winner = "tie"
    elif my_result == "4A0B" and your_result != "4A0B":
        winner = "me"
    elif my_result != "4A0B" and your_result == "4A0B":
        winner = "you"
    if winner != "":
        break
print "my answer is {}, and your answer is {}".format(my_answer, your_answer)
if winner == "me":
    print "Yeah! I win!!!!!"
if winner == "you":
    print "OK, you win."
if winner == "tie":
    print "It's a tie. Let's start a new game!!!!!"