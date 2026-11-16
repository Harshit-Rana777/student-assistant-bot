import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def create_study_assistant():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Create a .env file in the project root with:\n"
            "GOOGLE_API_KEY=your_actual_api_key"
        )

    # Initialize the Gemini language model
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=api_key,
    )

    # Create a prompt template tailored for a Study Assistant
    template = """
    You are a helpful and encouraging Study Assistant. 
    Explain the concept or answer the student's question clearly using simple language, 
    bullet points, and a short example if helpful.

    Student's Question: {question}

    Study Assistant Answer:
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )

    # Combine prompt and model into a chain
    chain = prompt | llm
    return chain

def main():
    print("==========================================")
    print("📚 Welcome to the AI Study Assistant! 📚")
    print("Type 'exit' or 'quit' to stop.")
    print("==========================================\n")

    try:
        assistant_chain = create_study_assistant()
    except Exception as e:
        print(f"Setup Error: {e}")
        return

    while True:
        try:
            user_question = input("Ask a study question: ").strip()

            if user_question.lower() in ["exit", "quit"]:
                print("Goodbye! Happy studying!")
                break

            if not user_question:
                print("⚠️ Please enter a valid question.\n")
                continue

            print("\nThinking...\n")
            response = assistant_chain.invoke({"question": user_question})
            print("💡 Answer:\n")
            print(response.content)
            print("\n" + "-" * 42 + "\n")

        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred while generating the answer: {e}\n")

if __name__ == "__main__":
    main()

