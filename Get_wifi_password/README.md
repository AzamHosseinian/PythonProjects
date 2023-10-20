# WiFi Password Retriever

This script retrieves and displays the names and passwords of all saved WiFi networks on a Windows machine. It utilizes the `subprocess` module to interact with the `netsh` command line utility.

## Requirements

- Python 3.6 or above

## Usage

1. Ensure you have Python installed on your machine.
2. Clone this repository or download the script to your machine.
3. Open a command prompt or terminal window and navigate to the directory containing the script.
4. Run the script by executing the command `python wifi_password_retriever.py` (assuming the script file is named `wifi_password_retriever.py`).

The script will output a list of all saved WiFi networks along with their passwords (if available).

## Functionality

- `run_command(command: List[str]) -> str`: Executes a shell command and returns the output as a string. Handles any `CalledProcessError` exceptions that occur.
- `get_profiles() -> List[str]`: Retrieves a list of saved WiFi profiles.
- `get_password(profile: str) -> Optional[str]`: Retrieves the password for a given WiFi profile.
- `display_profiles_and_passwords()`: Iterates over all saved WiFi profiles, retrieves the passwords, and prints them to the console.

## Notes

- This script is intended for educational and personal use only. Unauthorized access to computer systems is illegal and punishable by law.
- The script must be run with sufficient privileges to access the WiFi profiles and passwords.
