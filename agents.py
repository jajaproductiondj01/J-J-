import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_xai import ChatXAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Agents
grok = Agent(
    role="Chef d'Orchestre Musical & Prompt Engineer",
    goal="Coordonner toute l'équipe et créer des prompts Suno parfaits",
    backstory="Expert en production EDM, tech house, bass house. Très bon pour structurer les tracks.",
    llm=ChatXAI(model="grok-3", api_key=os.getenv("GROK_API_KEY")),
    verbose=True
)

claude = Agent(
    role="Compositeur Créatif & Raffineur",
    goal="Améliorer les idées musicales, ajouter de l'émotion et de la complexité",
    backstory="Style Claude : très créatif, bon en storytelling musical et mélodies.",
    llm=ChatAnthropic(model="claude-3-5-sonnet-20240620", api_key=os.getenv("ANTHROPIC_API_KEY")),
    verbose=True
)

gemini = Agent(
    role="Expert Technique & Mastering",
    goal="Optimiser la technique, le mastering, les variations et l'énergie club",
    backstory="Très bon en analyse technique et conseils de production pro.",
    llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=os.getenv("GEMINI_API_KEY")),
    verbose=True
)
