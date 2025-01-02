# Exam Assistant - Automated Question Answering Tool

## Overview
The **Exam Assistant** is a Python-based tool designed to assist with answering questions during exams. It leverages speech recognition, text-to-speech, and an external API to provide quick and accurate responses to spoken questions. This project is intended for educational purposes and demonstrates the integration of various technologies to create a functional assistant.

## Features
- **Speech Recognition**: Converts spoken questions into text using Google Web Speech API.
- **Text-to-Speech**: Provides audible responses to the user.
- **API Integration**: Connects to an external API to fetch answers based on the user's query.
- **Asynchronous Processing**: Ensures smooth and efficient handling of API requests.
- **Confirmation Mechanism**: Allows users to confirm or change their questions before processing.

## Installation
To use the Exam Assistant, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/exam-assistant.git
   cd exam-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**:
   - Replace the `API_KEY` variable in the script with your actual API key.

4. **Run the Script**:
   ```bash
   python exam_assistant.py
   ```

## Usage
1. **Speak Your Question**: When prompted, speak your question clearly into the microphone.
2. **Confirm the Question**: The assistant will repeat your question and ask for confirmation.
3. **Receive the Answer**: If confirmed, the assistant will fetch and speak the answer.

## Requirements
- Python 3.7+
- `speech_recognition` library
- `pyttsx3` library
- `aiohttp` library
- `asyncio` library

## Disclaimer
This project is intended for educational purposes only. Using this tool to cheat in exams is unethical and against academic integrity. The creator does not condone or encourage the use of this tool for dishonest purposes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or feedback, please contact EKAMJOT at [ekamjotsing002@gmail.com]

---

**Note**: This project is a demonstration of integrating various technologies and should be used responsibly.
