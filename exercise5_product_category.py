product = input("What's the product name? ").strip().lower()

match product:
    case "electronics" | "gadget":
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

# Anything starting with "tech" also counts as High Margin
if product.startswith("tech"):
    category = "High Margin"

print(f"Product: {product} | Category: {category}")