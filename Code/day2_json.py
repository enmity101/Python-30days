import json

# Simulated raw API response (this is what LLMs return)
raw_response = '{"id": "msg_01", "role": "assistant", "content": "Meeting confirmed for 3pm.", "tokens": 120}'

# Parse it
parsed = json.loads(raw_response)

# Navigate it
print(parsed["content"])
print(parsed["tokens"])

# Convert Python dict back to JSON string
my_data = {"name": "Harsh", "score": 95}
json_string = json.dumps(my_data)
print(json_string)
print(type(json_string))