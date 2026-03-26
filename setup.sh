#!/bin/bash
echo "🔧 Setting up Insightbot..."

# Create virtual environment
python3.9 -m venv venv

# Activate
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create .env from example if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "⚠️ Created .env file - please add your API key!"
fi

echo "✅ Setup complete! Run: source venv/bin/activate"