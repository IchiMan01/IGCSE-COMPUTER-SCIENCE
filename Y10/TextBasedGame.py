global inventory
inventory = []

import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def gameover():
    print("""
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼""")
    exit()


def inventoryfunc():
    print("====INVENTORY====")
    for i in range(len(inventory)):
        print(">", inventory[i])


def user_input():
    choice = input("")
    if choice.capitalize() == "Inventory" or choice.capitalize() == "I":
        inventoryfunc()
        return choice
    else:
        return choice

def start():
    print("You wake up from your slumber...")
    print("Where are you? Why can't you remember anything?")
    print("Do you want to get out of bed? ")
    choice = user_input()
    if choice.capitalize() == "Yes":
        print("Let's save the world, shall we?")
    else:
        print("Well, not like you have a choice anyways... Get moving!")

def chest():
    print(
        ".\n.\n.\nYou walk out of the room and wander around the castle carelessly...\nYou found a suspicious chest!")
    print("Would you like to examine the chest? (Yes/No)")
    choice = user_input()
    while choice.capitalize() != "Yes" and choice.capitalize() != "No":
        choice = input("Yes/No: ")
    if choice.capitalize() == "Yes":
        print("You found the Excalibur, the legendary sword of King Arthur!")
        print("Item is stored within your inventory!")
        inventory.append("Excalibur")
        print("You continue and walke to the throne room...")
    elif choice.capitalize() == "No":
        print("You ignore the suspicious chest and walk to the throne room...")

def kingschallenge():
    print(".\n.\n.\nYou enter the throne room and is greeted by rows of marvelous knights.  ")
    print("Knight: Huuuuuuuh? This weak looking man is THE hero that is destined to defeat the demon lord?"
          "\nYour majesty, please let me take care of him!")
    print("What will you do? (Talk/Fight) ")
    choice = user_input()
    while choice.capitalize() != "Talk" and choice.capitalize() != "Fight":
        choice = input("Talk/Fight: ")
    if choice.capitalize() == "Talk":
        print("The knight ignores you and stabs you through your heart!")
        print(
            "King: Hmmm... This guy isn't even worth being called a hero! How pathetic! Get him out of my sight and "
            "summon another one!")
        gameover()
    elif choice.capitalize() == "Fight":
        if inventory.count("Excalibur") > 0:
            print("You take out the Excalibur and slash through him into two!")
            print(
                "King: Worth it indeed! Take 100 gold coin and use it as the travel expense to the great archmage "
                "tower!")
            inventory.append("100 coins")
        elif inventory.count("Excalibur") == 0:
            print("You don't have a weapon with you, yet you charge forward but is stabbed through the heart!")
            gameover()

def scenario1():
    print(".\n.\n.\nNext to you, you spotted a priest kneeling next to you...")
    print("Priest: You finally wake up, sir Hero; you were in a slumber for a whole week!")
    print("Priest: We almost thought of dispos- Uhhh... I mean ask for help from the archmage!")
    print("What do you want to do? (Ignore/Ask) ")
    choice = user_input()
    while choice.capitalize() != "Ignore" and choice.capitalize() != "Ask":
        choice = input("Ignore/Ask: ")
    if choice.capitalize() == "Ignore":
        chest()
        kingschallenge()
    elif choice.capitalize() == "Ask":
        print(
            "Priest: This is a world, where outlanders like Sir Hero call a fantasy world! You were summoned here to "
            "\ndefeat the demon lord "
            "and save people in this world. Before you can go out, though, you have to pass the king's challenge "
            "first! "
            "\nThe king challenge can be completed by defeating the knight. That's all I can tell you! Good luck!")
        chest()
        kingschallenge()


def merchant():
    print(".\n.\n.\nOn your way there, a merchant approachs you menacingly..."
          "\nMerchant: Hey! Young man, would you like to buy this Roasted Dragon Meat for 100 coins? (Buy/Ignore) ")
    print("Hint: Check your inventory!")
    choice = user_input()
    while choice.capitalize() != "Buy" and choice.capitalize() != "Ignore":
        choice = input("Buy/Ignore: ")
    if choice.capitalize() == "Buy":
        if inventory.count("100 coins") > 0:
            print("You spend 100 coins on Roasted Dragon Meat!")
            print("100 coins is removed from your inventory!")
            print("Roasted Dragon Meat is added to your inventory!")
            inventory.append("Roasted Dragon Meat")
            inventory.remove("100 coins")
            inventoryfunc()
        elif inventory.count("100 coins") <= 0:
            print("You don't have the 100 coins with you!")
            print("The merchant spits at you then walked away...")
        print("You carry on your journey. However, when you look back, he disappears without a trace!")
    elif choice.capitalize() == "Ignore":
        print("You walk past the wandering merchant. However, when you look back, he disappears without a trace!")

def slime():
    print(
        ".\n.\n.\nAfter several hours of walking, you encounter yet another bizarre creature - A Talking Slime!"
        "\nSlime: You impertinent human! I'm hungry so feed me something!"
        "\nYou: What the- Hey can't you speak politely to someone who you just met?"
        "\nSlime: I AM THE EMPEROR OF ALL MONSTER! I DON'T CARE! GIVE ME FOOD!!!"
        "\nWhat would you like to do? (Ignore/Feed/Kill)")
    choice = user_input()
    while choice.capitalize() != "Ignore" and choice.capitalize() != "Feed" and choice.capitalize() != "Kill":
        choice = input("Ignore/Feed/Kill: ")
    if choice.capitalize() == "Ignore":
        print("The slime is angered by your ignorance and engulfs you!")
        gameover()
    elif choice.capitalize() == "Feed":
        if inventory.count("Roasted Dragon Meat") > 0:
            print("You give the self-proclaimed Emperor of all monster Roasted Dragon Meat!")
            print("Roasted Dragon Meat is removed from your inventory!")
            inventory.remove("Roasted Dragon Meat")
            print(
                    "The arrogant slime quickly engulfs the precious Dragon Meat..."
                    "Slime: I shall return you the favour!"
                    "Suddenly, the slime spit a holy item - The Missing Holy Armour!"
                    "The slime expresses his gratitude one more time before leaping into the unknown..."
                    "Holy Armour is added into your inventory")
            inventory.append("Holy Armour")
            inventoryfunc()
        elif inventory.count("Roasted Dragon Meat") <= 0:
            print("The Roasted Dragon Meat isn't in you inventory")
            print("The monster emperor is enraged by your lies! It crushes you with its body!")
            gameover()
    elif choice.capitalize() == "Kill":
        print(
            "You draw out Excalibur but before you could react, the slime spits an acidic substance at you, "
            "leaving you to melt and die pathetically")
        gameover()

def archmage():
    print(".\n.\n.\nAn elderly man stepped out of the tower...")
    print("Dee Z. Nuts: Are you the rumored hero, young man? It seems that you are more that qualified to take my blessing!"
          "\nThe legendary archmage soon casts his spells and give you unimaginable strength!")
    print(".\n.\n.\nHowever, after he finishes casting his spell, the archmage collapse to the ground and his body seems to"
          "\ndisintegrate into dust...")
    print("Dee Z. Nuts: Subjugate the demon lord... Don't let my sacrifice be in vai-")
    print("Before he can even finish his sentence, Dee Z. Nuts dissolved into the surrounding air..."
          "\nIt seems that the great archmage transferred all his power to you, betting his life that you can defeat the demon lord!")
    print("Although you had barely talked to the man, you intend to carry on his legacy. Thus, you used your newly acquired"
          "\nmagic power to fly over the continent.")

def scenario2():
    print(
        "You begin your journey to the archmage tower. According to the priest, Sir Dee Z. Nuts, the archmage, "
        "is the strongest mage in the whole continent. ")
    merchant()
    print("That doesn't stop you as you continue to your adventure courageously.")
    slime()
    print("Suddenly, a magic tower appeared out of thin air!")
    archmage()


def scenario3():
    print(".\n.\n.\nYou travel over the sky of countless countries eventually reach the corrupted land of Helheim")
    print("The demon lord is sitting on its throne while glancing at you!")
    print("Demon lord: Incompetent beings like you deserve to die... Now perish!!")
    print("The demon lord fires several fireballs at you!"
          "\n What will you do? (Block/Dodge)")
    choice = user_input()
    while choice.capitalize() != "Block" and choice.capitalize() != "Dodge":
        choice = input("Block/Dodge: ")
    if choice.capitalize() == "Block":
        print("You successfully block the demon lord's attack with Excalibur")
    elif choice.capitalize() == "Dodge":
        print("You failed to dodge the fireball attack!"
              "\nThe eternal flame burn you to death")
        gameover()
    print("With the power of friendship from the people you met along your journey, you slashes through the demon lord"
          "\n cutting him perfectly in half!")
    print("With that attack, you defeated the demon lord and turns him into grains of sand...")
    print(".\n.\n.\nWith this your story about your legendary encounter with the demon lord circulated through the continents"
          "\n and will forever be remembered by the people!")
    delay_print(".\n.\n.\nThe end?")

# Main Game
start()
scenario1()
scenario2()
scenario3()
