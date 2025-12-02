# Advent of Code 2025

Rust solutions for Advent of Code 2025.

## Quick Start

```bash
# Generate a new day
make generate 3

# Run a solution
make run 3.1
```

## Commands

| Command | Description |
|---------|-------------|
| `make generate X` | Create a new day folder with template files |
| `make run X.Y` | Run day X part Y in release mode |
| `make run-debug X.Y` | Run day X part Y in debug mode |
| `make build` | Build all binaries |
| `make clean` | Clean build artifacts |
| `make all-days` | Run all solutions |

## Project Structure

```
src/bin/
├── day1/
│   ├── data.txt       # Puzzle input
│   ├── data_ex.txt    # Example input
│   ├── day1_p1.rs     # Part 1 solution
│   └── day1_p2.rs     # Part 2 solution
├── day2/
│   └── ...
```

## Adding Dependencies

Add dependencies to `Cargo.toml` **before** the `[[bin]]` entries:

```toml
[dependencies]
counter = "0.7"
```

The `Cargo.toml` binary entries are auto-generated when you run `make run`.

