import subprocess
import re
from typing import List, Tuple, Optional


def run_command(command: List[str]) -> str:
    try:
        output = subprocess.check_output(command, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {command}")
        print(f"Error: {e}")
        return ""
    return output


def get_profiles() -> List[str]:
    output = run_command(["netsh", "wlan", "show", "profiles"])
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
    return profiles


def get_password(profile: str) -> Optional[str]:
    output = run_command(["netsh", "wlan", "show", "profile", profile, "key=clear"])
    password_match = re.search(r"Key Content\s*:\s*(.*)", output)
    return password_match.group(1) if password_match else None


def display_profiles_and_passwords():
    profiles = get_profiles()
    for profile in profiles:
        password = get_password(profile)
        print(f"{profile:<30}|  {password if password else '':<}")


if __name__ == "__main__":
    display_profiles_and_passwords()
