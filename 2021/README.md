# Advent of Code 2021 - Java

Java solutions for Advent of Code 2021.

## Prerequisites

- Java JDK (version 8 or higher)
- make

### Installing Java

**macOS:**
```bash
brew install openjdk
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install default-jdk
```

## Usage

### Generate a new day

```bash
make generate 1
```

This creates a `day1` folder with:
- `Day1P1.java` - Part 1 solution template
- `Day1P2.java` - Part 2 solution template
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
2021/
├── Makefile
├── README.md
└── dayX/
    ├── DayXP1.java
    ├── DayXP2.java
    ├── DayXP1.class    # Compiled (auto-generated)
    ├── DayXP2.class    # Compiled (auto-generated)
    ├── data.txt
    └── data_ex.txt
```

## Template Structure

Each generated Java file includes:
- File I/O with Scanner
- Exception handling
- Basic structure for reading input line by line

```java
import java.io.*;
import java.util.*;

public class Day1P1 {
    public static void main(String[] args) {
        try {
            File file = new File("day1/data_ex.txt");
            Scanner scanner = new Scanner(file);
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }
            
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }
}
```

