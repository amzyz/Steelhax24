import os
from openai import OpenAI
import pyperclip
from dotenv import load_dotenv

# Load environment variables from key.env file
load_dotenv(dotenv_path="key.env")

# Set up OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OpenAI API key not found in environment variables.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Get content from clipboard
clipboard_content = pyperclip.paste()


# Generate flashcards using the OpenAI GPT model

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Create 9 unnumbered flashcards with the following text in a question and answer format. Format it exactly this way: 'Question: ', 'Answer: '. {clipboard_content}."}
    ]
)

# Extract generated flashcards from the response
generated_flashcards = completion.choices[0].message.content

# Split the flashcards by ...
flashcards_list = generated_flashcards.split('\n')

# Join the flashcards with ##
formatted_flashcards = formatted_flashcards = generated_flashcards.replace("Question: ", "").replace("Answer: ", "").replace("\n\n", "##").replace("\n", "$$")

# Save formatted flashcards to a file
with open("flashcards1.txt", "w") as f:
    f.write(formatted_flashcards)

print("Flashcards saved to 'flashcards1.txt'")