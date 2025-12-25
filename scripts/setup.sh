#!/bin/bash
# setup.sh

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🎭 Installing Playwright browsers..."
playwright install webkit

echo "🔑 Creating secret key..."
python create_secret_key.py

echo "✅ Setup complete! Run with: python app.py"
