from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Creating empty list to store in it the stack instances
stacks = []

# Creating the stack instances
left_stack, middle_stack, right_stack = Stack("Left"), Stack("Middle"), Stack("Right")

# Adding the stack instances into the empty list above
stacks.extend([left_stack, middle_stack, right_stack])

# Ensuring that the user will enter at least 3 disks to play with 
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

# Adding value to the left side of the stack 
for disk in range(num_disks, 0, -1):
    stacks[0].push(disk)

# Calculating the number of optimal moves in which the game can be solved
num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))


# Creating a function to get the first letter of each stack in stacks' list
def get_input():
    choices = [stack.name[0].lower() for stack in stacks]
    while True:
        for i in range(len(stacks)):
            letter = choices[i]
            name = stacks[i].get_name()
            print("Enter {0} for {1}".format(letter.upper(), name))
        user_input = input("").lower()
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


# Creating a function to print the current stacks' state
def print_current_stacks():
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()


# Creating the game functionality
num_user_moves = 0
# While loop until the right side stack has disks equal to the initial's user choice
while right_stack.get_size() != num_disks:
    print_current_stacks()
    # Nested while loop to perform and track user's moves
    while True:
        # Getting the user input from which stack to move
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        # Getting the user input to which stack to move
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        # Avoiding an edge case where you can't pop a disk from an empty stack
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again.")
            print_current_stacks()
        # If the stack where you want to move to is not empty or your chosen value is less than the uppermost disk
        # of the stack where you want to move to - your move is valid
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            # Increasing the number of the user moves and breaking the inner while loop
            num_user_moves += 1
            break
        else:
            # Any other case is not a valid move
            print("\n\nInvalid Move. Try Again.")
            print_current_stacks()

# Finally, printing the result of the game
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,
                                                                                               num_optimal_moves))