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

### Demo Run (200 Char)
![image](https://user-images.githubusercontent.com/87340855/220170260-afd8828c-9f41-49c4-a212-069d17e4c717.png)

### Demo Run (500 Char)
![image](https://user-images.githubusercontent.com/87340855/220170654-d85653cc-da76-43b6-995a-fbcf078acbd7.png)

### Line Completely Generated
![image](https://user-images.githubusercontent.com/87340855/220170805-51f60ef5-6786-40cb-89d0-cc8de9f1fbd9.png)

## References
- https://arxiv.org/abs/1706.03762
