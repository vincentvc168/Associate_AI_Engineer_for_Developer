client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"transforms sample email delimited by triple backticks by changing its tone to be professional, positive, and user-centric. ```{sample_email}```

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)
