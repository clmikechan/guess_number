from guess_number import create_number
from guess_number import check_number

while True:
    try:
        times = int(input("Please enter the times that you want:"))
    except ValueError:
        print("Please enter a postive integer!")
    if times > 0:
        break
    else:
        print("Please enter a postive integer!")
sum = 0
times_dictinoary = dict()
for i in range(0, times):
    answer = create_number()
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
    trying_times = len(process_dictionary) + 1
    print("{}-th trying. The answer is {}, I use {} times to get the answer.".format(i, answer, trying_times))
    times_dictinoary[trying_times] = times_dictinoary.get(trying_times, 0) + 1
    sum += (trying_times)
print("The program complete!")
print("The average times is ", sum * 1.0 / times)
for number in times_dictinoary:
    print("There are {} runnings trying {} times".format(times_dictinoary[number], number))