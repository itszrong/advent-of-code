# Advent of Code 2022 - Python

Python solutions for Advent of Code 2022.

## Prerequisites

- Python 3
- make

## Usage

### Generate a new day

```bash
make generate 1
```

This creates a `day1` folder with:
- `day1_p1.py` - Part 1 solution template
- `day1_p2.py` - Part 2 solution template
- `data.txt` - Input data
- `data_ex.txt` - Example data

### Run

```bash
# Run a specific day and part
make run 1.1    # Run day 1, part 1
make run 5.2    # Run day 5, part 2

# Run with timing
make run-timed 1.1
```

### Other commands

```bash
# Run all solutions
make all-days

# Clean Python cache files
make clean

# Show help
make help
```

## File Structure

```
2022/
├── Makefile
├── README.md
└── dayX/
    ├── dayX_p1.py
    ├── dayX_p2.py
    ├── data.txt
    └── data_ex.txt
```
