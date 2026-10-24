# Liang Hao Chatbot
### First experimental AI Engineering Project: Local Chatbot based on Ollama Deepseek and Chainlit for the web-based chat UI

## Install Dependency
```powershell
# Download and install Ollama in Windows
irm https://ollama.com/install.ps1 | iex

# Pull DeepSeek-R1 model (takes around 5GB storage)
ollama pull deepseek-r1

# Install dependencies
pip install pydantic==2.10.1 chainlit ollama
```

## How to run app
```
chainlit run app.py -w
```

> marcoyap41
