import pickle
import os

class Save:
    def __init__(self, file_ext, save_folder):
        self.file_ext = file_ext
        self.save_folder = save_folder

    def save_data(self, data, name):
        data_file = open(self.save_folder + "/" + name + self.file_ext, "wb")
        pickle.dump(data, data_file)
    
    def save_game_data(self, data_to_save, file_names):
        for index, file in enumerate(data_to_save):
            self.save_data(file, file_names[index])

class Load:
    def __init__(self, file_ext, save_folder):
        self.file_ext = file_ext
        self.save_folder = save_folder
    
    def load_data(self, name):
        data_file = open(self.save_folder + "/" + name + self.file_ext, "rb")
        data = pickle.load(data_file)
        return data

    def check_for_save(self, name):
        return os.path.exists(self.save_folder + "/" + name + self.file_ext)

    def load_game_data(self, files_to_load, default_data):
        variables = []
        for index, file in enumerate(files_to_load):
            if self.check_for_save(file):
                variables.append(self.load_data(file))
            else:
                variables.append(default_data[index])

        if len(variables) > 1:
            return tuple(variables)
        else:
            return variables[0]