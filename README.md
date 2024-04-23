# File-Reader-Application

This is a simple Flask web application that reads text files from a directory and displays their content in a web browser.

# Features
- Reads text files from a specified directory.
- Automatically detects the encoding of the text files.
- Allows specifying start and end lines to display a specific range of lines from the file.

# Prerequisites
- Python 3.x
- Flask
- chardet

# Installation
1. Clone the repository:
- git clone https://github.com/OmkarBakare17/File-Reader-Application.git

2. Install dependencies:
- pip install -r requirements.txt

# Usage
1. Navigate to the project directory:
- cd File-Reader-Application

2. Run the Flask application:
- python main.py

3. Open a web browser and go to http://127.0.0.1:5000/file1.txt

4. Optionally, you can specify start and end line numbers as query parameters:
- http://127.0.0.1:5000/file1.txt?start_line=1&end_line=10

# Acknowledgments
- This project uses the Flask web framework.
- Text encoding detection is performed using the chardet library.
