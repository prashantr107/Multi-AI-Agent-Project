# ResearchMind: Multi-AI-Agent Research App

ResearchMind is a Streamlit app that researches a topic through a multi-agent pipeline. It searches the web, scrapes a relevant page, drafts a report, and generates a critique.

## Features

- Searches the web with Tavily.
- Scrapes a selected source for additional context.
- Generates a structured report with OpenAI's `gpt-4o-mini` model.
- Reviews the report and provides a score and feedback.
- Displays the results in a Streamlit interface and lets you download the report as Markdown.

## Project Structure

```text
.
|-- agents.py       # LangChain agents and report/critic chains
|-- app.py          # Streamlit application
|-- pipeline.py     # Command-line research pipeline
|-- requirements.txt
|-- tools.py        # Tavily search and web scraping tools
```

## Requirements

- Python 3.12 or newer
- An OpenAI API key with API access and available credits
- A Tavily API key

API usage may incur charges according to your providers' plans. A ChatGPT subscription does not include OpenAI API credits.

## Run Locally

Open PowerShell in the project directory and create a virtual environment:

```powershell
python -m venv .venv
& ".\.venv\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root with your own keys:

```dotenv
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
```

Keep `.env` private. It is excluded from Git by `.gitignore`; never commit or share real API keys.

Start the Streamlit app:

```powershell
python -m streamlit run app.py
```

Open the local URL printed in the terminal, enter a research topic, and select **Run Research Pipeline**.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) and create an app from the repository.
3. Select the deployment branch and set the main file path to `app.py`.
4. In the app's **Advanced settings** or **Manage app → Settings → Secrets**, add your keys as TOML:

   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   TAVILY_API_KEY = "your-tavily-api-key"
   ```

5. Save the secrets and deploy the app.

Do not add `.env` or real keys to the GitHub repository. Anyone who can use a public deployment may trigger API requests using your configured keys, so monitor usage and provider billing.

## Troubleshooting

- **Missing OpenAI credentials:** Add `OPENAI_API_KEY` to Streamlit Cloud Secrets, save, and reboot the app. Make sure it is a root-level TOML entry.
- **OpenAI `429` or insufficient quota:** Check the billing and usage for the OpenAI organization/project associated with the key.
- **`ModuleNotFoundError` or unresolved import:** Install dependencies with `python -m pip install -r requirements.txt` in the same virtual environment selected by VS Code.
- **Tavily authentication error:** Confirm `TAVILY_API_KEY` is set in the local `.env` or Streamlit Cloud Secrets.

## Security

Never commit API keys, `.env` files, or Streamlit `secrets.toml` files. If a key is exposed, revoke it with its provider and replace it with a new one.