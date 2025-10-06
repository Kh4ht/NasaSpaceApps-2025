#!/bin/bash
# ------------------------------------------------------------
# setup_venv.sh
# A portable script to rebuild a virtual environment for any project
# ------------------------------------------------------------

# Stop if any command fails
set -e

# Configuration (change if you prefer a different name or Python version)
VENV_NAME=".venv311"
PYTHON_PATH="/opt/homebrew/bin/python3.11"
REQ_FILE="requirements.txt"

echo "🔧 Setting up Python virtual environment..."

# 1. Deactivate current venv (if any)
deactivate 2>/dev/null || true

# 2. Remove existing environment
if [ -d "$VENV_NAME" ]; then
  echo "🧹 Removing existing environment: $VENV_NAME"
  rm -rf "$VENV_NAME"
fi

# 3. Create new environment
echo "🐍 Creating new environment with $PYTHON_PATH..."
"$PYTHON_PATH" -m venv "$VENV_NAME"

# 4. Activate the new venv
source "$VENV_NAME/bin/activate"

# 5. Upgrade pip
echo "⬆️  Upgrading pip..."
python -m pip install --upgrade pip

# 6. Install requirements if available
if [ -f "$REQ_FILE" ]; then
  echo "📦 Installing dependencies from $REQ_FILE..."
  pip install -r "$REQ_FILE"
else
  echo "⚠️  No requirements.txt found — skipping package installation."
fi

echo "✅ Virtual environment setup complete!"
echo "💡 To activate it later, run: source $VENV_NAME/bin/activate"

