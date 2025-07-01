import os
import shutil

# Define the project structure with the correct paths
project_files = {
    "__main__.py": "from app import main\n\nif __name__ == '__main__':\n    main()",
    "app.py": "def main():\n    print(\"Launching ChessChat TUI\")",
    "core/controller.py": "class Controller:\n    '''Main controller for handling user input and routing.'''\n    def handle_input(self, input_text):\n        pass",
    "core/state.py": "class AppState:\n    '''Singleton-like state manager for global app state.'''\n    _instance = None\n\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n            # Initialize state variables here\n        return cls._instance",
    "core/spellcheck.py": "import subprocess\n\ndef check_spelling(text):\n    '''Check spelling using aspell and return a set of misspelled words.'''\n    p = subprocess.Popen(['aspell', 'list'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)\n    stdout, _ = p.communicate(text)\n    return set(stdout.splitlines())",
    "core/models.py": "from dataclasses import dataclass\n\n@dataclass\nclass Message:\n    user: str\n    content: str\n\n@dataclass\nclass User:\n    name: str\n    status: str = 'online'",
    "ui/layout.py": "class Layout:\n    '''Compose the full terminal UI layout.'''\n    def compose(self):\n        pass",
    "ui/chat_window.py": "class ChatWindow:\n    '''Main chat display widget.'''\n    def display_message(self, message):\n        pass",
    "ui/input_box.py": "class InputBox:\n    '''Handles user text input and triggers spellcheck.'''\n    def get_input(self):\n        pass",
    "ui/channel_list.py": "class ChannelList:\n    '''Sidebar list of joined or available channels.'''\n    def update(self, channels):\n        pass",
    "ui/friend_list.py": "class FriendList:\n    '''Sidebar list of friends and their statuses.'''\n    def update(self, friends):\n        pass",
    "ui/board_view.py": "class BoardView:\n    '''ASCII-based chess board viewer.'''\n    def render(self, board_state):\n        pass",
    "net/fics_client.py": "class FICSClient:\n    '''Handles connection to the Free Internet Chess Server.'''\n    def connect(self):\n        pass",
    "net/lichess_client.py": "class LichessClient:\n    '''Handles connection to Lichess via WebSocket.'''\n    def connect(self):\n        pass",
    "net/protocol.py": "class ServerMessage:\n    '''Unified format for server messages.'''\n    def parse(self, raw_text):\n        pass",
    "config/settings.py": "CONFIG = {\n    'server': 'fics',\n    'spellcheck': True,\n    'theme': 'default',\n}",
    "utils/logger.py": "def setup_logger():\n    '''Set up and return a logger instance.'''\n    pass",
    "utils/helpers.py": "def truncate(text, max_length):\n    '''Truncate long text with ellipsis.'''\n    return text if len(text) <= max_length else text[:max_length - 3] + '...'",
    "tests/test_spellcheck.py": "from core import spellcheck\n\ndef test_check_spelling():\n    result = spellcheck.check_spelling(\"Ths sentnce has errrs.\")\n    assert \"Ths\" in result\n    assert \"errrs\" in result"
}

# Create files in the correct structure
for path, content in project_files.items():
    full_path = os.path.join("chesschat", path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("✅ Project restructured successfully.")