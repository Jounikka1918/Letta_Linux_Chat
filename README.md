# Letta GUI Chat Application

A simple GUI application for chatting with Letta AI using Tkinter.

## Features

- Simple and intuitive chat interface
- Real-time communication with Letta AI
- Scrollable chat history
- Power button to quit the application

## Requirements

- Python 3.6+
- tkinter (usually comes with Python)
- requests library

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure your Letta AI server is running on localhost:8283
2. Update the `AGENT_ID` in `letta_gui.py` with your agent ID
3. Run the application:
   ```bash
   python letta_gui.py
   ```

## Configuration

- **AGENT_ID**: Replace with your actual agent ID in the code
- **API_URL**: Modify if your Letta server runs on a different address/port
- **Authorization**: Uncomment and set if your server requires authentication

## File Structure

- `letta_gui.py`: Main application file
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (optional)
