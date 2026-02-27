'''Write a dictionary for a **fake job application** with these exact keys: `name`, `role`, `skills` (a list of at least 3), `status`. Then write a loop that prints each key and its value on a separate line like this:
'''
# name: Harsh
# role: AI Automation Executive
# skills: ['SQL', 'n8n', 'Make']
# status: Applied

name = 'Harsh'
role = 'AI Automation Executive'
skills = ['SQL', 'n8n', 'Make']
status = 'Applied'
job_application = {
    "name": name,
    "role": role,
    "skills": skills,
    "status": status
}
for key, value in job_application.items():
    print(f"{key}: {value}")