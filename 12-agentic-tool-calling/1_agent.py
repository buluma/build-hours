from agents import Agent, function_tool
from utils import run_demo_loop


agent = Agent(
    name="Assistant",
    model="o3-mini",
)

run_demo_loop(agent)
