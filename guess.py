from guess_number import create_number
from guess_number import check_number
ans = ""
goal_number = create_number()
cnt = 0
while ans != "4A0B":
    guess_number = raw_input("Enter your guess number:")
    ans =  check_number(goal_number, guess_number)
    cnt += 1
    print "Your {} time(s) guess is, {}, you get {}".format(cnt, guess_number, ans)
print "The answer is {}, you use {} times to get the answer.".format(goal_number, cnt)