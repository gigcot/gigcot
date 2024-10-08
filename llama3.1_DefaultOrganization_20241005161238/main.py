# main.py
'''
Main entry point for the dice rolling game application.
'''
import dice
def roll_dice(dice_count=1):
    # Add input validation for dice count
    if not isinstance(dice_count, int) or dice_count <= 0:
        raise ValueError("Invalid dice count")
    import random
    die = dice.Dice()
    die.roll()
    if dice_count == 1:
        return die.result
    else:
        return [die.result for _ in range(dice_count)]
def main():
    while True:
        print("\nDice Rolling Game Menu:")
        print("1. Roll Dice")
        print("2. Add Player Roll")
        print("3. Calculate Sum")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            dice_count = int(input("Enter dice count (default=1): ") or 1)
            result = roll_dice(dice_count)
            print(f"Dice result: {result}")
        elif choice == "2":
            # Implement player roll addition and validation
            player_roll = input("Enter roll value (space-separated, e.g., '3 4'): ")
            try:
                rolls = [int(x) for x in player_roll.split()]
                if len(rolls) < 1 or any(x <= 0 for x in rolls):
                    raise ValueError("Invalid roll values")
                player.add_rolls(rolls)
                print(f"Added player roll: {rolls}")
            except ValueError as e:
                print(e)
        elif choice == "3":
            # Calculate sum for existing rolls
            try:
                total = player.calculate_sum()
                print(f"Player's current sum: {total}")
            except AttributeError:
                print("No rolls added yet.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")
if __name__ == "__main__":
    global player
    player = dice.Player()
    main()