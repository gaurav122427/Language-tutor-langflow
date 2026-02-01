import gradio as gr
from langflow.interface import load_flow_from_json

# Load your exported flow
flow = load_flow_from_json("flow.json")

def tutor_chat(user_input):
    # Run your LangFlow flow with the input
    response = flow.run({"input": user_input})
    return response

# Simple Gradio UI
iface = gr.Interface(
    fn=tutor_chat,
    inputs="text",
    outputs="text",
    title="AI Language Tutor",
    description="Corrects grammar, explains errors, and gives practice questions"
)

iface.launch()
