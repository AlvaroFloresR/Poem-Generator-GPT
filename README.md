# Poem Generator GPT
GPT Poem Generator


## Highlights
- Trained with poem verses from 20 categories
- PyTorch based
- Based on the paper "Attention Is All You Need"
- Simple Tokenization with ints for the following chars:

``` !'(),-.01238:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]`abcdefghijklmnopqrstuvwxyz  –—‘’“”…```

## Potential Improvements
- TikToken implementation (better speeds for bigger datasets) - https://github.com/openai/tiktoken
- Train based on poem categories (Haiku, romantic, etc.)
- Deploy on web-server as an online app

## How to run
1. Clone repo
2. Include dataset `big_dataset.txt` in `./data/` directory 
3. Download pre-trained weights and add in root folder (`model.pth` too heavy, can be shared upon request)

## Demo Images

