.PHONY: all help build run run-timed run-debug clean all-days generate

# Compiler settings
JAVAC := javac
JAVA := java
JAVAC_FLAGS := -Xlint:deprecation
RELEASE_FLAGS := 
DEBUG_FLAGS := -g

# Directories
BUILD_DIR := build

# Default target
all: help

help:
	@echo "Advent of Code 2021 - Java"
	@echo ""
	@if ! command -v javac >/dev/null 2>&1; then \
		echo "⚠️  Java compiler (javac) not found! Please install Java JDK."; \
		echo "   macOS:  brew install openjdk"; \
		echo "   Linux:  sudo apt-get install default-jdk"; \
		echo ""; \
	else \
		echo "✓ Using Java compiler: $$(javac -version 2>&1)"; \
		echo ""; \
	fi
	@echo "Available commands:"
	@echo "  make generate X   - Generate a new day folder (e.g., make generate 3)"
	@echo "  make build X.Y    - Build a specific day (e.g., make build 1.1 or make build 2.2)"
	@echo "  make run X.Y      - Build and run a specific day (e.g., make run 1.1 or make run 2.2)"
	@echo "  make run-timed X.Y - Build and run a specific day with timing"
	@echo "  make run-debug X.Y - Build and run in debug mode"
	@echo "  make all-days     - Build and run all day programs"
	@echo "  make clean        - Clean build artifacts"

# Generate a new day folder with template files
generate:
	@if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make generate 3"; \
		exit 1; \
	fi; \
	DAY_DIR="day$(ARGS)"; \
	if [ -d "$$DAY_DIR" ]; then \
		echo "Error: $$DAY_DIR already exists"; \
		exit 1; \
	fi; \
	echo "Creating $$DAY_DIR..."; \
	mkdir -p "$$DAY_DIR"; \
	touch "$$DAY_DIR/data.txt"; \
	touch "$$DAY_DIR/data_ex.txt"; \
	echo 'import java.io.*;' > "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo 'import java.util.*;' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo 'public class Day$(ARGS)P1 {' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '    public static void main(String[] args) {' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '        try {' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '            File file = new File("data_ex.txt");' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '            Scanner scanner = new Scanner(file);' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '            while (scanner.hasNextLine()) {' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '                String line = scanner.nextLine();' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '                System.out.println(line);' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '            }' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '            scanner.close();' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '        } catch (FileNotFoundException e) {' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '            System.err.println("Error reading file: " + e.getMessage());' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '        }' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '    }' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	echo '}' >> "$$DAY_DIR/Day$(ARGS)P1.java"; \
	sed 's/P1/P2/g' "$$DAY_DIR/Day$(ARGS)P1.java" > "$$DAY_DIR/Day$(ARGS)P2.java"; \
	echo "Created $$DAY_DIR with template files"

# Get arguments passed to make (everything after the target)
ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

# Parse day.part format using Make functions
DAY_NUM := $(word 1,$(subst ., ,$(ARGS)))
PART_NUM := $(word 2,$(subst ., ,$(ARGS)))
CLASS_NAME := Day$(DAY_NUM)P$(PART_NUM)
SOURCE_FILE := day$(DAY_NUM)/$(CLASS_NAME).java
CLASS_FILE := day$(DAY_NUM)/$(CLASS_NAME).class

# Build a specific day
build:
	@if ! command -v javac >/dev/null 2>&1; then \
		echo "Error: Java compiler (javac) not found!"; \
		echo "Please install Java JDK:"; \
		echo "  macOS:  brew install openjdk"; \
		echo "  Linux:  sudo apt-get install default-jdk"; \
		exit 1; \
	fi; \
	if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make build 1.1 or make build 2.2"; \
		exit 1; \
	fi; \
	if [ -z "$(DAY_NUM)" ] || [ -z "$(PART_NUM)" ]; then \
		echo "Error: Invalid format. Use DAY.PART (e.g., make build 1.1 or make build 2.2)"; \
		exit 1; \
	fi; \
	if [ ! -f "$(SOURCE_FILE)" ]; then \
		echo "Error: $(SOURCE_FILE) not found"; \
		exit 1; \
	fi; \
	echo "Building $(SOURCE_FILE)..."; \
	$(JAVAC) $(JAVAC_FLAGS) $(RELEASE_FLAGS) $(SOURCE_FILE)

# Build in debug mode
build-debug:
	@if ! command -v javac >/dev/null 2>&1; then \
		echo "Error: Java compiler (javac) not found!"; \
		echo "Please install Java JDK:"; \
		echo "  macOS:  brew install openjdk"; \
		echo "  Linux:  sudo apt-get install default-jdk"; \
		exit 1; \
	fi; \
	if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make build-debug 1.1 or make build-debug 2.2"; \
		exit 1; \
	fi; \
	if [ -z "$(DAY_NUM)" ] || [ -z "$(PART_NUM)" ]; then \
		echo "Error: Invalid format. Use DAY.PART (e.g., make build-debug 1.1 or make build-debug 2.2)"; \
		exit 1; \
	fi; \
	if [ ! -f "$(SOURCE_FILE)" ]; then \
		echo "Error: $(SOURCE_FILE) not found"; \
		exit 1; \
	fi; \
	echo "Building $(SOURCE_FILE) (debug)..."; \
	$(JAVAC) $(JAVAC_FLAGS) $(DEBUG_FLAGS) $(SOURCE_FILE)

# Run a specific day - supports make run 1.1 or make run 2.2
run: build
	@echo "Running $(CLASS_NAME)..."; \
	cd day$(DAY_NUM) && $(JAVA) $(CLASS_NAME)

# Run with timing - supports make run-timed 1.1 or make run-timed 2.2
run-timed: build
	@echo "Running $(CLASS_NAME) (with timing)..."; \
	cd day$(DAY_NUM) && time $(JAVA) $(CLASS_NAME)

# Run in debug mode - supports make run-debug 1.1 or make run-debug 2.2
run-debug: build-debug
	@echo "Running $(CLASS_NAME) (debug)..."; \
	cd day$(DAY_NUM) && $(JAVA) $(CLASS_NAME)

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@find . -type f -name "*.class" -delete
	@rm -rf $(BUILD_DIR)

# Run all day programs
all-days:
	@if ! command -v javac >/dev/null 2>&1; then \
		echo "Error: Java compiler (javac) not found!"; \
		echo "Please install Java JDK:"; \
		echo "  macOS:  brew install openjdk"; \
		echo "  Linux:  sudo apt-get install default-jdk"; \
		exit 1; \
	fi; \
	echo "Building and running all day programs..."; \
	for src in $$(find . -name "Day*.java" -type f | sort); do \
		dir=$$(dirname $$src); \
		base=$$(basename $$src .java); \
		echo "Building $$src..."; \
		$(JAVAC) $(JAVAC_FLAGS) $(RELEASE_FLAGS) $$src || continue; \
		echo "Running $$base..."; \
		(cd $$dir && $(JAVA) $$base) || true; \
		echo ""; \
	done


