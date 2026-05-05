import json
import sys
from collections import defaultdict

def validate_channels(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        tracker = defaultdict(list)
        
        for index, item in enumerate(data):
            username = item.get('username', '').strip().lower().replace('@', '')
            if username:
                tracker[username].append(index + 1)

        duplicates = {u: pos for u, pos in tracker.items() if len(pos) > 1}

        if duplicates:
            print("ERROR: Found duplicate Telegram channels!")
            print("-" * 40)
            for user, positions in duplicates.items():
                print(f"• @{user} is repeated at positions: {', '.join(map(str, positions))}")
            print("-" * 40)
            print("Please remove duplicates before merging.")
            sys.exit(1)
        
        print("Success: No duplicates found. List is clean.")
        sys.exit(0)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' is not a valid JSON file.")
        sys.exit(1)

if __name__ == "__main__":
    validate_channels('channels.json')
