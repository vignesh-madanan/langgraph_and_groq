SCRIPT_NAME = main.py
PYTHON = python3

# Default target that runs the Python script
run:
	$(PYTHON) $(SCRIPT_NAME)

# Clean target (optional) to remove any generated files
clean:
	rm -rf __pycache__ *.pyc

# Add a help target to describe the available commands (optional)
help:
	@echo "Makefile for running a Python script"
	@echo "Available targets:"
	@echo "  run   - Run the Python script"
	@echo "  clean - Remove any generated files (e.g., __pycache__)"
	@echo "  help  - Show this help message"