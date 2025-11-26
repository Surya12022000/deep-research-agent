import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research Agent")
    gr.Markdown("Enter a research topic and let the AI agents conduct comprehensive research for you.")
    query_textbox = gr.Textbox(label="What topic would you like to research?", placeholder="e.g., Latest developments in quantum computing")
    run_button = gr.Button("Run Research", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

if __name__ == "__main__":
    ui.launch(inbrowser=True)
