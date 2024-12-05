import time

def type_text(text, delay=0.05):
    """Simulate typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    type_text("Welcome, Detective. You’ve been called to solve a high-profile crime! 🕵️‍♂️")
    type_text("A billionaire has been murdered in his mansion, and it’s your job to find the killer.")
    type_text("You’ll need to explore the scene, interrogate suspects, and gather evidence.")
    type_text("Can you solve the mystery before it’s too late? Let's begin! 🔎\n")
    time.sleep(1)

def scene():
    type_text("You arrive at the mansion. The body of Mr. Goldstein lies in the study. There are three clues:")
    type_text("1. A shattered glass near the window.\n2. A bloody knife on the desk.\n3. A torn piece of fabric caught on the doorknob.\n")
    choice = input("Which clue do you investigate first? (glass/knife/fabric): ").strip().lower()

    if choice == 'glass':
        type_text("You notice fingerprints on the glass, suggesting a struggle near the window.")
        return "glass"
    elif choice == 'knife':
        type_text("The knife has the victim’s blood, but no fingerprints. Suspicious. 🗡️")
        return "knife"
    elif choice == 'fabric':
        type_text("The fabric seems to match the jacket of one of the suspects. 🤔")
        return "fabric"
    else:
        type_text("Invalid choice. You lose precious time!")
        return None

def interrogate(clue):
    suspects = {
        "John": "The butler, calm but evasive.",
        "Anna": "The maid, visibly nervous.",
        "Mark": "The victim's business partner, confident but hostile."
    }
    type_text("\nYou gather the suspects in the lounge.")
    type_text("The suspects are:")
    for name, desc in suspects.items():
        type_text(f"- {name}: {desc}")
    type_text("\nUsing the clue you found, decide who to question first.")
    suspect = input("Who do you question? (John/Anna/Mark): ").strip().capitalize()

    if suspect == "John":
        type_text("John stutters and mentions hearing a struggle near the study.")
        if clue == "glass":
            type_text("You deduce he may have seen the killer escape through the window!")
            return "innocent"
        else:
            type_text("John’s testimony doesn’t match the evidence. You’re uncertain.")
            return "unclear"
    elif suspect == "Anna":
        type_text("Anna admits to seeing Mark near the study with a knife earlier.")
        if clue == "knife":
            type_text("Her statement corroborates with the knife clue. Mark seems suspicious! 🧐")
            return "guilty"
        else:
            type_text("Anna seems genuine, but you don’t have enough evidence.")
            return "unclear"
    elif suspect == "Mark":
        type_text("Mark denies everything and accuses Anna of planting evidence.")
        if clue == "fabric":
            type_text("The fabric matches Mark’s jacket. He’s the prime suspect! 🚨")
            return "guilty"
        else:
            type_text("Mark is defiant, and you don’t have enough to pin him down.")
            return "unclear"
    else:
        type_text("That’s not a valid suspect! You waste time and lose leads.")
        return "unclear"

def end_game(verdict):
    if verdict == "guilty":
        type_text("\nCongratulations, Detective! You solved the case and arrested the killer! 🎉👮")
    elif verdict == "innocent":
        type_text("\nThe real killer escaped while you focused on the wrong person. Case closed, but not solved. 😞")
    else:
        type_text("\nYou couldn’t gather enough evidence to solve the case. Better luck next time! 😔")

def main():
    intro()
    clue = scene()
    if clue:
        verdict = interrogate(clue)
        end_game(verdict)
    else:
        type_text("\nWithout a proper investigation, the case goes cold. 🕳️")

if __name__ == "__main__":
    main()
