import random

# "js", "py", "java", "c#", "php"
available_stacks = [
    {
        "leng": "Node",
        "frontend": ["React", "Angular", "Svelte", "Vue"],
        "backend": ["Nest.js", "Express"],
        "dbs": ["Postgresql", "Oracle", "Mongo"]
    },
    {
        "leng": "Python",
        "frontend": ["React", "Angular", "Svelte", "Vue"],
        "backend": ["Django", "FastApi"],
        "dbs": ["Postgresql", "Oracle", "Mongo"]
    },
    {
        "leng": "Php",
        "frontend": ["React", "Angular", "Svelte", "Vue"],
        "backend": ["Laravel", "Symfony"],
        "dbs": ["Postgresql", "Oracle", "Mongo", "MySql"]
    },
    {
        "leng": "Java 11",
        "frontend": ["React", "Angular", "Svelte", "Vue"],
        "backend": ["Springboot/Jakarta EE", "Springboot/SE"],
        "dbs": ["Postgresql", "Oracle", "Mongo"]
    },
    {
        "leng": "C#",
        "frontend": ["React", "Angular", "Svelte", "Vue"],
        "backend": ["ASP.NET Core"],
        "dbs": ["Postgresql", "Microsoft SQL Server", "Mongo"]
    },
]

stack = []

def elm_picker(list):
    return list[random.randint(0, (len(list) - 1))]

for k, v in elm_picker(available_stacks).items():    
    if isinstance(v, list):
        stack.append(elm_picker(v))
    else:
        stack.append(v)

print("Welcome to random tech stack generator!:")
print("Your stack is:\n")
print(stack)

