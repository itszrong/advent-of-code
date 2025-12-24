.PHONY: all help build run run-timed run-debug clean all-days generate

# Compiler settings
CXX := g++
CXXFLAGS := -std=c++20 -Wall -Wextra
RELEASE_FLAGS := -O3
DEBUG_FLAGS := -g

# Directories
BUILD_DIR := build

# Default target
all: help

help:
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
	echo '#include <iostream>' > "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '#include <fstream>' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '#include <string>' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo 'int main() {' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    std::ifstream file("day$(ARGS)/data_ex.txt");' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    if (!file.is_open()) {' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '        std::cerr << "Error opening file" << std::endl;' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '        return 1;' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    }' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    std::string line;' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    while (std::getline(file, line)) {' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '        std::cout << line << std::endl;' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    }' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '    return 0;' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	echo '}' >> "$$DAY_DIR/day$(ARGS)_p1.cpp"; \
	cp "$$DAY_DIR/day$(ARGS)_p1.cpp" "$$DAY_DIR/day$(ARGS)_p2.cpp"; \
	echo "Created $$DAY_DIR with template files"

# Get arguments passed to make (everything after the target)
ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

# Parse day.part format using Make functions
DAY_NUM := $(word 1,$(subst ., ,$(ARGS)))
PART_NUM := $(word 2,$(subst ., ,$(ARGS)))
SOURCE_FILE := day$(DAY_NUM)/day$(DAY_NUM)_p$(PART_NUM).cpp
BINARY_NAME := $(BUILD_DIR)/day$(DAY_NUM)_p$(PART_NUM)

# Build a specific day
build:
	@if [ -z "$(ARGS)" ]; then \
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
	mkdir -p $(BUILD_DIR); \
	echo "Building $(SOURCE_FILE)..."; \
	$(CXX) $(CXXFLAGS) $(RELEASE_FLAGS) $(SOURCE_FILE) -o $(BINARY_NAME)

# Build in debug mode
build-debug:
	@if [ -z "$(ARGS)" ]; then \
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
	mkdir -p $(BUILD_DIR); \
	echo "Building $(SOURCE_FILE) (debug)..."; \
	$(CXX) $(CXXFLAGS) $(DEBUG_FLAGS) $(SOURCE_FILE) -o $(BINARY_NAME)

# Run a specific day - supports make run 1.1 or make run 2.2
run: build
	@echo "Running $(BINARY_NAME)..."; \
	./$(BINARY_NAME)

# Run with timing - supports make run-timed 1.1 or make run-timed 2.2
run-timed: build
	@echo "Running $(BINARY_NAME) (with timing)..."; \
	time ./$(BINARY_NAME)

# Run in debug mode - supports make run-debug 1.1 or make run-debug 2.2
run-debug: build-debug
	@echo "Running $(BINARY_NAME) (debug)..."; \
	./$(BINARY_NAME)

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@rm -rf $(BUILD_DIR)

# Run all day programs
all-days:
	@echo "Building and running all day programs..."
	@mkdir -p $(BUILD_DIR); \
	for src in $$(find . -name "day*_p*.cpp" -type f | sort); do \
		base=$$(basename $$src .cpp); \
		bin="$(BUILD_DIR)/$$base"; \
		echo "Building $$src..."; \
		$(CXX) $(CXXFLAGS) $(RELEASE_FLAGS) $$src -o $$bin || continue; \
		echo "Running $$bin..."; \
		$$bin || true; \
		echo ""; \
	done


