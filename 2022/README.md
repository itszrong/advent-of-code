# Advent of Code 2022 - OCaml

OCaml solutions for Advent of Code 2022.

## Prerequisites

- OCaml compiler (ocamlopt)
- make

### Installing OCaml

**macOS:**
```bash
brew install ocaml
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ocaml
```

## Usage

### Generate a new day

```bash
make generate 1
```

This creates a `day1` folder with:
- `day1_p1.ml` - Part 1 solution template
- `day1_p2.ml` - Part 2 solution template
- `data.txt` - Input data
- `data_ex.txt` - Example data

### Build and run

```bash
# Run a specific day and part
make run 1.1    # Run day 1, part 1
make run 5.2    # Run day 5, part 2

# Run with timing
make run-timed 1.1

# Run in debug mode
make run-debug 1.1

# Build without running
make build 1.1
```

### Other commands

```bash
# Run all solutions
make all-days

# Clean build artifacts
make clean

# Show help
make help
```

## File Structure

```
2022/
├── Makefile
├── README.md
├── build/          # Compiled binaries (auto-generated)
└── dayX/
    ├── dayX_p1.ml
    ├── dayX_p2.ml
    ├── data.txt
    └── data_ex.txt
```

