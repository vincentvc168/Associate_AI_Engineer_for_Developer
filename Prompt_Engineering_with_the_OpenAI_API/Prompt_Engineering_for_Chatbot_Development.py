client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "Ask the user for their order number if they submitted a query about an order without specifying an order number"

# Define the technical issue condition
technical_issue_condition = "start the response with I'm sorry to hear about your issue with ... if the user is reporting a technical issue"

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)

---
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks. You should respond to user queries in a gentle way.
 ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)
