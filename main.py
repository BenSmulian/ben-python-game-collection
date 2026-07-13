from pathlib import Path
import shutil, json, os, urllib, subprocess
import urllib.request
import urllib.error

games_path = Path("./games")

# --- Linux/Mac Only Stuff ---

# Ordered from most powerful/modern to simplest/fallback
terminals = [
    "osascript",  # macOS native execution wrapper
    "konsole",
    "yakuake",
    "guake",
    "gnome-terminal",
    "xfce4-terminal",
    "lxterminal",
    "kgx",
    "mate-terminal",
    "ptyxis",
    "alacritty",
    "kitty",
    "ghostty",
    "foot",
    "terminator",
    "tilix",
    "terminology",
    "tilda",
    "xterm",
    "st",
    "urxvt",
    "warp-terminal",
    "hyper",
    "blackbox",
    "cool-retro-term"
]

def get_preffered_terminal():
    config_file = Path("./app_config.json")
    
    # Safely look for user configuration first
    if config_file.exists():
        try:
            config_data = json.loads(config_file.read_text())
            configured_preferred = config_data.get("preferred_terminal", "None")
            if configured_preferred != "None" and shutil.which(configured_preferred):
                return configured_preferred
        except (json.JSONDecodeError, KeyError):
            pass  # Fall back to automated scan if json is malformed

    # Automated scan down the priority list
    for terminal_name in terminals:
        if shutil.which(terminal_name) is not None:
            return terminal_name
    
    print("You are using a potato as a PC. First, get mental help; second, run this on Linux or Mac (or download any known graphical terminal in existence).")
    return None

def open_terminal(*args):
    terminal = get_preffered_terminal()
    if not terminal:
        return

    # Flatten arbitrary infinite args/commands into a single string for shell execution
    command_str = " ".join(str(arg) for arg in args)

    match terminal:
        case "osascript":
            # Native macOS handling: Tells Terminal app to run a script
            # If no command is provided, it simply opens a clean terminal window
            script = f'tell application "Terminal" to do script "{command_str}"' if command_str else 'tell application "Terminal" to do script ""'
            subprocess.run(["osascript", "-e", script])

        case "yakuake" | "guake":
            # Dropdown terminals do not launch new windows cleanly with inline tasks; 
            # they are triggered globally via D-Bus commands or execution toggles
            if command_str:
                subprocess.run([terminal, "-e", command_str])
            else:
                subprocess.run([terminal])

        case "gnome-terminal" | "tilix" | "terminator":
            # Modern Linux terminals use the standard double-dash execution barrier
            if command_str:
                subprocess.run([terminal, "--", "bash", "-c", f"{command_str}; exec bash"])
            else:
                subprocess.run([terminal])

        case "kgx" | "ptyxis":
            # GNOME Console variations use explicit command execution flags
            if command_str:
                subprocess.run([terminal, "-e", f"bash -c '{command_str}; exec bash'"])
            else:
                subprocess.run([terminal])

        case "konsole" | "xfce4-terminal" | "lxterminal" | "mate-terminal" | "alacritty" | "kitty" | "ghostty" | "foot" | "terminology" | "tilda" | "xterm" | "st" | "urxvt" | "warp-terminal" | "hyper" | "cool-retro-term":
            # Broad compatibility block using standard execution arguments (-e)
            if command_str:
                # Passing 'exec bash' ensures the newly spawned window remains open after your tasks finish
                subprocess.run([terminal, "-e", "bash", "-c", f"{command_str}; exec bash"])
            else:
                subprocess.run([terminal])

        case "blackbox":
            # Handles both direct binary execution or standard Linux Flatpak routing
            binary = shutil.which("blackbox") or shutil.which("com.raggesilver.BlackBox")
            if command_str:
                subprocess.run([binary, "-c", command_str])
            else:
                subprocess.run([binary])

# --- end of Linux/Mac Only Stuff ---

def get_github_directory_children(owner, repo, subdirectory_path):
    # Construct the GitHub API endpoint for the specific path
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{subdirectory_path}"
    
    # GitHub API requires a User-Agent header
    req = urllib.request.Request(url, headers={"User-Agent": "Python-Script"})
    
    try:
        with urllib.request.urlopen(req) as response:
            
            items = json.loads(response.read().decode())
            
            # print(f"Children of '{subdirectory_path}' in {owner}/{repo}:\n" + "-"*50)

            items = [item["name"].replace(".py", "") for item in items if item["type"] != "dir"]
            
            return items
                    
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Path '{subdirectory_path}' or repository '{owner}/{repo}' not found.")
        elif e.code == 403:
            print("Error: API rate limit exceeded. Try again later or use an API token.")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
        return []
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
        return []

def choose_game():
    game_names = [file.name for file in games_path.iterdir() if file.is_file()]

    question = "choose a game from the fallowing: "

    for i, game_name in enumerate(game_names):
        question += "\n" + str(i+1) + ". " + game_name

    chosen_game_index = input(question + "\n")

    try:
        if len(game_names) > int(chosen_game_index)-1 and int(chosen_game_index)-1 >= 0:
            return game_names[int(chosen_game_index)-1]
    except:
        return None

    return None

def chooose_option():
    player_input = input("would you like to\n1. play a game\n2. install a game\n")

    match player_input:
        case "1":
            return "game"
        case "2":
            return "install"
        case _:
            return "error"

def download_github_file(owner, repo, file_path, save_directory=".", branch="main"):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/refs/heads/{branch}/{file_path}"
    # https://raw.githubusercontent.com/BenSmulian/ben-python-game-collection/refs/heads/main/main.py
    
    local_filename = Path(file_path).name
    destination_path = Path(save_directory) / local_filename
    
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    
    req = urllib.request.Request(url, headers={"User-Agent": "Python-Script"})
    
    try:
        with urllib.request.urlopen(req) as response:
            with open(destination_path, "wb") as local_file:
                local_file.write(response.read())
        
        return True
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            if branch == "main":
                print("File not found on branch 'main'. Retrying with branch 'master'...")
                return download_github_file(owner, repo, file_path, save_directory, branch="master")
            else:
                print(f"Error 404: File '{file_path}' not found in repository '{owner}/{repo}'.")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
        return False

def choose_install():
    game_names = get_github_directory_children("BenSmulian", "ben-python-game-collection", "games")

    question = "choose a game from the fallowing to install: "

    for i, game_name in enumerate(game_names):
        question += "\n" + str(i+1) + ". " + game_name

    chosen_game_name = input(question + "\n")

    try:
        if len(game_names) > int(chosen_game_name)-1 and int(chosen_game_name)-1 >= 0:
            chosen_game_name = game_names[int(chosen_game_name)-1]
        else:
            return None

    except:
        return None

    print("started downloading " + chosen_game_name + "...")
    if download_github_file("BenSmulian", "ben-python-game-collection", "games/" + chosen_game_name +".py", save_directory="./games/"):
        print(chosen_game_name + " is ready to play!")

is_windows = os.name == "nt"

def main():
    while True:
        match chooose_option():
            case "game":
                chosen_game = choose_game()
                if chosen_game != None: 
                    if is_windows:
                        # 1. Resolve paths cleanly to absolute Windows paths
                        script_dir = Path("./").resolve()
                        activate_bat = (script_dir / "venv" / "Scripts" / "activate.bat").resolve()
                        game_script = (script_dir / "games" / chosen_game).resolve()

                        # 2. Build the precise string for CMD (Note the use of % instead of $)
                        # The & operator chains commands unconditionally on a single line
                        cmd_payload = ( 
                            f'set "SCRIPT_DIR={script_dir}" && '
                            f'cd /d "%SCRIPT_DIR%" && '
                            f'"{activate_bat}" && '
                            f'python "{game_script}"'
                        )

                        # 3. Launch via CMD using the built-in shell execution engine
                        # Passing shell=True allows Python to call the native 'start' mechanism directly
                        subprocess.run(f'start cmd /k "{cmd_payload}"', shell=True)
                    else:
                        open_terminal("SCRIPT_DIR=$(cd \"$(dirname \"$0\")\" && pwd) cd \"$SCRIPT_DIR\"", "&&", "source \"./venv/bin/activate\"", "&&", f"python3 \"./games/{chosen_game}\"")


            case "install":
                choose_install()
if __name__ == "__main__":
    main()
