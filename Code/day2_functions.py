# Basic Function
def greet(name):
    return f"Hello, {name}"

print(greet('Harsh'))

# Fuction with multiple inputs
def describe_role(name, role):
    return f"{name} is applying for the role of {role}"

print(describe_role('Harsh', 'Data Scientist'))

# Function that returns a dictionary
def build_profile(name, role):
    return{
        'name' : name,
        'role' : role,
        'status' : 'active'
    }

profile = build_profile('Harsh', 'Data Scientist')
print(profile)
print(profile['status'])