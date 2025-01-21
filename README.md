# Pepper Chat

This a Vertically Integrated Project for Sustainable Development in University of Strathclyde on the Pepper Robot.  
We wanted to make Pepper into a shopping assistant who can chat with the customer using OpenAI's GPT, direct them to products and more.

## Important Files

### `move.py`

This file opens a shell that allows the user to move pepper and its joints as they wish using simple `WASD` commands.

### `setLocations.py`

This file when run can be used to set a `home` location and other named locations which can later be asked to navigate to during the conversation with the customer.

## Usage

First create a `keys.txt` file and save your OpenAI API Key in the file in the format:

```shell
OpenAIKey=<enter key here>
```

Create necessary folders.  
Then run the `main.py`.

```shell
mkdir maps
mkdir recordings
python main.py
```
