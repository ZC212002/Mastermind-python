# A Master Mind Computer Game.

# User Interface when end-user starting to play Master Mind Computer Game.
print(" Welcome to the Master Mind Computer Game ! ")
print(" Enter yes to play and enter no to exit ↓ " )
play = input(" Do you want to play ? ")
# Error Handling and Data Validation.
while str(play) != "yes" and str(play) != "no":
    print(" <Enter only yes or no> ")
    play = input(" Do you want to play ? ")
if str(play) == "yes":
    while str(play) == "yes":
        input(" Please enter the username for you to access the game: ")
        print(" Guess any four colours in the list [O, P, G, Y] below ! ")
        print(" You can choose the same colour from the list repeatedly ! ")
        print(" O = ORANGE | P = PINK | G= GREEN | Y = YELLOW ")

# Import random module from the python library.
        import random

# List of colours.
        colours = ["O", "P", "G", "Y"] 

# Define a function for a list of random colours.
        def secret_list () :
            colours_list = [ ]
            secret_list = 0
            for count in range (0, 4) :
                secret_list = random.randint(0, 3)
                colours_list.append(colours[secret_list])
            return colours_list

# Assign secret_list to mastermind list for comparison and checking purposes below.
        mastermind_list = secret_list ()

# Assign and initialize the value for each variable below.
        correct_colour_correctplace = 0
        correct_colour_wrongplace = 0
        guessing_times = 0

# Guessing parts.
        while correct_colour_correctplace < 4 :
            first_guess_colour = input(" Guess the first colour: ")
            # Error Handling and Data Validation.
            while first_guess_colour.upper () not in colours:
                print(" Guess only the colours list provided [O, P, G, Y] ")
                first_guess_colour = input(" Guess the first colour: ")
            second_guess_colour = input(" Guess the second colour: ")
            # Error Handling and Data Validation.
            while second_guess_colour.upper () not in colours:
                print(" Guess only the colours list provided [O, P, G, Y] ")
                second_guess_colour = input(" Guess the second colour: ")
            third_guess_colour = input(" Guess the third colour: ")
            # Error Handling and Data Validation.
            while third_guess_colour.upper () not in colours:
                print(" Guess only the colours list provided [O, P, G, Y] ")
                third_guess_colour = input(" Guess the third colour: ")
            fourth_guess_colour = input(" Guess the fourth colour: ")
            # Error Handling and Data Validation.
            while fourth_guess_colour.upper () not in colours:
                print(" Guess only the colours list provided [O, P, G, Y] ")
                fourth_guess_colour = input(" Guess the fourth colour: ")

            # Record how many times the end-user to guess it correctly.
            guessing_times += 1

#  Checking the correct colour in correct place.
            if first_guess_colour.upper() == mastermind_list [0] :
                correct_colour_correctplace += 1
            if second_guess_colour.upper() == mastermind_list [1] :
                correct_colour_correctplace += 1
            if third_guess_colour.upper() == mastermind_list [2] :
                correct_colour_correctplace += 1
            if fourth_guess_colour.upper() == mastermind_list [3] :
                correct_colour_correctplace += 1

# Assign and initialize value for each variable below.
            ORANGE_count = 0
            ORANGE_code = 0
            ORANGE_correct_colour_correctplace = 0

# Preparation of variables to find the correct colour in wrong place.
            if first_guess_colour.upper() == "O" :
                ORANGE_count += 1
            if second_guess_colour.upper() == "O" :
                ORANGE_count += 1
            if third_guess_colour.upper() == "O" :
                ORANGE_count += 1
            if fourth_guess_colour.upper() ==  "O" :
                ORANGE_count += 1
            if mastermind_list [0] == "O" :
                ORANGE_code += 1
            if mastermind_list [1] == "O" :
                ORANGE_code += 1
            if mastermind_list [2] == "O" :
                ORANGE_code += 1
            if mastermind_list [3] == "O" :
                ORANGE_code += 1
        
            if mastermind_list [0] == first_guess_colour.upper() and first_guess_colour.upper() == "O" :
                ORANGE_correct_colour_correctplace += 1
            if mastermind_list [1] == second_guess_colour.upper() and second_guess_colour.upper() == "O" :
                ORANGE_correct_colour_correctplace += 1
            if mastermind_list [2] == third_guess_colour.upper() and third_guess_colour.upper() == "O" :
                ORANGE_correct_colour_correctplace += 1
            if mastermind_list [3] == fourth_guess_colour.upper() and fourth_guess_colour.upper() == "O" :
                ORANGE_correct_colour_correctplace += 1

# Assign and initialize value for each variable below.
            PINK_count = 0
            PINK_code = 0
            PINK_correct_colour_correctplace = 0

# Preparation of variables to find the correct colour in wrong place.
            if first_guess_colour.upper() == "P" :
                PINK_count += 1
            if second_guess_colour.upper() == "P" :
                PINK_count += 1
            if third_guess_colour.upper() == "P" :
                PINK_count += 1
            if fourth_guess_colour.upper() ==  "P" :
                PINK_count += 1
            if mastermind_list [0] == "P" :
                PINK_code += 1
            if mastermind_list [1] == "P" :
                PINK_code += 1
            if mastermind_list [2] == "P" :
                PINK_code += 1
            if mastermind_list [3] == "P" :
                PINK_code += 1

            if mastermind_list [0] == first_guess_colour.upper() and first_guess_colour.upper() == "P" :
                PINK_correct_colour_correctplace += 1
            if mastermind_list [1] == second_guess_colour.upper() and second_guess_colour.upper() == "P" :
                PINK_correct_colour_correctplace += 1
            if mastermind_list [2] == third_guess_colour.upper() and third_guess_colour.upper() == "P" :
                PINK_correct_colour_correctplace += 1
            if mastermind_list [3] == fourth_guess_colour.upper() and fourth_guess_colour.upper() == "P" :
                PINK_correct_colour_correctplace += 1

# Assign and initialize value for each variable below.
            GREEN_count = 0
            GREEN_code = 0
            GREEN_correct_colour_correctplace = 0

# Preparation of variables to find the correct colour in wrong place.
            if first_guess_colour.upper() == "G" :
                GREEN_count += 1
            if second_guess_colour.upper() == "G" :
                GREEN_count += 1
            if third_guess_colour.upper() == "G" :
                GREEN_count += 1
            if fourth_guess_colour.upper() ==  "G" :
                GREEN_count += 1
            if mastermind_list [0] == "G" :
                GREEN_code += 1
            if mastermind_list [1] == "G" :
                GREEN_code += 1
            if mastermind_list [2] == "G" :
                GREEN_code += 1
            if mastermind_list [3] == "G" :
                GREEN_code += 1

            if mastermind_list [0] == first_guess_colour.upper() and first_guess_colour.upper() == "G" :
                GREEN_correct_colour_correctplace += 1
            if mastermind_list [1] == second_guess_colour.upper() and second_guess_colour.upper() == "G" :
                GREEN_correct_colour_correctplace += 1
            if mastermind_list [2] == third_guess_colour.upper() and third_guess_colour.upper() == "G" :
                GREEN_correct_colour_correctplace += 1
            if mastermind_list [3] == fourth_guess_colour.upper() and fourth_guess_colour.upper() == "G" :
                GREEN_correct_colour_correctplace += 1

# Assign and initialize value for each variable below.
            YELLOW_count = 0
            YELLOW_code = 0
            YELLOW_correct_colour_correctplace = 0

# Preparation of variables to find the correct colour in wrong place.
            if first_guess_colour.upper() == "Y" :
                YELLOW_count += 1
            if second_guess_colour.upper() == "Y" :
                YELLOW_count += 1
            if third_guess_colour.upper() == "Y" :
                YELLOW_count += 1
            if fourth_guess_colour.upper() ==  "Y" :
                YELLOW_count += 1
            if mastermind_list [0] == "Y" :
                YELLOW_code += 1
            if mastermind_list [1] == "Y" :
                YELLOW_code += 1
            if mastermind_list [2] == "Y" :
                YELLOW_code += 1
            if mastermind_list [3] == "Y" :
                YELLOW_code += 1

            if mastermind_list [0] == first_guess_colour.upper() and first_guess_colour.upper() == "Y" :
                YELLOW_correct_colour_correctplace += 1
            if mastermind_list [1] == second_guess_colour.upper() and second_guess_colour.upper() == "Y":
                YELLOW_correct_colour_correctplace += 1
            if mastermind_list [2] == third_guess_colour.upper() and third_guess_colour.upper() == "Y" :
                YELLOW_correct_colour_correctplace += 1
            if mastermind_list [3] == fourth_guess_colour.upper() and fourth_guess_colour.upper() == "Y" :
                YELLOW_correct_colour_correctplace += 1

# Checking the correct colour in wrong place by comparing them.
            if [first_guess_colour.upper(), second_guess_colour.upper(), third_guess_colour.upper(), fourth_guess_colour.upper()] != mastermind_list:
                if ORANGE_count >= ORANGE_code and ORANGE_count >= ORANGE_correct_colour_correctplace:
                    ORANGE_check = 0
                if ORANGE_correct_colour_correctplace <= ORANGE_code <= ORANGE_count:
                    ORANGE_check = ORANGE_code - ORANGE_correct_colour_correctplace
                if ORANGE_code > ORANGE_count >= ORANGE_correct_colour_correctplace:
                    ORANGE_check = ORANGE_count - ORANGE_correct_colour_correctplace

                if PINK_count >= PINK_code and PINK_count >= PINK_correct_colour_correctplace:
                    PINK_check = 0
                if PINK_correct_colour_correctplace <= PINK_code <= PINK_count:
                    PINK_check = PINK_code - PINK_correct_colour_correctplace
                if PINK_code > PINK_count >= PINK_correct_colour_correctplace:
                    PINK_check = PINK_count - PINK_correct_colour_correctplace

                if GREEN_count >= GREEN_code and GREEN_count >= GREEN_correct_colour_correctplace:
                    GREEN_check = 0
                if GREEN_correct_colour_correctplace <= GREEN_code <= GREEN_count:
                    GREEN_check = GREEN_code - GREEN_correct_colour_correctplace
                if GREEN_code > GREEN_count >= GREEN_correct_colour_correctplace:
                    GREEN_check = GREEN_count - GREEN_correct_colour_correctplace

                if YELLOW_count >= YELLOW_code and YELLOW_count >= YELLOW_correct_colour_correctplace:
                    YELLOW_check = 0
                if YELLOW_correct_colour_correctplace <= YELLOW_code <= YELLOW_count:
                    YELLOW_check = YELLOW_code - YELLOW_correct_colour_correctplace
                if YELLOW_code > YELLOW_count >= YELLOW_correct_colour_correctplace:
                    YELLOW_check = YELLOW_count - YELLOW_correct_colour_correctplace

# Display the results of correct colour in correct place and correct colour in wrong place.
            if correct_colour_correctplace < 4:
                correct_colour_wrongplace = ORANGE_check + PINK_check + GREEN_check + YELLOW_check
                print(" correct colour in correct place: " , correct_colour_correctplace)
                print(" correct colour but in wrong place: ", correct_colour_wrongplace)

# Initialize value for ALL variables below to clear the accumulation when the end-user wants to replay.
                correct_colour_correctplace = 0
                correct_colour_wrongplace = 0

                ORANGE_count = 0
                ORANGE_code = 0
                ORANGE_correct_colour_correctplace = 0

                PINK_count = 0
                PINK_code = 0
                PINK_correct_colour_correctplace = 0

                GREEN_count = 0
                GREEN_code = 0
                GREEN_correct_colour_correctplace = 0

                YELLOW_count = 0
                YELLOW_code = 0
                YELLOW_correct_colour_correctplace = 0

# Results of the end of the Master Mind Computer Game.
        if guessing_times == 1:
            print(" Congrats ! You use only 1 time to guess them correctly ! ")
            print(" You are a master mind ! " )
        elif guessing_times > 1:
            print(" Congrats ! You use ",  str(guessing_times) , " times to guess them correctly ! " )
            print(" You are now a master mind ! " )

        play = input(" Do you want to replay ? ")
        # Error Handling and Data Validation.
        while str(play) != "yes" and str(play) != "no" :
            print(" <Enter only yes or no> ")
            play = input(" Do you want to replay ? ")
    print(" See you next time ! Thank you for playing! ")

# End the mastermind program if the user input is equal to "no".
elif str(play) == "no":
    print(" See you next time ! ")




        
   

  
 























        
    


             
            
    
    
 
    
    
    
    

       
        




    
    







        
