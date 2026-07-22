# # # # # from agent.agent import Agent

# # # # # agent = Agent("models/llama-3-8b-instruct.gguf")
# # # # # # response = agent.simple_generate("write a poem about the trees")
# # # # # response = agent.generate_with_role("What is an AI agent?")
# # # # # print(response)

# # # # from agent.agent import Agent

# # # # agent = Agent("models/llama-3-8b-instruct.gguf")

# # # # schema = '''
# # # # {
# # # #   "topic": string,
# # # #   "description':string
# # # #   "difficulty": "beginner" | "intermediate" | "advanced"
# # # # }
# # # # '''

# # # # result = agent.generate_structured(
# # # #     "Explain quantum computing",
# # # #     schema
# # # # )

# # # # print(result)
# # # # # {"topic": "'quantum computing", "difficulty": "advanced"}


# # # from agent.agent import Agent

# # # agent = Agent("models/llama-3-8b-instruct.gguf")

# # # decision = agent.decide(
# # #     "Can you eat with me and dance with a fork?",
# # #     choices=["answer_question", "summarize_text", "translate" , 'text-to-spech' , 'None of the Above']
# # # )

# # # print(decision)
# # # # Output: "summarize_text"


# # from agent.agent import Agent

# # agent = Agent("models/llama-3-8b-instruct.gguf")

# # tool_call = agent.request_tool("How's the weather in Spain?")
# # print(f"Tool request: {tool_call}")

# # if tool_call:
# #     result = agent.execute_tool_call(tool_call)
# #     print(f"Tool result: {result}")
# from agent.agent import Agent

# agent = Agent("models/llama-3-8b-instruct.gguf")

# print("\nNote: Repetition in early iterations is expected.")
# print("The agent refines its understanding step by step and may repeat analysis")
# print("before converging on a clearer explanation.\n")

# results = agent.run_loop("Help me understand loops", max_steps=3)
# print(results)
# for i, result in enumerate(results, 1):
#     print(f"Iteration {i}:")
#     action = result.get("action", "unknown")
#     reason = result.get("reason", "No reason provided")
#     print(f"  Action: {action}")
#     print(f"  Reason: {reason}")
#     if i < len(results):
#         print()


# from agent.agent import Agent

# agent = Agent("models/llama-3-8b-instruct.gguf")

# # First interaction - store name
# response1 = agent.run_with_memory("My name is Alice")
# if response1 and "reply" in response1:
#     print(f"Response 1: {response1['reply']}")

# # Second interaction - recall name
# response2 = agent.run_with_memory("What's my name?")
# if response2 and "reply" in response2:
#     print(f"Response 2: {response2['reply']}")

# # print(f"Memory contents: {agent.memory.get_all()}")

# from agent.agent import Agent

# agent = Agent("models/llama-3-8b-instruct.gguf")

# plan = agent.create_plan("Write a blog post about AI agents")
# print(f"Plan: {plan}")

# if plan:
#     results = agent.execute_plan(plan)
#     print(f"Execution results: {results}")
# from agent.agent import Agent

# agent = Agent("models/llama-3-8b-instruct.gguf")

# # Convert a plan step into an atomic action
# step = "Write an explanation of AI agents"
# atomic_action = agent.create_atomic_action(step)
# print(f"Step: {step}")
# print(f"Atomic action: {atomic_action}")

# # Example with a step from a plan
# plan = agent.create_plan("Create a tutorial about Python")
# if plan and "steps" in plan and plan["steps"]:
#     first_step = plan["steps"][0]
#     print(plan)
#     atomic_action_from_plan = agent.create_atomic_action(first_step)
#     print(f"\nPlan step: {first_step}")
#     print(f"Atomic action from plan step: {atomic_action_from_plan}")

from agent.agent import Agent

agent = Agent("models/llama-3-8b-instruct.gguf")

graph = agent.create_aot_plan("Research and write article")
print(f"AoT graph: {graph}")

if graph:
    results = agent.execute_aot_plan(graph)
    print(f"Execution results: {results}")