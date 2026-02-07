# Screen Position / Resolution

Small Python tools that report your primary monitor’s resolution and total pixel count using [screeninfo](https://github.com/rr-/screeninfo).

## What it does

- Detects the first (primary) monitor’s width and height in pixels  
- Prints width, height, and total pixels (width × height)

## Requirements

- Python 3.x  
- [screeninfo](https://github.com/rr-/screeninfo) (listed in `requirements.txt`)

## Setup

```bash
git clone https://github.com/alwayschangingusernames/screen_wxh.git
cd screen_wxh
pip install -r requirements.txt
```

## Usage

Run the script; it will install dependencies from `requirements.txt` if needed, then print the resolution info.

**screen_wxh.py**

```bash
python screen_wxh.py
```

Example output:

```
Screen Width: 1920
Screen Height: 1080
Total Pixels: 2073600
```

## License


Use and modify as you like.
