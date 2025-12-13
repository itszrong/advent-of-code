.PHONY: all help build run run-timed run-debug clean all-days generate

# Compiler settings - try ocamlopt first, fall back to ocamlc
OCAMLOPT := $(shell which ocamlopt 2>/dev/null)
OCAMLC_BYTE := $(shell which ocamlc 2>/dev/null)

ifneq ($(OCAMLOPT),)
    OCAMLC := ocamlopt
    OCAML_FLAGS := -O3
    COMPILER_TYPE := native
else ifneq ($(OCAMLC_BYTE),)
    OCAMLC := ocamlc
    OCAML_FLAGS := 
    COMPILER_TYPE := bytecode
else
    OCAMLC := 
    COMPILER_TYPE := none
endif

DEBUG_FLAGS := -g

# Directories
BUILD_DIR := build

# Default target
all: help

help:
	@echo "Advent of Code 2022 - OCaml"
	@echo ""
	@if [ "$(COMPILER_TYPE)" = "none" ]; then \
		echo "⚠️  OCaml compiler not found! Please install:"; \
		echo "   macOS:  brew install ocaml"; \
		echo "   Linux:  sudo apt-get install ocaml"; \
		echo ""; \
	else \
		echo "✓ Using OCaml $(COMPILER_TYPE) compiler: $(OCAMLC)"; \
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
	echo 'let read_file filename =' > "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '  let ic = open_in filename in' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '  let rec read_lines acc =' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '    try' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '      let line = input_line ic in' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '      read_lines (line :: acc)' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '    with End_of_file ->' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '      close_in ic;' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '      List.rev acc' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '  in' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '  read_lines []' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo 'let () =' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '  let lines = read_file "day$(ARGS)/data_ex.txt" in' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	echo '  List.iter (fun line -> Printf.printf "%s\n" line) lines' >> "$$DAY_DIR/day$(ARGS)_p1.ml"; \
	cp "$$DAY_DIR/day$(ARGS)_p1.ml" "$$DAY_DIR/day$(ARGS)_p2.ml"; \
	echo "Created $$DAY_DIR with template files"

# Get arguments passed to make (everything after the target)
ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

# Parse day.part format using Make functions
DAY_NUM := $(word 1,$(subst ., ,$(ARGS)))
PART_NUM := $(word 2,$(subst ., ,$(ARGS)))
SOURCE_FILE := day$(DAY_NUM)/day$(DAY_NUM)_p$(PART_NUM).ml
BINARY_NAME := $(BUILD_DIR)/day$(DAY_NUM)_p$(PART_NUM)

# Build a specific day
build:
	@if [ "$(COMPILER_TYPE)" = "none" ]; then \
		echo "Error: OCaml compiler not found!"; \
		echo "Please install OCaml:"; \
		echo "  macOS:  brew install ocaml"; \
		echo "  Linux:  sudo apt-get install ocaml"; \
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
	mkdir -p $(BUILD_DIR); \
	echo "Building $(SOURCE_FILE) (using $(COMPILER_TYPE) compiler)..."; \
	$(OCAMLC) $(OCAML_FLAGS) $(SOURCE_FILE) -o $(BINARY_NAME)

# Build in debug mode
build-debug:
	@if [ "$(COMPILER_TYPE)" = "none" ]; then \
		echo "Error: OCaml compiler not found!"; \
		echo "Please install OCaml:"; \
		echo "  macOS:  brew install ocaml"; \
		echo "  Linux:  sudo apt-get install ocaml"; \
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
	mkdir -p $(BUILD_DIR); \
	echo "Building $(SOURCE_FILE) (debug)..."; \
	$(OCAMLC) $(DEBUG_FLAGS) $(SOURCE_FILE) -o $(BINARY_NAME)

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
	@find . -type f \( -name "*.cmi" -o -name "*.cmo" -o -name "*.cmx" -o -name "*.o" \) -delete

# Run all day programs
all-days:
	@if [ "$(COMPILER_TYPE)" = "none" ]; then \
		echo "Error: OCaml compiler not found!"; \
		echo "Please install OCaml:"; \
		echo "  macOS:  brew install ocaml"; \
		echo "  Linux:  sudo apt-get install ocaml"; \
		exit 1; \
	fi; \
	echo "Building and running all day programs (using $(COMPILER_TYPE) compiler)..."; \
	mkdir -p $(BUILD_DIR); \
	for src in $$(find . -name "day*_p*.ml" -type f | sort); do \
		base=$$(basename $$src .ml); \
		bin="$(BUILD_DIR)/$$base"; \
		echo "Building $$src..."; \
		$(OCAMLC) $(OCAML_FLAGS) $$src -o $$bin || continue; \
		echo "Running $$bin..."; \
		$$bin || true; \
		echo ""; \
	done


