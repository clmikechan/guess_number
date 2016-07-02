from guess_number import create_number
from guess_number import check_number

while True:
    answer = raw_input("Enter your answer number:")
    try:
        if len(answer) != 4:
            print "Please enter 4 different digits!"
            continue
        elif len(set([int(answer[0]), int(answer[1]), int(answer[2]), int(answer[3])])) != 4:
            print "Please enter 4 different digits!"
            continue
        else:
            break
    except ValueError:
        print "Please enter 4 different digits!"
        continue
process_dictionary = dict()
error_set = set()

while True:
    new_number = create_number()
    if len(process_dictionary) > 0:
        for reference in process_dictionary:
            if check_number(new_number, reference) != process_dictionary[reference]:
                error_set.add(new_number)
                break
    if new_number not in error_set:
        inner_result = check_number(answer,new_number)
        if inner_result == "4A0B":
            break
        else:
            process_dictionary[new_number] = inner_result
            print "my {} time(s) guess is {}, I get {}.".format(len(process_dictionary), new_number, inner_result)
print "my {} time(s) guess is {}, I get {}.".format(len(process_dictionary) + 1, new_number, inner_result)
print "The answer is {}, I use {} times to get the answer.".format(answer, len(process_dictionary) + 1)
print len(error_set)