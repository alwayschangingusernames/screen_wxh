## Install dependencies from requirements.txt
import subprocess
import sys
def main():

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    import screeninfo
    from screeninfo import get_monitors

    # Get the first monitor's resolution
    monitor = get_monitors()[0]  # Get the first monitor, you can loop for multiple monitors

    width = monitor.width
    height = monitor.height

    # Calculate total pixels
    total_pixels = width * height

    print(f"Screen Width: {width}")
    print(f"Screen Height: {height}")
    print(f"Total Pixels: {total_pixels}")

## Run if error occurs, run again
if __name__ == "__main__":
    main()