.PHONY: all help build run run-timed run-debug clean test all-days generate

# Default target
all: help

help:
	@echo "Available commands:"
	@echo "  make generate X   - Generate a new day folder (e.g., make generate 3)"
	@echo "  make run X.Y      - Run a specific day (e.g., make run 1.1 or make run 2.2)"
	@echo "  make run-timed X.Y - Run a specific day with timing"
	@echo "  make all-days     - Run all day binaries"
	@echo "  make clean        - Clean Python cache files"

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
	echo 'def main():' > "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '    with open("day$(ARGS)/data_ex.txt", "r") as f:' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '        contents = f.read()' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '    print(contents)' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo 'if __name__ == "__main__":' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	echo '    main()' >> "$$DAY_DIR/day$(ARGS)_p1.py"; \
	cp "$$DAY_DIR/day$(ARGS)_p1.py" "$$DAY_DIR/day$(ARGS)_p2.py"; \
	echo "Created $$DAY_DIR with template files"

# Get arguments passed to make (everything after the target)
ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)  # Commented out - causes FUNCNEST issues in zsh

# Parse day.part format using Make functions
DAY_NUM := $(word 1,$(subst ., ,$(ARGS)))
PART_NUM := $(word 2,$(subst ., ,$(ARGS)))
SCRIPT_NAME := day$(DAY_NUM)/day$(DAY_NUM)_p$(PART_NUM).py

# Run a specific day - supports make run 1.1 or make run 2.2
run:
	@if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make run 1.1 or make run 2.2"; \
		exit 1; \
	fi; \
	if [ -z "$(DAY_NUM)" ] || [ -z "$(PART_NUM)" ]; then \
		echo "Error: Invalid format. Use DAY.PART (e.g., make run 1.1 or make run 2.2)"; \
		exit 1; \
	fi; \
	if [ ! -f "$(SCRIPT_NAME)" ]; then \
		echo "Error: $(SCRIPT_NAME) not found"; \
		exit 1; \
	fi; \
	echo "Running $(SCRIPT_NAME)..."; \
	python3 $(SCRIPT_NAME)

# Run with timing - supports make run-timed 1.1 or make run-timed 2.2
run-timed:
	@if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make run-timed 1.1 or make run-timed 2.2"; \
		exit 1; \
	fi; \
	if [ -z "$(DAY_NUM)" ] || [ -z "$(PART_NUM)" ]; then \
		echo "Error: Invalid format. Use DAY.PART (e.g., make run-timed 1.1 or make run-timed 2.2)"; \
		exit 1; \
	fi; \
	if [ ! -f "$(SCRIPT_NAME)" ]; then \
		echo "Error: $(SCRIPT_NAME) not found"; \
		exit 1; \
	fi; \
	echo "Running $(SCRIPT_NAME) (with timing)..."; \
	time python3 $(SCRIPT_NAME)

# Clean Python cache files
clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -exec rm -f {} + 2>/dev/null || true
	@find . -type f -name "*.pyo" -exec rm -f {} + 2>/dev/null || true

# Run all day scripts
all-days:
	@echo "Running all day scripts..."
	@for script in $$(find . -name "day*_p*.py" -type f | sort); do \
		echo "Running $$script..."; \
		python3 $$script || true; \
		echo ""; \
	done


