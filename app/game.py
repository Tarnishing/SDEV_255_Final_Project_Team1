from save_load_manager import Save, Load

save_load_manager = Save(".dat", "save_data")

# Load class function
items, room_num, progress = save_load_manager.load_game_data(["items", "room_num", "progress"], [[], 0, 0])

for event in # module.event.get():
    if event.type == # save_btn.click:
        # Save class function
        save_load_manager.save_game_data([items, room_num, progress], ["items", "room_num", "progress"])