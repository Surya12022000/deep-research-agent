# Deep Research Agent

A production-ready AI-powered research system built with OpenAI's Agents SDK. This multi-agent system conducts comprehensive web research, synthesizes findings, and delivers detailed reports.

## Features

- **Multi-Agent Architecture**: Specialized agents working together
  - **Planner Agent**: Strategizes search queries
  - **Search Agent**: Performs parallel web searches
  - **Writer Agent**: Synthesizes comprehensive reports
  - **Email Agent**: Delivers results via email
- **Parallel Processing**: Executes multiple searches simultaneously for faster results
- **Structured Outputs**: Uses Pydantic models for reliable data handling
- **Web Interface**: Beautiful Gradio UI for easy interaction
- **Tracing**: Full visibility into agent behavior via OpenAI platform

## Architecture

```
Research Manager
    ├── Planner Agent → Creates 5 search strategies
    ├── Search Agent × 5 (Parallel) → Performs web searches
    ├── Writer Agent → Synthesizes detailed markdown report
    └── Email Agent → Sends HTML email via SendGrid
```

## Requirements

- Python 3.10+
- OpenAI API key
- SendGrid API key (for email functionality)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd deep-research-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
SENDGRID_API_KEY=your_sendgrid_api_key_here
SENDGRID_FROM_EMAIL=your_verified_sender@example.com
SENDGRID_TO_EMAIL=recipient@example.com
```

## Usage

### Run the Web Interface

```bash
cd src
python app.py
```

The Gradio interface will open in your browser automatically. Enter your research query and click "Run Research".

### Use as a Library

```python
from research_manager import ResearchManager
import asyncio

async def research():
    manager = ResearchManager()
    async for update in manager.run("Latest developments in quantum computing"):
        print(update)

asyncio.run(research())
```

## Configuration

### Customizing Search Count

Edit `src/planner_agent.py` and modify the `HOW_MANY_SEARCHES` constant:

```python
HOW_MANY_SEARCHES = 5  # Change to your desired number
```

### Changing Models

Each agent can use different models. Edit the respective agent files:

```python
# In planner_agent.py, search_agent.py, writer_agent.py, or email_agent.py
agent = Agent(
    name="AgentName",
    model="gpt-4o-mini",  # Change to gpt-4o, gpt-4-turbo, etc.
    ...
)
```

### Adjusting Report Length

Edit `src/writer_agent.py` and modify the instructions:

```python
INSTRUCTIONS = (
    "...Aim for 5-10 pages of content, at least 1000 words."  # Customize as needed
)
```

## How It Works

1. **Planning Phase**: The Planner Agent analyzes your query and generates 5 strategic search queries with reasoning
2. **Search Phase**: The Search Agent performs all searches in parallel, summarizing results into 2-3 paragraphs each
3. **Writing Phase**: The Writer Agent synthesizes all findings into a comprehensive markdown report (1000+ words)
4. **Delivery Phase**: The Email Agent converts the report to HTML and sends it via SendGrid

## Project Structure

```
deep-research-agent/
├── src/
│   ├── app.py                  # Gradio web interface
│   ├── research_manager.py     # Main orchestrator
│   ├── planner_agent.py        # Search strategy planner
│   ├── search_agent.py         # Web search executor
│   ├── writer_agent.py         # Report synthesizer
│   └── email_agent.py          # Email delivery
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Tracing and Debugging

Each research run generates a trace URL that appears in the console:

```
View trace: https://platform.openai.com/traces/trace?trace_id=...
```

Visit this URL to see detailed agent interactions, tool calls, and decision-making processes.

## SendGrid Setup

1. Sign up for a free SendGrid account at https://sendgrid.com
2. Verify a sender email address in SendGrid
3. Generate an API key with "Mail Send" permissions
4. Add credentials to your `.env` file

## Troubleshooting

### "No module named 'agents'"
Install the OpenAI Agents SDK:
```bash
pip install git+https://github.com/openai/openai-agents-sdk.git
```

### Email not sending
- Verify your SendGrid API key is correct
- Ensure sender email is verified in SendGrid
- Check SendGrid dashboard for error logs

### Search results are empty
- Verify your OpenAI API key has access to web search tools
- Check your OpenAI account usage limits

## Cost Considerations

- Uses `gpt-4o-mini` by default for cost efficiency
- Typical research run: 5 searches + report generation ≈ $0.10-0.30
- Upgrade to `gpt-4o` for higher quality results (higher cost)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

Built with [OpenAI Agents SDK](https://github.com/openai/openai-agents-sdk) and [Gradio](https://gradio.app/).
