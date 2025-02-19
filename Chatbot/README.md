AI Micro-Finance Chatbot 
A simple terminal-based AI chatbot that educates borrowers and answers compliance-related queries using OpenAI's GPT-4.

Features
Educates borrowers on loans, KYC, and financial terms
 Provides compliance-related answers (e.g., AML, ESG factors)
 Uses OpenAI’s GPT-4 for AI-generated responses
 Checks a predefined knowledge base for instant replies
 Terminal-based chatbot for quick and easy access

📌 Installation
1️⃣ Prerequisites
Python 3.7+
OpenAI API Key (Required)
2️⃣ Install Required Libraries
Run the following command in your terminal:
pip install openai

3️⃣ Set Your OpenAI API Key
Before running the chatbot, set your OpenAI API key as an environment variable:
For Windows (Command Prompt)
set OPENAI_API_KEY="your_openai_key"

For macOS/Linux (Terminal)
export OPENAI_API_KEY="your_openai_key"


📜 Usage
Run the chatbot script using:
python chatbot.py

Then, enter your questions related to micro-finance, loans, and compliance. Type "exit" to quit.

💡 Example Queries
User Query
Bot Response
What is KYC?
KYC (Know Your Customer) requires valid ID proof, address proof, and income proof.
How do I check my loan eligibility?
Loan eligibility depends on income, credit score, and repayment history.
What happens if I default on a loan?
Defaulting on a loan affects your credit score and may lead to legal consequences.
How does microfinance help small businesses?
Microfinance provides small loans to individuals without access to traditional banking.


🛠️ How It Works
Checks the knowledge base first for common queries.
If no match is found, it sends the query to OpenAI's GPT-4.


🔧 Troubleshooting
🔹 Error: "ModuleNotFoundError: No module named 'openai'"
 → Run pip install openai to install the missing dependency.
🔹 Error: "OpenAI API key not set"
 → Make sure your OpenAI API key is properly set using set (Windows) or export (macOS/Linux).
🔹 Error: "HTTPSConnectionPool error"
 → Check your internet connection and try updating the openai package:
pip install --upgrade openai urllib3


