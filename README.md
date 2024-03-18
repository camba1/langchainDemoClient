# Clients for the LangChain demo

This repo serves as the companion to the [langChainDemo repo](https://github.com/camba1/langChainDemo). It is used to show simple alternatives to consume the APIs 
exposed when LangServe is running. This repo expects to be able to connect to the inference endpoints running 
at 127.0.0.1:8000

## Installing dependencies

Install Poetry following the instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer).
Install all the dependencies and activate your environment

```bash
poetry install
poetry shell
```

## Sample UIs

### CLI
To run the different flavors of the "/simple" endpoint, just run `python langchaindemoclient/main.py` Responses will be
logged to the console

### Web Uis
There are 3 simple Web UIs available using 3 different frameworks:
- **Streamlit**: Run the UI with `streamlit run webUI/streamlitChatBot.py`
- **Gradio**: Execute the following command to run the UI: `python webUI/gradioChatbot.py`
- **chainlit**: Run the commands 
```shell
    cd webUI/chainlit
    chainlit run --port 8080 chainlitChatBot.py 
```

## Useful Resources

- LangSmith Docs: https://docs.smith.langchain.com/tracing
- Langserve Application templates: https://templates.langchain.com
- LangChain Hub: https://smith.langchain.com/hub
- LangChain Python documentation: https://python.langchain.com/
- LangChain JS documentation: https://js.langchain.com
- Blog: https://blog.langchain.dev/
- Discord: https://discord.gg/cU2adEyC7w
- Repo for this demo: 
  - Backend: https://github.com/camba1/langChainDemo
  - Frontend: https://github.com/camba1/langchainDemoClient 
