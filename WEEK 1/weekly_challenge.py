# PERSONALIZED GREETING APP
# Create a program that asks for the user’s name and 
# favorite color, then prints a personalized greeting 
# like: “Hello, [Name]! Your favorite color, [Color], is awesome!”

# usersName = input("What is your name dear user ")
# usersColor = input("What is your favourite color? ")

# print("Hello " + usersName + " You favourite color is " + usersColor + " and is awesome")



# SIMPLE QUIZ GAME
# Create a multiple-choice quiz with questions about Python, 
# movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆

def play_quiz():
    print("====WELCOME TO SIMPLY QUIZY GAME====")
    print("Let's test your Knowledge on the football World")

    # Correct answers
    correctAnswers = (1995, "Arsenal", "Jose Mourinho")

    # Initialize total score
    totalScore = 0

    # Get user inputs
    eplQuizone = input("When was the Premier League started? ")
    eplQuiztwo = input("Who won the invincible league? ")
    eplQuizthree = input("Which coach is referred to as the 'Chosen one' in the Premier League? ")

    # Convert inputs to lower case to handle case insensitivity
    if str(eplQuizone).strip().lower() == str(correctAnswers[0]).lower():  # Ensure both are strings for comparison
        totalScore += 1

    if eplQuiztwo.strip().lower() == correctAnswers[1].lower():  # No need to convert 'Arsenal' to lowercase, just use it as a string
        totalScore += 1

    if eplQuizthree.strip().lower() == correctAnswers[2].lower():  # Similar for 'Jose Mourinho'
        totalScore += 1

    # Print the final score
    print("Your Total score is " + str(totalScore) + "/3")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_quiz()  # Recursively call the function to restart the game
    else:
        print("Thank you for playing! Goodbye! 🏆")  # End the game

# Start the quiz
play_quiz()


