# 📰 AI Newsletter Generator

An end-to-end LLM-powered AI Newsletter Generator built using LLaMA-3, CrewAI, and the Google Serper API. This app takes a user-defined topic and uses a team of autonomous agents to research, fact-check, and generate a well-structured newsletter with real-time information.

---

## 🚀 Features

- Accepts a topic from the user
- Utilizes CrewAI to coordinate multiple LLM agents
- Integrates Google Serper API for real-time search
- Generates well-structured, fact-checked newsletter content
- Powered by LLaMA-3 through LangChain and langchain-groq

---

## 📦 Install Dependencies

Make sure you have [Pipenv](https://pipenv.pypa.io/en/latest/installation.html) installed.

Then run the following commands in your terminal:

pipenv install crewai
pipenv install langchain_groq
pipenv install crewai_tools

---

## ▶️ Run the App
pipenv run python crew.py

---

## 🛠️ Tech Stack

- **LLaMA-3** – LLM for generating and refining content
- **CrewAI** – Framework for multi-agent task coordination
- **LangChain + langchain-groq** – For LLM orchestration and interaction
- **CrewAI Tools** – Prebuilt tools for search and analysis
- **Google Serper API** – Real-time web search results
- **Pipenv** – Dependency and environment management
