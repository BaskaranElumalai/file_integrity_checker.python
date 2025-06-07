import hashlib
import json
import os

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the given algorithm."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None

def save_hashes(hash_dict, filename='hashes.json'):
    with open(filename, 'w') as f:
        json.dump(hash_dict, f, indent=4)

def load_hashes(filename='hashes.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def scan_directory(directory_path, algorithm='sha256'):
    hash_dict = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, directory_path)
            file_hash = calculate_hash(full_path, algorithm)
            hash_dict[relative_path] = file_hash
    return hash_dict

def compare_hashes(old_hashes, new_hashes):
    changes = {'modified': [], 'deleted': [], 'added': []}

    for file, old_hash in old_hashes.items():
        if file not in new_hashes:
            changes['deleted'].append(file)
        elif new_hashes[file] != old_hash:
            changes['modified'].append(file)

    for file in new_hashes:
        if file not in old_hashes:
            changes['added'].append(file)

    return changes

def main():
    directory = input("Enter directory to monitor: ").strip()
    old_hashes = load_hashes()
    new_hashes = scan_directory(directory)
    changes = compare_hashes(old_hashes, new_hashes)

    print("\n=== Changes Detected ===")
    for change_type, files in changes.items():
        print(f"\n{change_type.upper()}:")
        for f in files:
            print(f"  - {f}")

    save_hashes(new_hashes)

if __name__ == "__main__":
    main()
