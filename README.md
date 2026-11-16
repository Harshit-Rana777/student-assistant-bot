# AI Study Assistant Chatbot

A simple command-line Study Assistant chatbot built with Python, LangChain, and Google Gemini.

## Setup Instructions

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key:**
   Add your Gemini API key inside the `.env` file:
   ```env
   GOOGLE_API_KEY=your_actual_api_key
   ```

4. **Run the Chatbot:**
   ```bash
   python app.py
   ```
