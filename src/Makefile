# src/Makefile

.PHONY: install setup run test clean

install:
	@echo "Installing dependencies..."
	pip install -e .

setup: install
	@echo "Installing Playwright browsers..."
	playwright install webkit
	@echo "Creating secret key..."
	python create_secret_key.py
	@echo "Setup complete!"

dev-install:
	@echo "Installing dev dependencies..."
	pip install -e ".[dev]"
	playwright install webkit
	python create_secret_key.py

run:
	@echo "Starting server..."
	python app.py

test:
	@echo "Running tests..."
	pytest

format:
	@echo "Formatting code..."
	black .
	ruff check --fix .

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ .pytest_cache .coverage htmlcov *.pyc
	find . -type d -name "__pycache__" -exec rm -rf {} +

help:
	@echo "Available commands:"
	@echo "  make setup       - Complete project setup"
	@echo "  make install     - Install dependencies"
	@echo "  make dev-install - Install with dev dependencies"
	@echo "  make run         - Start the Flask server"
	@echo "  make test        - Run tests"
	@echo "  make format      - Format code with black/ruff"
	@echo "  make clean       - Remove cache and temp files"

# to run the server on mobile devices
.PHONY: run run-mobile

run:
	python main.py

run-mobile:
	PORT=5000 HOST=0.0.0.0 python main.py
	@echo "📱 Öffne auf deinem Handy: http://192.168.178.140:5000"
