
import random

# step 1
print("Enter the number of friends joining (including you):")
friends_num = int(input())
print("")

# Created an empty list for later
friend_list = []

# step 2
if friends_num <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friends_num):
        friend = input()
        friend_list.append(friend)
        # it takes the keys from the list
        list = dict.fromkeys(friend_list, 0)

    print("")

    # bill part
    print("Enter the total bill value:")
    bill = int(input())
    print("")

    # lucky person
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    answer = input()
    if answer == "Yes":
        winner = random.choice(friend_list)
        print("")
        print(winner, "is the lucky one!")
        # only winner doesn't has to pay
        not_equal = bill / (friends_num - 1)
        not_equal = round(not_equal, 2)
        list_2 = dict.fromkeys(friend_list, not_equal)
        list_2[winner] = 0
        print("")
        print(list_2)

    else:
        print("")
        print("No one is going to be lucky")
        # everyone has to pay
        equal = bill / friends_num
        equal = round(equal, 2)
        list = dict.fromkeys(friend_list, equal)
        print("")
        print(list)
