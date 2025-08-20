import chainlit as cl
from main import ai_agent,Model,external_client
from agents import Runner,RunConfig,SQLiteSession
from openai.types.responses import ResponseTextDeltaEvent


# this one is also a method for adding previous conversation to in ai agent
# @cl.on_chat_start
# async def handle_chat_start():
#     cl.user_session.set('history',[])
#     await cl.Message(content="Hello there").send()

    # history.append({"role":"assistant","content":result.final_output}) 
    # cl.user_session.set("history",history)

#------------------------------------------------------------------------
@cl.on_message
async def main(message:cl.Message):
    # history = cl.user_session.get('history')
    # history.append({"role":"user","content":message.content})

    my_session = SQLiteSession("session_123","conversation.db")   # for state in agent adding previous conversation 
    prompt = message.content 
    config = RunConfig(model=Model,model_provider=external_client,tracing_disabled=True) 

    
    result = Runner.run_streamed(ai_agent, prompt,run_config=config,session=my_session)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
                await cl.Message(content=event.data.delta).send()


