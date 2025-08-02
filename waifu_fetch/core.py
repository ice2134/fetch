import os
import random
import platform
import psutil
import socket

def show_random_waifu():
    dir_path = os.path.join(os.path.dirname(__file__), "ascii_waifus")
    waifus = [f for f in os.listdir(dir_path) if f.endswith(".txt")]

    if not waifus:
        print("No waifu ASCII files found.")
        return

    # Detect rare files by name (e.g. "golden_waifu.txt", "rare_001.txt")
    rare_waifus = [f for f in waifus if "gold" in f.lower() or "rare" in f.lower()]
    is_gold = False

    if rare_waifus and random.random() < 0.05:
        chosen = random.choice(rare_waifus)
        is_gold = True
    else:
        chosen = random.choice(waifus)

    ascii_path = os.path.join(dir_path, chosen)
    with open(ascii_path, "r", encoding="utf-8") as f:
        ascii_art = f.readlines()

    sys_info = get_system_info()
    max_lines = max(len(ascii_art), len(sys_info))

    print()
    for i in range(max_lines):
        waifu_line = ascii_art[i].rstrip("\n") if i < len(ascii_art) else ""
        info_line = sys_info[i] if i < len(sys_info) else ""
        print(f"{waifu_line:<70}   {info_line}")

    if is_gold:
        print()
        print("\033[93m✨🎉  CONGRATS! YOU JUST UNLOCKED THE GOLDEN WAIFU!  🎉✨")
        print("💥  It had only a 5% chance to appear.")
        print("💡  Maybe... just maybe... go touch some grass, bro. 🍃\033[0m")

def get_system_info():
    uname = platform.uname()
    ram = psutil.virtual_memory()
    os_version = platform.win32_ver()[0] or uname.release
    processor = uname.processor or platform.processor()

    # ANSI Colors
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    return [
        f"{GREEN}User:{RESET}      {os.getlogin()}",
        f"{CYAN}Host:{RESET}      {socket.gethostname()}",
        f"{YELLOW}OS:{RESET}        Windows {os_version}",
        f"{YELLOW}Kernel:{RESET}    {uname.version.split()[0]}",
        f"{MAGENTA}CPU:{RESET}       {processor}",
        f"{MAGENTA}Cores:{RESET}     {psutil.cpu_count(logical=False)} ({psutil.cpu_count(logical=True)} threads)",
        f"{MAGENTA}RAM:{RESET}       {round(ram.total / (1024**3), 2)} GB",
        f"{MAGENTA}Python:{RESET}    {platform.python_version()}",
    ]
