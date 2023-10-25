# Exercise 2: Alien Colors #2


# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# if-else chain

print("\tROUND ONE\n")

# •If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
alien_color = 'green'
alien_color = (input("There are colorful aliens. Who to shoot? The Green , The Red or The Yellow Alien? : For this round, you get less points if you shoot the green alien!"))

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("Yay! You just earned 10 points!")


print("\tROUND TWO\n")


# •If the alien’s color isn’t green, print a statement that the player just earned 10 points.
alien_color = 'yellow'
alien_color = (input("There are colorful aliens. Who to shoot this time? The Green , The Red or The Yellow Alien? : Hint, shoot the green alien..."))

if alien_color == 'red' + 'yellow' :
    print("You just earned 5 points!")
    if alien_color == 'yellow' :
     print("You just earned 5 points!")
else:
    print("You're on a roll! You just earned 10 points!")

    alien_color = 'green'




print("\tTry this extra mini game that runs on the if block and another that runs the else block\n")

## Write one version of this program that runs the if block and another that runs the else block.

###step 1: if block
draw = 'circle'

draw = (input("circle or square? "))
if draw == 'circle':
    print("Circles are awesome")
else:
    print("Squares are cooler")

    draw = 'square'

### else block

if draw == 'square':
    print("That's the end of the debate.")
else:
    print("That's the end of the debate.")

