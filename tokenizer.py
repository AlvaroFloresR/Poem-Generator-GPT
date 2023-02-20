class Token():
    def __init__(self, chars_input) -> None:
        super().__init__()
        self.chars = chars_input
        self.encoder, self.decoder = self.generate_tokenizer()

    def generate_tokenizer(self):
        # Dict as lookup table for coder/decoder
        #TODO: Implement Tiktoken: https://github.com/openai/tiktoken
        stoi = {ch:i for i,ch in enumerate(self.chars)}
        itos = {i:ch for i,ch in enumerate(self.chars)}

        # Encode based on dictionary stoi
        encode = lambda s: [stoi[c] for c in s]
        # Decode based on dictionary itos
        decode = lambda l: ''.join([itos[i] for i in l])

        return encode, decode     

