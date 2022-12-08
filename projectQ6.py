#6) In this activity, you will create the code that a candy store will use in their state-of-the-art candy vending machine.
# this is already checked
        # Instructions
        # Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.

        # For example: "[0] Snickers"
        # Create a second loop that runs for a set number of times determined by the variable allowance.

        # For example: If allowance is equal to five, the loop should run five times.

        # Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable candy_cart.

        # For example: If the user enters "0" as their input, "Snickers" should be added into the candy_cart list.

        # Use another loop to print all of the candies selected to the terminal.

        # Bonus
        # Create a version of the code that allows a user to select as much candy as they want until they say they do not want any more.

candy = ['Snicker', 'Kit Kat','Lollypop','Mints','M&MS','Hersheys','Skittles','Twix','Milkyway','Starburst']
# include  the allowance accept from user accordingly
print("Welcome to Group Three Candy Vending Machine: ")
n=len(candy)
for i in range(n):
        print('['+ str(i)+']'+ '........> '+candy[i])

print('.......................................')
candy_list=''
allowance=5

for i in range(allowance):
        m=input('Please select your favorite:'+ str(i+1)+ ' ')
        candy_list+=m

for i in range(candy_list):
print(candy_list[i])

# it will print the cart of the candy
