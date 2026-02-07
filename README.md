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
git clone https://github.com/YOUR_USERNAME/screen_pos.git
cd screen_pos
pip install -r requirements.txt
```

## Usage

Run either script; it will install dependencies from `requirements.txt` if needed, then print the resolution info.

**screen_pos_calc.py**

```bash
python screen_pos_calc.py
```

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