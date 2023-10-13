# Cutebot

Simple chatbot using OpenAI's GPT-3.5 Turbo API for use on terminals and TTYs. It is meant to be used for quick references and small tasks, big tasks might take forever to fetch or sometimes not possible because of token limit.

## Screenshot

![Chatbot Screenshot](https://github.com/msrsaditya/cutebot/blob/main/cutebot.png)

## Goals

- Use the Best Free OpenAI API Model
- Make it as simple as possible and make it available for use on Terminals/TTYs
- Yep, that's it! 

## Prerequisites

- Python and pip should be installed and updated to the latest version.

```shell
pip3 install openai colorama
```

## Usage

1. Clone this repository and navigate into it

```shell
git clone https://github.com/msrsaditya/cutebot
```

```shell
cd /path/to/cutebot
```

2. Open `cutebot.py` and replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key obtained from [here](https://platform.openai.com/account/api-keys).

3. Now, Run the program

```
python3 cutebot.py
```

**Note:**
- Terminal colors may not display as intended due to differences in terminal color support.
- You can type "exit" to exit out of the program, optionally you can SIGINT using ctrl+c or corresponding shortcut on your terminal.
- Arrow keys (up, down) to move between prompts and arrow keys (left, right) to move between words in prompts are not working and maybe fixed in future.
