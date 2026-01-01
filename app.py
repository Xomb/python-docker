"""
Docstring for python-docker.app
"""
import requests


def get_facts():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        print("Random Cat Fact:", response.json().get("fact"))
    else:
        print("Could not retrieve cat fact.")


if __name__ == "__main__":
    get_facts()


"""        
def main():
    print("Hello, from inside my first Docker container!")
    print("Python version:", {sys.version})
    print(f"--- Habit check: 1% better every day! ---")


if __name__ == "__main__":
    main()
"""
