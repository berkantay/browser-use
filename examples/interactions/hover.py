

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller

load_dotenv()

controller = Controller()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)


task = """
1.On the hover interactions card, move the cursor to the button with text 'Hover Card 1'
2. On the hover interactions card, move the cursor to the button with text 'Hover Card 2'
3. On the hover interactions card, move the cursor to the button with text 'Hover Card 3'
"""
initial_actions = [
	{'open_tab': {'url': 'http://localhost:3000/'}},
]

agent = Agent(task=task, llm=llm,controller=controller, initial_actions=initial_actions, use_vision=True)


async def main():
	history = await agent.run()
	print(history)


if __name__ == '__main__':
	asyncio.run(main())
