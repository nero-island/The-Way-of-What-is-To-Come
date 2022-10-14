it = 0

def Validation(item, prompt):
    """Makes sure the input value for the item parameter is an integer, and returns it.
    The prompt is simply a custom message that prompts input from the user."""
    while True:
        try:
            item = int(input(prompt))
            break
        except ValueError:
            print("Invalid entry. Please try again.")
    return item

Validation(it, "Enter za numbar:\n")
print(it)