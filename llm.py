import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file for API key
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_answer(question, document_list):

    # Combine all the documents into a single string with numbered labels
    full_text = ""
    for i in range(len(document_list)):
        full_text += f"[{i+1}] " + document_list[i][2] + "\n\n"

    # Create the prompt to ask Gemini
    prompt = (
        "You are a smart assistant helping users answer questions using the provided documents.\n"
        "Stick to the title and content of the documents.\n"
        "If the question is not answerable with the documents, say 'I don't know about the topic'.\n"
        "Use citations like [1], [2], etc. to refer to the documents.\n"
        "Question: " + question + "\n\n"
        "Documents:\n" + full_text + "\nAnswer:"
    )

    # Generate the answer using the model
    response = model.generate_content(prompt, generation_config={"temperature": 0.5, "max_output_tokens": 4096})

    final_answer = response.text.strip()

    sources_text = ""
    for i in range(len(document_list)):
        title = document_list[i][0]
        url = document_list[i][1]
        sources_text += f"[{i+1}] [{title}]({url})\n"

    markdown_result = final_answer + "\n\n---\n### Sources\n" + sources_text

    return markdown_result


# if __name__ == "__main__":
#     sample_question = "What is the purpose of the OpenAI API?"
#     docs = [
#         ("OpenAI API Overview", "https://openai.com/api", "The OpenAI API provides access to advanced AI models for various tasks."),
#         ("Developer Docs", "https://platform.openai.com/docs", "It allows developers to integrate AI into their applications."),
#         ("API Features", "https://platform.openai.com/docs/guides/gpt", "The API supports text generation, translation, and summarization.")
#     ]

#     answer, metadata = generate_answer(sample_question, docs)
#     print(answer)
