#game modes

game_questions = [
                    "What owns Tesla?",
                    "What owns Facebook and WhatsApp?",
                    "When did World War 1 start?",
                    "When did Nigeria gain Independence?",
                    "Who Is Nigeria's current President?",
                    "What is 1 + 1?",
                    "Calculate 5 x 25:",
                    "What is the speed of light?",
                    "Who is the CEO of google?",
                    "What happens when an unstoppable force meets an immovable object?"
                ]

game_answers = [
                    "Elon Musk",
                    "Mark Zuckerberg",
                    "October 1, 1914",
                    "October 1, 1960",
                    "President Mohammadu Buhari",
                    "2",
                    "125",
                    "300000000m/s",
                    "Sundar Pichai",
                    "Nothing"
            ]
# print(game_questions[0])
# print(game_answers.index('Elon Musk'))
# provided_answer = game_answers.index(response)

points = 0
is_answer_correct = False

def auto_mode():
    level_one_selected = False
    level_two_selected = False
    level_three_selected = False

    choose_level = int(input("Choose a level between 0 - 2: "))

    if choose_level == 0:
        level_one_selected = True
        print("Level 1 Selected")

        if level_one_selected:
            for question in game_questions[:3]:
                while question == game_questions[0]:
                    response = input(question + " ")
                    if response == game_answers[0]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_one = points + 5
                            print(f"You got {res_one} for giving the correct answer")
                            break
                    elif response != game_answers[0]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_one = points - 2
                            print(f"You lost {res_one} for giving the wrong answer")
                            break

                while question == game_questions[1]:
                    response = input(question + " ")
                    if response == game_answers[1]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_two = points + 5
                            print(
                                f"You got {res_two} for giving the wrong answer")
                            break
                    elif response != game_answers[1]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_two = points - 2
                            print(
                                f"You lost {res_two} for giving the wrong answer")
                            break

                while question == game_questions[2]:
                    response = input(question + " ")
                    if response == game_answers[2]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_three = points + 5
                            print(f"You got {res_three} for giving the correct answer")
                            break

                    elif response != game_answers[2]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_three = points - 2
                            print(f"You lost {res_three} for giving the wrong answer")
                            break

            total_res = res_one + res_two + res_three

            print(f"You scored {total_res} for this level. Start game again")

    if choose_level == 1:
        level_two_selected = True
        print("Level 2 Selected")

        if level_two_selected:
            for question in game_questions[:5]:
                while question == game_questions[0]:
                    response = input(question + " ")
                    if response == game_answers[0]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_one = points + 5
                            print(f"You got {res_one} for giving the correct answer")
                            break

                    elif response != game_answers[0]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_one = points - 2
                            print(
                                f"You lost {res_one} for giving the wrong answer")
                            break

                while question == game_questions[1]:
                    response = input(question + " ")
                    if response == game_answers[1]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_two = points + 5
                            print(
                                f"You got {res_two} for giving the correct answer")
                            break
                    elif response != game_answers[1]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_two = points - 2
                            print(
                                f"You lost {res_two} for giving the correct answer")
                            break

                while question == game_questions[2]:
                    response = input(question + " ")
                    if response == game_answers[2]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_three = points + 5
                            print(
                                f"You got {res_three} for giving the correct answer")
                            break

                    elif response != game_answers[2]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_three = points - 2
                            print(
                                f"You lost {res_three} for giving the correct answer")
                            break

                while question == game_questions[3]:
                    response = input(question + " ")
                    if response == game_answers[3]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_four = points + 5
                            print(
                                f"You got {res_four} for giving the correct answer")
                            break

                    elif response != game_answers[3]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_four = points - 2
                            print(
                                f"You lost {res_four} for giving the correct answer")
                            break

                while question == game_questions[4]:
                    response = input(question + " ")
                    if response == game_answers[4]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_five = points + 5
                            print(
                                f"You got {res_five} for giving the correct answer")
                            break

                    elif response != game_answers[4]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_five = points - 2
                            print(
                                f"You lost {res_five} for giving the correct answer")
                            break

        total_res = res_one + res_two + res_three + res_four + res_five

        print(f"You scored {total_res} for this level. Start game again")
        total_res = 0

    if choose_level == 2:
        level_three_selected = True
        print("Level 3 Selected")

        if level_three_selected:
            for question in game_questions[:]:
                while question == game_questions[0]:
                    response = input(question + " ")
                    if response == game_answers[0]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_one = points + 5
                            print(f"You got {res_one} for giving the correct answer")
                            break

                    elif response != game_answers[0]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_one = points - 2
                            print(
                                f"You lost {res_one} for giving the wrong answer")
                            break

                while question == game_questions[1]:
                    response = input(question + " ")
                    if response == game_answers[1]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_two = points + 5
                            print(
                                f"You got {res_two} for giving the correct answer")
                            break
                    elif response != game_answers[1]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_two = points - 2
                            print(
                                f"You lost {res_two} for giving the correct answer")
                            break

                while question == game_questions[2]:
                    response = input(question + " ")
                    if response == game_answers[2]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_three = points + 5
                            print(
                                f"You got {res_three} for giving the correct answer")
                            break

                    elif response != game_answers[2]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_three = points - 2
                            print(
                                f"You lost {res_three} for giving the correct answer")
                            break

                while question == game_questions[3]:
                    response = input(question + " ")
                    if response == game_answers[3]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_four = points + 5
                            print(
                                f"You got {res_four} for giving the correct answer")
                            break

                    elif response != game_answers[3]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_four = points - 2
                            print(
                                f"You lost {res_four} for giving the correct answer")
                            break

                while question == game_questions[4]:
                    response = input(question + " ")
                    if response == game_answers[4]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_five = points + 5
                            print(
                                f"You got {res_five} for giving the correct answer")
                            break

                    elif response != game_answers[4]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_five = points - 2
                            print(
                                f"You lost {res_five} for giving the correct answer")
                            break

                while question == game_questions[5]:
                    response = input(question + " ")
                    if response == game_answers[5]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_six = points + 5
                            print(
                                f"You got {res_six} for giving the correct answer")
                            break

                    elif response != game_answers[5]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_six = points - 2
                            print(
                                f"You lost {res_six} for giving the correct answer")
                            break

                while question == game_questions[6]:
                    response = input(question + " ")
                    if response == game_answers[6]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_seven = points + 5
                            print(
                                f"You got {res_seven} for giving the correct answer")
                            break

                    elif response != game_answers[6]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_seven = points - 2
                            print(
                                f"You lost {res_seven} for giving the correct answer")
                            break

                while question == game_questions[7]:
                    response = input(question + " ")
                    if response == game_answers[7]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_eight = points + 5
                            print(
                                f"You got {res_eight} for giving the correct answer")
                            break

                    elif response != game_answers[7]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_eight = points - 2
                            print(
                                f"You lost {res_eight} for giving the correct answer")
                            break

                while question == game_questions[8]:
                    response = input(question + " ")
                    if response == game_answers[8]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_nine = points + 5
                            print(
                                f"You got {res_nine} for giving the correct answer")
                            break

                    elif response != game_answers[8]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_nine = points - 2
                            print(
                                f"You lost {res_nine} for giving the correct answer")
                            break

                while question == game_questions[9]:
                    response = input(question + " ")
                    if response == game_answers[9]:
                        is_answer_correct = True
                        if is_answer_correct:
                            res_ten = points + 5
                            print(
                                f"You got {res_ten} for giving the correct answer")
                            break

                    elif response != game_answers[9]:
                        is_answer_correct = False
                        if not is_answer_correct:
                            res_ten = points - 2
                            print(
                                f"You lost {res_ten} for giving the correct answer")
                            break

        total_res = res_one + res_two + res_three + res_four + res_five + res_six + res_seven + res_eight + res_nine + res_ten

        print(f"You scored {total_res} for this level. Start game again")
        total_res = 0


def manual_mode():
    print("You have chosen manual mode")
    start_manual_mode = True
    have_user_made_choice = False
    choice_count = 0
    player_result = 0
    user_question_choice = []
    question_selected = False
    res_one = 0
    res_two = 0
    res_three = 0
    res_four = 0
    res_five = 0
    res_six = 0
    res_seven = 0
    res_eight = 0
    res_nine = 0
    res_ten = 0
    numbers = 0

    while start_manual_mode:
        user_choice = int(input("Choose a question from 1 - 10: "))
        user_choice_translate = user_choice - 1

        if user_choice in user_question_choice:
            question_selected = True
            print("You have selected this number, select a new number")

        else:
            question_selected = False
        if user_choice > 0 and not question_selected:
            choice_count = choice_count + 1

        if user_choice == 1 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[0]:
                is_answer_correct = True
                if is_answer_correct:
                    res_one = res_one + 5
                    print(f"You have {res_one} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[0]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_one = res_one - 2
                    print(
                        f"You lost {res_one} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 2 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[1]:
                is_answer_correct = True
                if is_answer_correct:
                    res_two = res_two + 5
                    print(
                        f"You have {res_two} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[1]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_two = res_two - 2
                    print(
                        f"You lost {res_two} for choosing the wrong answer. Choose another question from 1 - 10")
        
        if user_choice == 3 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[2]:
                is_answer_correct = True
                if is_answer_correct:
                    res_three = res_three + 5
                    print(
                        f"You have {res_three} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[2]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_three = res_three - 2
                    print(
                        f"You lost {res_three} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 4 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[3]:
                is_answer_correct = True
                if is_answer_correct:
                    res_four = res_four + 5
                    print(
                        f"You have {res_four} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[3]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_four = res_four - 2
                    print(
                        f"You lost {res_four} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 5 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[4]:
                is_answer_correct = True
                if is_answer_correct:
                    res_five = res_five + 5
                    print(
                        f"You have {res_five} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[4]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_five = res_five - 2
                    print(
                        f"You lost {res_five} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 6 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[5]:
                is_answer_correct = True
                if is_answer_correct:
                    res_six = res_six + 5
                    print(
                        f"You have {res_six} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[5]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_six = res_six - 2
                    print(
                        f"You lost {res_six} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 7 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[6]:
                is_answer_correct = True
                if is_answer_correct:
                    res_seven = res_seven + 5
                    print(
                        f"You have {res_seven} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[6]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_seven = res_seven - 2
                    print(
                        f"You lost {res_seven} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 8 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[7]:
                is_answer_correct = True
                if is_answer_correct:
                    res_eight = res_eight + 5
                    print(
                        f"You have {res_eight} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[7]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_eight = res_eight - 2
                    print(
                        f"You lost {res_eight} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 9 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[8]:
                is_answer_correct = True
                if is_answer_correct:
                    res_nine = res_nine + 5
                    print(
                        f"You have {res_nine} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[8]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_nine = res_nine - 2
                    print(
                        f"You lost {res_nine} for choosing the wrong answer. Choose another question from 1 - 10")

        if user_choice == 10 and not question_selected:
            user_question_choice.append(user_choice)
            print(game_questions[user_choice_translate])
            response = input("")

            if response == game_answers[9]:
                is_answer_correct = True
                if is_answer_correct:
                    res_ten = res_ten + 5
                    print(
                        f"You have {res_ten} for getting the right answer. Choose another question from 1 - 10")

            elif response != game_answers[9]:
                is_answer_correct = False
                if not is_answer_correct:
                    res_ten = res_ten - 2
                    print(
                        f"You lost {res_ten} for choosing the wrong answer. Choose another question from 1 - 10")

        player_result = res_one + res_two + res_three + res_four + res_five + res_six + res_seven + res_eight + res_nine + res_ten

        if choice_count == 10:
            print(f"You have completed the game with {player_result} points. Thank you for participating.")
            break
