class DataLoader():
    def __init__(self, data_path) -> None:
        super().__init__()
        self.dataPath = data_path
        self.text = self.load()
    
    def load(self):
        # Read Dataset
        text = ''
        with open(self.dataPath, encoding="utf8") as f:
            text = f.read()

        # Get unique characters sorted
        self.chars = sorted(set(text))
        self.vocabSize = len(self.chars)
        print("Available Char: \n",''.join(self.chars))

        return text