# 01. VARIABLES & STRINGS
name = 'Harsh'
role = 'AI Automation Trainee'
print(name)
print(role)

# 2. NUMBERS
experience_years = 0
daily_hours = 4
print(experience_years + daily_hours)

# 3. LISTS
skills = ['SQL', 'Make', "n8n" , "Prompt Engineering"]
print(skills[0])        # First Item
print(skills[-1])       # Last Item
print(len(skills))       # How many items

# 4. DICTIONARIES
applicant = {
    "name": "Harsh",
    "role" : "AI Automation",
    "skills" : ["SQL", "n8n"],
    "status" : "In-Training"
}
print(applicant["name"])
print(applicant["skills"])
print(applicant["status"])
