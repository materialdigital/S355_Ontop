#!/usr/bin/env bash

set -e

echo "========================================"
echo "Setting up R2RML/YARRRML pipeline"
echo "========================================"

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$PROJECT_ROOT"

# --------------------------------------------------
# Check required system dependencies
# --------------------------------------------------

echo ""
echo "Checking system dependencies..."

check_command() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "ERROR: '$1' is not installed or not in PATH."
        exit 1
    fi
}

check_command java
check_command node
check_command npm
check_command python3
check_command pip3

echo "All required system dependencies found."

# --------------------------------------------------
# Print versions
# --------------------------------------------------

echo ""
echo "Detected versions:"

echo "- Java:"
java --version | head -n 1

echo "- Node:"
node --version

echo "- npm:"
npm --version

echo "- Python:"
python3 --version

# --------------------------------------------------
# Install Node.js dependencies
# --------------------------------------------------

echo ""
echo "Installing Node.js dependencies..."

npm install

echo "Node.js dependencies installed."

# --------------------------------------------------
# Create Python virtual environment
# --------------------------------------------------

echo ""
echo "Creating Python virtual environment..."

if [ ! -d "$PROJECT_ROOT/.venv" ]; then
    python3 -m venv "$PROJECT_ROOT/.venv"
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# --------------------------------------------------
# Activate venv
# --------------------------------------------------

# shellcheck disable=SC1091
source "$PROJECT_ROOT/.venv/bin/activate"

# --------------------------------------------------
# Upgrade pip
# --------------------------------------------------

echo ""
echo "Upgrading pip..."

pip install --upgrade pip

# --------------------------------------------------
# Install Python dependencies
# --------------------------------------------------

echo ""
echo "Installing Python dependencies..."

pip install -r requirements.txt

echo "Python dependencies installed."

# --------------------------------------------------
# Final validation
# --------------------------------------------------

echo ""
echo "Running final validation..."

if ! npx yarrrml-parser --help >/dev/null 2>&1; then
    echo "ERROR: yarrrml-parser is not working correctly."
    exit 1
fi

echo "yarrrml-parser OK."

echo ""
echo "========================================"
echo "Setup completed successfully."
echo "========================================"
echo ""
echo "To activate the Python environment manually:"
echo ""
echo "    source .venv/bin/activate"
echo ""
echo "You can now run the pipeline."