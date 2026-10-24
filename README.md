# Liang Hao Chatbot
### First experimental AI Engineering Project: Local Chatbot based on Ollama Deepseek and Chainlit for the web-based chat UI

## Install Dependency
```powershell
# Download and install Ollama in Windows
irm https://ollama.com/install.ps1 | iex

# Pull DeepSeek-R1:1.5b model (a lighter version of deepseek-r1)
ollama pull deepseek-r1:1.5b

# Install dependencies
pip install pydantic==2.10.1 chainlit ollama
```

## How to run app
```
chainlit run app.py -w
```

> marcoyap41
