import json
import pickle
import os

# Define a custom class to demonstrate object serialization
class UserProfile:
    def __init__(self, username, points, inventory):
        self.username = username
        self.points = points
        self.inventory = inventory

    def __repr__(self):
        return f"UserProfile(username='{self.username}', points={self.points}, inventory={self.inventory})"


def run_json_demo(filename="data.json"):
    print("--- 1. JSON Serialization & Deserialization ---")
    
    # In-memory dictionary data
    config_data = {
        "theme": "dark",
        "resolution": "1920x1080",
        "auto_save": True,
        "recent_projects": ["proj_alpha", "proj_beta"]
    }
    
    # SERIALIZATION: Write data to a text file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=4)
    print(f"[JSON] Data successfully serialized to '{filename}'")

    # DESERIALIZATION: Read data back from the text file
    with open(filename, "r", encoding="utf-8") as file:
        restored_config = json.load(file)
        
    print("[JSON] Restored Object Type:", type(restored_config))
    print("[JSON] Restored Content:", restored_config)
    print()


def run_pickle_demo(filename="object_state.pkl"):
    print("--- 2. Pickle Serialization & Deserialization ---")
    
    # Instantiate a custom class object
    player = UserProfile(username="ShadowNinja", points=1250, inventory=["sword", "shield", "potion"])
    print(f"[Pickle] Original Object State: {player}")

    # SERIALIZATION: Write object to a binary file
    with open(filename, "wb") as file:
        pickle.dump(player, file)
    print(f"[Pickle] Object successfully serialized to binary file '{filename}'")

    # DESERIALIZATION: Read object back from the binary file
    # WARNING: Only unpickle data you created yourself to avoid code execution exploits
    with open(filename, "rb") as file:
        restored_player = pickle.load(file)
        
    print("[Pickle] Restored Object Type:", type(restored_player))
    print(f"[Pickle] Restored Object State: {restored_player}")
    print()


def cleanup(files):
    """Removes the generated files to keep your directory clean."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)


if __name__ == "__main__":
    # Define file paths
    json_file = "app_config.json"
    pickle_file = "player_state.pkl"

    # Execute workflows
    run_json_demo(json_file)
    run_pickle_demo(pickle_file)
    
    # Cleanup files
    cleanup([json_file, pickle_file])
