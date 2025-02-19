import os
from dotenv import load_dotenv
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Error: Please set your OpenAI API key as an environment variable.")
    exit(1)

load_dotenv()
openai.api_key = OPENAI_API_KEY

knowledge_base = {
    "loan eligibility": "Loan eligibility depends on income, credit score, and repayment history.",
    "kyc process": "KYC (Know Your Customer) requires valid ID proof, address proof, and income proof.",
    "interest rates": "Interest rates vary based on lender policies, creditworthiness, and loan tenure.",
    "loan default": "If you default on a loan, it affects your credit score and may lead to legal consequences.",
    "microfinance": "Microfinance provides small loans to low-income individuals without traditional banking access."
}

def get_ai_response(query):
    for key, answer in knowledge_base.items():
        if key in query.lower():
            return answer

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": query}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the AI Micro-Finance Chatbot!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        response = get_ai_response(user_input)
        print("\nBot:", response, "\n")

if __name__ == "__main__":
    main()
