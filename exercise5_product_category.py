# Exercise 5: Product Category Matcher
# Concept: match-case statements, string methods, conditionals


def categorize_product(product_name):
    # Clean the input: remove extra spaces and convert to lowercase
    cleaned_name = product_name.strip().lower()

    match cleaned_name:
        case "electronics" | "gadget":
            category = "High Margin"
        case _ if cleaned_name.startswith("tech"):
            category = "High Margin"
        case "clothing" | "apparel":
            category = "Medium Margin"
        case "food" | "grocery":
            category = "Low Margin"
        case _:
            category = "Uncategorized - Review Needed"

    return cleaned_name, category


def main():
    product_name = input("What's the product name? ")
    name, category = categorize_product(product_name)
    print(f"Product: {name} | Category: {category}")


if __name__ == "__main__":
    main()
