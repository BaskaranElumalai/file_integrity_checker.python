# file_integrity_checker.python

COMPANY: CODTECH IT SOLUTIONS

NAME: Baskaran

INTERN ID :CT06DF546

DOMAIN:Cyber Security & Ethical Hacking

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

##YOU HAVE TO ENTER DESCRIOTON OF YOUR TASK (AND IT SHOULD NOT BE LESS THAN 500 WORDS)

#OUTPUT



# File Integrity Monitor `int.py`

## Description

`int.py` is a Python-based file integrity checker designed to monitor and detect changes (modification, deletion, addition) in files within a specified directory. It uses cryptographic hash functions to track changes over time.

Ideal for use in system auditing, digital forensics, or file change monitoring tasks.

---

##  Requirements

Built-in modules only:
- `hashlib`
- `json`
- `os`

No external libraries required.

---

## Usage

Run the script in your terminal:

```bash
python int.py
```

You will be prompted to enter the directory you want to monitor:

```text
Enter directory to monitor: /path/to/your/folder
```

The script will:
1. Generate hash values for files in the specified directory.
2. Compare current hashes with previously saved values (`hashes.json`).
3. Display files that have been added, modified, or deleted.
4. Update `hashes.json` with the latest state.

---

## Example Output

```text
=== Changes Detected ===

MODIFIED:
  - important/config.yaml

DELETED:
  - old_script.sh

ADDED:
  - new_folder/new_file.txt
```

## How It Works

- `calculate_hash()`: Computes hash of individual files.
- `scan_directory()`: Walks through the directory and calculates hashes for all files.
- `compare_hashes()`: Compares old and new hash states.
- `save_hashes() / load_hashes()`: Stores and retrieves hash data in/from `hashes.json`.

---

## Tip

You can schedule this script to run regularly using tools like `cron` (Linux/macOS) or Task Scheduler (Windows) to continuously monitor sensitive directories.

---

## Disclaimer

This tool is provided for **educational and monitoring purposes**. Ensure you have permission to scan and monitor directories on systems that are not your own.

---

## Author

Developed as part of a cybersecurity monitoring task
