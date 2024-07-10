import chainlit as cl
from phidata_assistant import assistant_interface
import asyncio

async def async_generator(gen):
    for item in gen:
        yield item
        await asyncio.sleep(0)  # Allow other tasks to run

@cl.on_chat_start
async def on_chat_start():
    # Initialize the chat session
    cl.user_session.set("assistant", assistant_interface)

@cl.on_message
async def main(message: cl.Message):
    # Get the assistant from the user session
    assistant = cl.user_session.get("assistant")
    
    # Create a new message for the response
    msg = cl.Message(content="", author="Assistant")
    await msg.send()

    # Get the generator from chat_workflow
    gen = assistant.get_response(message.content, stream=True)

    # Convert the synchronous generator to an asynchronous one
    async_gen = async_generator(gen)

    full_response = ""
    async for chunk in async_gen:
        full_response += chunk
        msg.content = full_response
        await msg.update()

@cl.on_stop
def on_stop():
    # Clean up the assistant if needed
    pass