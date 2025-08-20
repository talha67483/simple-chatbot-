from agents import Agent,Runner,RunConfig,OpenAIChatCompletionsModel,AsyncOpenAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("BASE_URL")
gemini_ai_model = os.getenv("AI_MODEL")



external_client = AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_base_url)

Model = OpenAIChatCompletionsModel(openai_client=external_client,model=gemini_ai_model)



ai_agent = Agent(
    name="simple agent",
    instructions="You are simple agent  "
)


