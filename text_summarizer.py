import requests
import gradio as gr
from fastapi import FastAPI

OLLAMA_URL = "http://localhost:11434/api/generate"


def summarize_text(text):
    """
    Using  the llm summarize the given text
    :param text:  to summarize
    """

    payload = {
        "model": "llama3.2",
        "prompt": f"Summarize the following text, including all key points and important details.\n\n{text}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error occurred {response.text}"


# Using gradio interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs=gr.Textbox(label="Summarized text"),
    title="AI Powered Text Summarizer",
    description="Enter a long text and the AI will generate a concise summary"
)
interface.launch()

# Using FasAPI
app = FastAPI()


@app.post("/summarize/")
def summarize_text_api(text: str):
    return summarize_text(text)

# Run with: uvicorn app:app --reload
