# chapter 4, practise 3 based on chapter 4, exercise 2

print("\tTry this extra mini game that runs on the if block and another that runs the else block\n")

## Write one version of this program that runs the if block and another that runs the else block.
work = 'yes'

work = (input("Should I work today? yes or no "))
if work == 'yes':
    print("you get $100! Work again tomorrow to earn $200")
else:
    print("You don't get money... You lost $100 today")

    work = 'no'

work = (input("Should I work tomorrow? yes or no "))

if work == 'no':
    print("You should reconsider to earn $100")
else:
    print("You deserve it! You just earned $200 in total!")