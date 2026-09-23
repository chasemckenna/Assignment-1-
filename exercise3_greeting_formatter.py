# Exercise 3: Customer Greeting Formatter
# Concept: strings, functions, parameters, defaults, return values


def format_greeting(name, title="Customer"):
    # strip() removes extra spaces before and after the input
    cleaned_name = name.strip()

    # If the user leaves the name blank, return a default greeting
    if cleaned_name == "":
        return "Hello, Valued Customer!"

    # title() capitalizes each word, such as "john doe" -> "John Doe"
    formatted_name = cleaned_name.title()

    # split() separates the full name into words, so we can use the first name
    first_name = formatted_name.split()[0]

    return f"Hello, {first_name} ({title})!"


def main():
    full_name = input("What's your full name? ")
    print(format_greeting(full_name))


if __name__ == "__main__":
    main()
