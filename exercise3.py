import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def show_dir(path: Path, indent=0):
    for item in path.iterdir():
        space = "  " * indent
        if item.is_dir():
            print(f"{space}{Fore.BLUE}{item.name}/{Fore.RESET}")
            show_dir(item, indent + 1)
        else:
            print(f"{space}{Fore.GREEN}{item.name}{Fore.RESET}")

def main():
    if len(sys.argv) < 2:
        print("Specify the path to the folder in the launch arguments")
        return

    target = Path(sys.argv[1])

    if not target.exists() or not target.is_dir():
        print("Error: The path does not exist or is not a directory")
        return

    print(f"Contents of directory: {target}")
    show_dir(target)

if __name__ == "__main__":
    main()
#type python exercise3.py "your desired directory`s path" in the terminal
