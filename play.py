import game

welcome_note = '''
    READ THE INSTRUCTIONS BEFORE STARTING THE GAME

    Welcome to this question and answer game. It promises to be fun for the players. In this game, there are levels
    1-3. When you start the game, you are prompted to choose a level. Level 0 is the easiest, it presents you with
    3 questions which you must answer correctly. Each question has 5 marks. Level 1 has 6 questions and level 2 has
    10 questions. After selecting your level, you can choose to play the game on auto mode. The total number of 
    questions are presented to you randomly. If you fail a question, the game ends. Your input must be in text.
    If you input numbers, the game ends automatically.

    N.B: Game levels can only be accessed on auto mode.
    Now that you have read the instructions, start playing

'''

game_mode = ["Auto", "Manual"]
game_mode_selector = 0

stop_game = 0


print("Do you want to start the game?")
start_game_response = input("Response: ")
start_game = False

if start_game_response == 'yes':
    start_game = True

if start_game_response == 'no':
    start_game = False

if start_game:
    print(welcome_note)
    while start_game:
        game_mode_selector = int(input("Choose a mode: "))

        if game_mode_selector == 0:
            game_mode_selector = 0
            while game_mode_selector == 0:
                print(f"You have selected {game_mode[game_mode_selector]} mode")
                game.auto_mode()
                break

        if game_mode_selector == 1:
            game_mode_selector = 1
            while game_mode_selector == 1:
                print(f"You have selected {game_mode[game_mode_selector]} mode")
                game.manual_mode()
                break


        if game_mode_selector == 2:
            start_game = False
            break