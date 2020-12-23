# Class for animation objects
class Animation:
    def __init__(self, name, id, file_path):
        self.name = name
        self.id = id
        self.file_path = file_path + name + "/"
        self.frames = []

        for i in range(len(os.listdir(self.file_path))):
            iter_path = self.file_path + str(i)
            print(iter_path)
            with open(iter_path, "r", encoding="utf8") as f:
                #sabe every line in list "f"
                f = f.readlines()
                #append list f to list frames
                self.frames.append(f)
