import requests
import gradio as gr

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


if __name__ == '__main__':
    summary = summarize_text(
        """
        DeepSeek AI is an innovative platform designed to revolutionize the way businesses analyze large datasets.
        By utilizing advanced machine learning algorithms and natural language processing,
        it can quickly extract valuable insights from complex and unstructured data sources.
        This allows companies to make more informed decisions, predict future trends, and improve their overall 
        operational efficiency. DeepSeek AI's user-friendly interface and powerful analytical capabilities make it 
        an indispensable tool for industries ranging from finance to healthcare, helping businesses stay ahead in 
        a competitive market.
        """)

    print(summary)
