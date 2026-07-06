import random

CARD_OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A1", "A2"]


def card_value(card):
    if card in {"J", "Q", "K", "10"}:
        return 10
    if card == "A1":
        return 1
    if card == "A2":
        return 11
    return int(card)


def draw_card():
    return random.choice(CARD_OPTIONS)


def prompt_enter_or_quit(prompt_text):
    
    while True:
        choice = input(prompt_text).strip()
        if choice.lower() == "q":
            return "quit"
        if choice == "":
            return "enter"
        print("Invalid input. Press Enter to continue or type Q to quit.")


def prompt_stop_or_quit(prompt_text):
    while True:
        choice = input(prompt_text).strip()
        if choice.lower() == "q":
            return "quit"
        if choice.lower() == "s":
            return "stop"
        if choice == "":
            return "enter"
        print("Invalid input. Press Enter for another card, S to stop, or Q to quit.")


def prompt_play_again():
    while True:
        choice = input("Play again? Type Y for yes, any other key to exit: ").strip()
        if choice.lower() == "y":
            return True
        return False


def show_totals(user_total, computer_total):
    print(f"Your total: {user_total}")
    print(f"Computer total: {computer_total}")


def play_blackjack():
    while True:
        print("\nWelcome to Blackjack! Press Enter to play or type Q to quit.")
        first_choice = prompt_enter_or_quit("Your choice: ")
        if first_choice == "quit":
            print("Goodbye!")
            break

        user_cards = []
        computer_cards = []
        user_total = 0
        computer_total = 0

        user_card = draw_card()
        user_cards.append(user_card)
        user_total += card_value(user_card)
        print(f"You drew: {user_card}. Your total is {user_total}.")

        computer_card = draw_card()
        computer_cards.append(computer_card)
        computer_total += card_value(computer_card)
        print(f"Computer drew: {computer_card}. Computer total is {computer_total}.")

        if user_total == 21:
            print("YOU WIN")
            if prompt_play_again():
                continue
            break

        if computer_total == 21:
            show_totals(user_total, computer_total)
            print("You lose - House wins!")
            if prompt_play_again():
                continue
            break

        choice = prompt_stop_or_quit("Press Enter to draw another card, S to stop, or Q to quit: ")
        if choice == "quit":
            print("Goodbye!")
            return
        if choice == "enter":
            new_card = draw_card()
            user_cards.append(new_card)
            user_total += card_value(new_card)
            print(f"You drew: {new_card}. Your total is {user_total}.")

            if user_total == 21:
                print("YOU WIN")
                if prompt_play_again():
                    continue
                break
            if user_total > 21:
                print(f"Your total: {user_total}. BUST - House Wins - Game Over.")
                if prompt_play_again():
                    continue
                break

            computer_card = draw_card()
            computer_cards.append(computer_card)
            computer_total += card_value(computer_card)
            print(f"Computer drew: {computer_card}. Computer total is {computer_total}.")

            if computer_total == 21:
                show_totals(user_total, computer_total)
                print("House Wins")
                if prompt_play_again():
                    continue
                break
            if computer_total > 21:
                show_totals(user_total, computer_total)
                print("Computer Busts. You Win!")
                if prompt_play_again():
                    continue
                break

        show_totals(user_total, computer_total)

        while True:
            if user_total == 21:
                print("YOU WIN")
                break
            if user_total > 21:
                print(f"Your total: {user_total}. BUST - House Wins - Game Over.")
                break

            action = prompt_stop_or_quit("Would you like another card? Press Enter for yes, S to stop, or Q to quit: ")
            if action == "quit":
                print("Goodbye!")
                return
            if action == "stop":
                break

            new_card = draw_card()
            user_cards.append(new_card)
            user_total += card_value(new_card)
            print(f"You drew: {new_card}. Your total is {user_total}.")

            if user_total == 21:
                print("YOU WIN")
                break
            if user_total > 21:
                print(f"Your total: {user_total}. BUST - House Wins - Game Over.")
                break
            show_totals(user_total, computer_total)
            continue

        if user_total == 21:
            if prompt_play_again():
                continue
            break

        if user_total > 21:
            if prompt_play_again():
                continue
            break

        while True:
            if computer_total > user_total and computer_total <= 21:
                show_totals(user_total, computer_total)
                print("House Wins")
                break
            if computer_total == 21:
                show_totals(user_total, computer_total)
                print("House Wins")
                break
            if computer_total > 21:
                show_totals(user_total, computer_total)
                print("Computer Busts. You Win!")
                break

            new_card = draw_card()
            computer_cards.append(new_card)
            computer_total += card_value(new_card)
            print(f"Computer drew: {new_card}. Computer total is {computer_total}.")
            continue

        if prompt_play_again():
            continue
        break


if __name__ == "__main__":
    play_blackjack()
    
