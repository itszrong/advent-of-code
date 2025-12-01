.PHONY: help update-toml build run run-debug clean test all-days

# Default target
help:
	@echo "Available commands:"
	@echo "  make update-toml  - Update Cargo.toml with all binary entries"
	@echo "  make build        - Build all binaries"
	@echo "  make run X.Y      - Run a specific day (e.g., make run 1.1 or make run 2.2)"
	@echo "  make run-debug X.Y - Run a specific day in debug mode"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make test         - Run tests"
	@echo "  make all-days     - Run all day binaries"

# Update Cargo.toml with all binary entries
update-toml:
	@echo "Updating Cargo.toml..."
	@./generate_cargo_toml.sh

# Build all binaries
build: update-toml
	@echo "Building all binaries..."
	@cargo build --release

# Build in debug mode (faster for development)
build-debug: update-toml
	@echo "Building all binaries (debug)..."
	@cargo build

# Helper function to convert DAY.PART to dayX_pY format
# Usage: $(call day_part_to_bin,1.1) -> day1_p1
day_part_to_bin = day$(word 1,$(subst ., ,$(1)))_p$(word 2,$(subst ., ,$(1)))

# Get arguments passed to make (everything after the target)
ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

# Parse day.part format using Make functions
DAY_NUM := $(word 1,$(subst ., ,$(ARGS)))
PART_NUM := $(word 2,$(subst ., ,$(ARGS)))
BIN_NAME := day$(DAY_NUM)_p$(PART_NUM)

# Run a specific day - supports make run 1.1 or make run 2.2
run: update-toml
	@if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make run 1.1 or make run 2.2"; \
		exit 1; \
	fi; \
	if [ -z "$(DAY_NUM)" ] || [ -z "$(PART_NUM)" ]; then \
		echo "Error: Invalid format. Use DAY.PART (e.g., make run 1.1 or make run 2.2)"; \
		exit 1; \
	fi; \
	echo "Running $(BIN_NAME)..."; \
	cargo run --release --bin $(BIN_NAME)

# Run in debug mode - supports make run-debug 1.1 or make run-debug 2.2
run-debug: update-toml
	@if [ -z "$(ARGS)" ]; then \
		echo "Error: Day not specified. Usage: make run-debug 1.1 or make run-debug 2.2"; \
		exit 1; \
	fi; \
	if [ -z "$(DAY_NUM)" ] || [ -z "$(PART_NUM)" ]; then \
		echo "Error: Invalid format. Use DAY.PART (e.g., make run-debug 1.1 or make run-debug 2.2)"; \
		exit 1; \
	fi; \
	echo "Running $(BIN_NAME) (debug)..."; \
	cargo run --bin $(BIN_NAME)

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@cargo clean

# Run tests
test: update-toml
	@echo "Running tests..."
	@cargo test

# Run all day binaries
all-days: update-toml
	@echo "Running all day binaries..."
	@for bin in $$(find src/bin -name "*.rs" -type f ! -name "*copy*" -exec basename {} .rs \; | sort); do \
		echo "Running $$bin..."; \
		cargo run --release --bin $$bin || true; \
		echo ""; \
	done

