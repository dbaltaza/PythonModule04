# Python Module 04 — File I/O and Exception Handling

Small, themed exercises that practice Python file handling (`open`, `read`, `write`), stream output, and robust exception handling. Each exercise is a standalone script and can be run directly.

## Structure

```
.
├── ex0
│   └── ft_ancient_text.py
├── ex1
│   └── ft_archive_creation.py
├── ex2
│   └── ft_stream_management.py
├── ex3
│   └── ft_vault_security.py
└── ex4
    └── ft_crisis_response.py
```

## Exercise Overview

- **ex0 — Ancient Text Recovery**
  - Opens and reads `ancient_fragment.txt` with error handling.
  - Demonstrates basic `open()` / `read()` and `try/except`.

- **ex1 — Archive Creation**
  - Creates `new_discovery.txt` and writes multiple lines.
  - Demonstrates `open()` with write mode and simple exception handling.

- **ex2 — Stream Management**
  - Prints messages to `stdout` and `stderr` using `sys.stdout` / `sys.stderr`.
  - Demonstrates stream separation and formatted output.

- **ex3 — Vault Security**
  - Uses `with` to safely read and append to `classified_data.txt`.
  - Demonstrates `seek()`, append mode, and automatic file closure.

- **ex4 — Crisis Response**
  - Implements `crisis_handler()` with `try/except` and `with`.
  - Handles `FileNotFoundError`, `PermissionError`, and unexpected exceptions.
  - Runs test scenarios against multiple filenames.

## Requirements

- Python 3.10+ recommended
- No external dependencies

## How to Run

Run any exercise from the repository root:

```bash
python3 ex0/ft_ancient_text.py
python3 ex1/ft_archive_creation.py
python3 ex2/ft_stream_management.py
python3 ex3/ft_vault_security.py
python3 ex4/ft_crisis_response.py
```

## Test Data Notes

Some exercises expect local data files (e.g., `ancient_fragment.txt`, `classified_data.txt`). If your course provides a data generator script such as:

```bash
python3 tools/data_generator.py
```

run it from the repo root to create the required test files before executing the scripts.

## Output

Each script prints a themed, structured output to the terminal. Some exercises may also create or update files in their respective directories.
