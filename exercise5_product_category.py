product = input("What's the product name? ").strip().lower()
 
match product:
    case "electronics" | "gadget":
        category = "High Margin"
    case _ if product.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"
 
print(f"Product: {product} | Category: {category}")