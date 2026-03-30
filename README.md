<div align="center">

# CodeCraft

**Transform your code into beautiful, shareable images with syntax highlighting**

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-red.svg)
![Playwright](https://img.shields.io/badge/Playwright-1.40+-45ba4b.svg)
![Platform](https://img.shields.io/badge/platform-MacOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)

![CodeCraft Demo](src/docs/UI.png)

</div>

<hr> 

<div align="center">

## Features

</div>

- **Modern UI/UX** - Glassmorphism design with smooth animations and rounded corners
- **Syntax Highlighting** - Support for 500+ programming languages via Pygments
- **Multiple Themes** - Choose from dozens of pre-designed color schemes
- **High-Quality Screenshots** - Export code as high-resolution PNG images with 2x resolution
- **Fast & Lightweight** - Built with Flask and Playwright for optimal performance
- **Secure** - Session-based authentication with encrypted cookies
- **Responsive Design** - Works seamlessly on desktop, tablet and mobile devices
- **Dark Mode Optimized** - Easy on the eyes with modern dark theme

<hr>

<div align="center">

## Quick Start

</div>

```bash
# Clone the repository
git clone https://github.com/beri336/CodeCraft.git
cd CodeCraft

# Run setup (recommended)
make setup

# Or manual installation
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip3 install -r requirements.txt
playwright install webkit
python3 scripts/create_secret_key.py

# Start the server
python3 app.py
```

<div align="center">

**Open `http://localhost:8080` in your browser and start creating.**

</div>

<div align="center">

### Access from other devices

</div>

To use the app on other devices in the same network, start the server and look for the address in the terminal output:

```bash
============================================================
🚀 CodeCraft Server Started
============================================================
💻 Local access:    http://localhost:8080
📱 Mobile access:   http://[YOUR-LOCAL-IP]:8080
🌐 Network access:  http://[YOUR-LOCAL-IP]:8080
============================================================
```

<div align="center">

## Installation

### Prerequisites

</div>

- Python 3.8 or higher
- Modern web browser (Chrome 76+, Firefox 70+, Safari 14+)

### Method 1: Using Make (Recommended)

```bash
git clone https://github.com/beri336/CodeCraft.git
cd CodeCraft
make setup
```

### Method 2: Manual Installation

**Step 1:** Clone and navigate

```bash
git clone https://github.com/beri336/CodeCraft.git
cd CodeCraft
```

**Step 2:** Create virtual environment

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

**Step 3:** Install dependencies

```bash
pip3 install -r requirements.txt
```

**Step 4:** Install Playwright browsers

```bash
playwright install webkit
```

**Step 5:** Generate secret key

```bash
python3 scripts/create_secret_key.py
```

**Step 6:** Run the application

```bash
python3 main.py
```

### Method 3: Using pip (Development)

```bash
pip3 install -e .
playwright install webkit
python3 scripts/create_secret_key.py
```

<hr>

<div align="center">

## Usage Guide

### Starting the Application

</div>

```bash
python3 main.py
```

<div align="center">

**The server will start at `http://127.0.0.1:8080`**

</div>

<div align="center">

### Creating Your First Snippet

#### 1. **Code Input Page**

</div>

![Code Input](src/docs/UI.png)

- Paste your code into the text area
- Select your programming language from the dropdown
- Click **Next** to proceed

**Controls:**
- `Reset Session` - Clear input and reset to default
- `Next` - Move to style selection
- `Dropdown` - Choose programming language (Python, Swift, C#, etc.)

<div align="center">

#### 2. **Style Selection Page**

</div>

![Style Selection](<src/docs/Example Download.png>)

- Preview your code with syntax highlighting in real-time
- Choose a color theme from the dropdown (monokai, dracula, github, etc.)
- Click **Create an Image** when satisfied

**Controls:**
- `Back` - Return to code input
- `Create an Image` - Generate high-resolution screenshot
- `Dropdown` - Select color theme

<div align="center">

#### 3. **Download Page**

</div>

![Download Page](<src/docs/Example Download.png>)

- View your beautifully generated image
- Click **Download Your Code Image Here** to save
- Click **Back to Start** to create another snippet

<div align="center">

**Example Output:**

</div>

![Download](<src/docs/Code as Image.png>)

<div align="center">

## Architecture

### Project Structure

</div>

```bash
CodeCraft/
├── README.md                                    # Project documentation
├── config.py                                    # Configuration & constants
├── config.json                                  # Secret key (auto-generated)
├── main.py                                      # Flask application entry point
├── pyproject.toml                               # Project configuration
├── requirements.txt                             # Python dependencies
├── Makefile                                     # Development commands
│
├── services/                                    # Business logic layer
│   ├── __init__.py
│   ├── code_service.py                          # Code input & language handling
│   ├── style_service.py                         # Syntax highlighting & themes
│   └── image_service.py                         # Screenshot generation
│
├── src/
│   ├── utils.py                                 # Playwright screenshot utility
│   ├── static/                                  # Static assets
│   │   ├── style.css                            # Glassmorphism UI styling
│   │   └── icon/
│   │       └── icon.png                         # Application icon
│   ├── templates/                               # Jinja2 templates
│   │   ├── base.html                            # Base template with header & footer
│   │   ├── code_input.html                      # Code entry page
│   │   ├── style_selection.html                 # Theme picker with preview
│   │   └─── image.html                          # Download page
│   ├── docs/                                    # Documentation assets
│   │   ├── Code as Image.png                    # Generated code snippet example
│   │   ├── Example Download.png                 # Download page screenshot
│   │   ├── Example Snippet.png                  # Style selection screenshot
│   │   └── UI.png                               # Main UI screenshot
│   └── scripts/                                 # Utility scripts
│       ├── create_secret_key.py                 # Secret key generator
│       └── setup.sh                             # Automated setup script
│
├── .gitignore                                   # Git ignore rules
└── .venv/                                       # Virtual environment
```

<div align="center">

### Core Components

#### `main.py` - Flask Application Entry Point

</div>

**Routes:**

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Code input page with language selector |
| `/save_code` | POST | Save code and language to session |
| `/reset_session` | POST | Clear session and restore defaults |
| `/style` | GET | Style selection page with preview |
| `/save_style` | POST | Save theme and code preferences |
| `/image` | GET | Generate and display screenshot |

**Key Features:**
- Automatic local IP detection for multi-device network access
- Error handling (404, 500)
- Session-based state management

<div align="center">

#### `config.py` - Configuration & Constants

</div>

**Manages:**
- Default values (placeholder code, styles, languages)
- App configuration (DEBUG, HOST, PORT)
- `load_secret_key()` - Loads cryptographic key from config.json for Flask session signing

<div align="center">

#### `services/` - Modular Business Logic

</div>

**`code_service.py` - Code Input Management**
- `get_all_available_lexers()` - Retrieves all supported programming languages from Pygments
- `prepare_code_context()` - Prepares template context with code metrics (line count, max chars)
- `validate_code_input()` - Sanitizes and validates user code input

**`style_service.py` - Syntax Highlighting**
- `get_all_available_styles()` - Lists all available Pygments themes
- `generate_highlighted_code()` - Applies syntax highlighting to code with selected theme
- `prepare_style_context()` - Generates preview context with CSS definitions and background color

**`image_service.py` - Screenshot Generation**
- `prepare_session_data()` - Extracts session cookies for Playwright authentication
- `generate_code_screenshot()` - Orchestrates browser screenshot capture and base64 encoding
- `prepare_image_context()` - Formats image data for template rendering

<div align="center">

#### `src/utils.py` - Playwright Screenshot Engine

</div>

**Function:** `take_screenshot_from_url(url, session_data)`

High-quality screenshot generation using Playwright WebKit:

1. **Browser Launch** - Headless WebKit with 2x device scale factor (Retina quality)
2. **Session Injection** - Injects session cookies for authentication state
4. **Element Wait** - Waits for `.code` element to be visible before capture
5. **Screenshot** - Captures element with padding and styling
6. **Return** - Returns PNG as bytes for base64 encoding

<div align="center">

#### `src/scripts/create_secret_key.py` - Security Setup

</div>

Generates cryptographically secure secret key for Flask session management:

```json
{
    "SECRET_KEY": "a1b2c3d4e5f6..."
}
```

**Features:**
- Uses `secrets.token_hex()` for cryptographic randomness (32 bytes = 64 hex chars)
- Creates config.json only if it doesn't exist

**Usage:**
```bash
python3 src/scripts/create_secret_key.py
```

<div align="center">

### Templates

</div>

#### `src/templates/base.html`
**Master template** with HTML structure:
- Header with icon and navigation
- Main content block for page-specific content
- Script block for smooth scroll

#### `src/templates/code_input.html`
**Code entry interface:**
- Textarea with syntax placeholder
- Language selector dropdown with all Pygments lexers
- Dynamic sizing based on content (num_lines, max_chars)
- Auto-expanding textarea on input

#### `src/templates/style_selection.html`
**Interactive theme preview:**
- Live code preview with applied highlighting
- Smooth animation on theme change
- Responsive button layout (mobile-optimized)

#### `src/templates/image.html`
**Download interface:**
- One-click download link with descriptive filename
- Empty state handling for missing images

<div align="center">

### Styling

</div>

#### `src/static/style.css` - Modern Design System

**Design: Glassmorphism (Apple-inspired)**

**CSS Variables:**
- Color palette (primary, success, accent with hover states)
- Background colors (dark mode optimized)
- Glass effects (blur, borders, transparency)
- Text colors
- Shadows
- Border radius
- Transitions

**Features:**
- **Glassmorphism** - Semi-transparent backgrounds with backdrop-filter blur
- **Interactive Elements** - Hover animations
- **Accessibility** - High contrast ratios, focus states, screen-reader support
- **Performance** - CSS custom properties for easy theming
- **Smooth Transitions**
- **Responsive Design**
- **Dark Mode**
- **Animations**

<hr>

<div align="center">

## Troubleshooting

### Port Already in Use

</div>

```bash
OSError: [Errno 48] Address already in use
```

**Solution:** Change port in `config.py`:

```py
PORT = 8080
```

<div align="center">

### Secret Key Missing

</div>

```bash
ValueError: A secret key is required to use the session.
```

**Solution:** Generate secret key:

```bash
python3 src/scripts/create_secret_key.py
```

Verify `config.json` exists with valid `SECRET_KEY`.

<div align="center">

### Playwright Browser Missing

</div>

```bash
playwright._impl._errors.Error: Executable doesn't exist at ...
```

**Solution:** Install Playwright browsers:

```bash
playwright install webkit

# Or with system dependencies (Linux)
playwright install --with-deps webkit
```

<hr>

<div align="center">

## Me

[![Project](https://img.shields.io/badge/Project-CodeCraft-blue.svg?style=flat-square&labelColor=orange&logo=github&logoColor=white)](https://github.com/beri336/CodeCraft)

[![Created By](https://img.shields.io/badge/Created_By-beri336-orange?style=flat-square&labelColor=blue&logo=github&logoColor=white)](https://github.com/beri336)
[![Created By](https://img.shields.io/badge/Created_By-berkants-orange?style=flat-square&labelColor=blue&logo=bitbucket&logoColor=white)](https://bitbucket.org/berkants/workspace/projects/DEV)

<hr>

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.


[⬆ Back to Top](#codecraft)

</div>