import zork_objects as obj
from js import document
# supress FutureWarning of deprecated feature from pyodide
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from pyodide import create_proxy

progress = 0

en = obj.Enemy()
men = obj.ModerateEnemy()
den = obj.DifficultEnemy()

def travel_1(loc, pname):
    global en
    global men
    global den

    if loc == 'nw':
        building = 'a1'
        Element("direction").write("You travel northwest...")
        Element("important").write("ENEMY SPOTTED!")
        Element("enemy").write(f"&emsp;<b><i>{en.name}</i></b>")
        Element("rank").write(f"&emsp;&emsp;{en.rank}")
        Element("message").write("")
        Element("prompt").write("&gt;&nbsp;&gt;&nbsp; Will you attack or flee?")
        # answer = validate_encounter_input()
        # attack_or_flee(answer, pname, en, loc)
        # arrive_to_building(pname, building)
    elif loc == 'n':
        building = 'a2'
        Element("direction").write("You travel north...")
        Element("important").write("ENEMY SPOTTED!")
        Element("enemy").write(f"&emsp;<b><i>{en.name}</i></b>")
        Element("rank").write(f"&emsp;&emsp;{en.rank}")
        Element("message").write("")
        Element("prompt").write("&gt;&nbsp;&gt;&nbsp; Will you attack or flee?")
        # answer = validate_encounter_input()
        # attack_or_flee(answer, pname, en, loc)
        # arrive_to_building(pname, building)
    elif loc == 'ne':
        building = 'a3'
        Element("direction").write("You travel northeast...")
        Element("enemy").write(f"&emsp;<b><i>{en.name}</i></b>")
        Element("rank").write(f"&emsp;&emsp;{en.rank}")
        Element("message").write("")
        Element("prompt").write("&gt;&nbsp;&gt;&nbsp; Will you attack or flee?")
        # answer = validate_encounter_input()
        # attack_or_flee(answer, pname, en, loc)
        # arrive_to_building(pname, building)
    else:
        Element("notify").write("&gt;&nbsp; Command is invalid. Try again. &nbsp;&lt;")

def arrive_to_building(pname, building):
    if building == 'a1':
        print("your arrived to a1")
    elif building == 'a2':
        print('you arrived to a2')
    elif building == 'a3':
        print('you arrived to a3')

    pass

# def validate_encounter_input(text):
#     global encounter_ans

#     encounter_ans = text.casefold()

#     if encounter_ans == 'attack' or 'a':
#         encounter_ans = encounter_ans.strip('ttack')
#         Element("test").write(f"{encounter_ans}")
#     elif encounter_ans == 'flee' or 'f':
#         encounter_ans = encounter_ans.strip('lee')
#     else:
#         Element("notify").write("&gt;&nbsp; Command is invalid. Try again. &nbsp;&lt;")

def attack_or_flee(text):

    if text == 'a':
        Element("direction").write("")
        Element("important").write("")
        Element("enemy").write("")
        ELement("rank").write("")
        Element("message").write(f"You killed the {en.name}!<br>There is now damage to your radiation suit.")
        enemy_damage(name, en)
    elif text == 'f':
        Element("direction").write("")
        Element("important").write("")
        Element("enemy").write("")
        ELement("rank").write("")
        Element("message").write(f"You decided that fighting {en.name} wasn't worth the risk, and so you return to your bio-pod.")
        Element("prompt").write("Which direction do you want to go now?")
        # direc = input("What direction do you want to travel?")
        # travel_1(direc, name)

# subtracts from player health a set ineger of enemy class
def enemy_damage(pname, en):
    en = obj.Enemy()
    player = obj.Player(pname)
    player.health = int(player.health) - int(en.damage)
    print(player.name, ', your health is at', player.health, 'points.')

def game_progress(e):
    global progress
    global text

    inp = Element('prompt-input').element
    text = inp.value
    progress += 1
    Element("test").write(f"{progress}")
    inp.value = ""

    Element("horizontal-div").write("_ __ ___ ____ _____ ______________________________________________ _____ ____ ___ __ _")

    if progress == 1:
        Element("important").write("")

        # intro statment
        Element("message").write('\"Year 2069, 6 years after the Betelgeuse Star went Supernova. In just seconds, the gamma rays wiped out 80% of life on earth. Few survived the initial flash, and less survived the radiation that pollutes the Earth now. Radiation is the leading cause of death for the remaining few. You are on a mission to travel to a hidden underground vault to find a special plant, the Chelsea-Wax Plant, to create a cure to suppress and combat the radiation sickness of the few remaining people. You may be humanity\'s final hope at survival.\"')

        Element("prompt").write("&gt;&nbsp&gt;&nbsp; What is your name?")

    elif progress == 2:
        global name

        Element("message").write(f"Welcome, {text}. You are on a mission to search for a hidden underground vault the goverment used to store seeds of all the plants known. Scientists have determined the rare Chelsea plant is needed to stop radiation sickness. It is up to you to search the barren wasteland for this vault. It will be dangerous and you may die. Travel looking for clues as to where the vault is and keep yourself safe along the way. Mankind depends on you!")

        Element("prompt").write("&gt;&nbsp;&gt;&nbsp; Would you like to view the instructions on how to play?")

        name = obj.Player(text)
        return name

    # elif progress == 3 and text == "n":
    #     progress += 1
    #     Element("message").write("You just woke up in your radiation proof bio-pod headquarters.<br><br>You had traveled from a small community from the south and there is nothing back there for you unless you retrieve the special Chelsea-Wax plant.")
    #     Element("prompt").write("&gt;&nbsp;&gt;&nbsp; You have the option to travel Northwest (nw), North (n), or Northeast (ne).")
    #     Element("test").write(f"{progress}")

    # elif progress == 3:
    #     if text != "" and text != "n":
    #         Element("important").write("INSTRUCTIONS:<br>")
    #         Element("message").write("' i ' . . .  Check inventory<br>' h ' . . .  Health<br>' c ' . . .  Armor<br>' nw ' . . .  Go Northwest<br>' n ' . . .  Go North<br>' ne ' . . .  Go Northeast<br><br><b>When encountering enemies:</b><br>' a ' . . .  Attack<br>' f ' . . .  Flee")

    #         Element("prompt").write("<h3 align='center'>&gt;&nbsp; Press 'Enter' to proceed &nbsp;&lt;</h3>")

    elif progress == 3:
        Element("message").write("You just woke up in your radiation proof bio-pod headquarters.<br><br>You had traveled from a small community from the south and there is nothing back there for you except to retrieve the special Chelsea-Wax plant.")
        Element("prompt").write("&gt;&nbsp;&gt;&nbsp; You have the option to travel Northwest (nw), North (n), or Northeast (ne).")

    elif progress == 4:
        travel_1(text, obj.Player)

    # progress == 5 is skipped because it is travel_1()

    elif progress == 6:
        attack_or_flee(text)

    elif progress == 7:
        Element("message").write("Progress at 7")


    else:
        pass

    proxy = create_proxy(game_progress)
    confirm_button = document.getElementById("confirm-btn")
    confirm_button.addEventListener("click", proxy)

if __name__ == "__main__":
    game_progress(progress)