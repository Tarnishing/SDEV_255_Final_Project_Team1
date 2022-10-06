import save_load_manager as save_load
import zork_functions as fun
import zork_objects as obj

save_load_manager = save_load.save_game_data(".dat", "save_data")

# Load class function
items, room_num, progress = save_load_manager.load_game_data(["items", "room_num", "progress"], [[], 0, 0])

for event in # module.event.get():
    if event.type == # save_btn.click:
        # Save class function
        save_load_manager.save_game_data([items, room_num, progress], ["items", "room_num", "progress"])

# intro statment
print(fun.intro())

# get input to create player
pname = input("What is your name? ")
player = obj.Player(pname)

# let the user know whats going on
fun.player_instructions(pname)

fun.view_instructions()

# Begin the actual game play
fun.start_game()