def format_greeting(name, title="Customer"):
    name = name.strip()          # strip() removes extra spaces

    if name == "":               # handle empty input
        return "Hello, Valued Customer!"

    name = name.title()          # title() capitalizes each word
    first_name = name.split()[0] # split() breaks it into words; [0] takes the first one
    return f"Hello, {first_name} ({title})!"


full_name = input("What's your full name? ")
print(format_greeting(full_name))
