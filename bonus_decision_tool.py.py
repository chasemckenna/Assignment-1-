def is_profitable(revenue, cost):
    return revenue > cost
 
def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    category = input("What's the product category? ").strip().lower()
 
    match category:
        case "electronics" | "gadget":
            advice = "Reinvest"
        case "clothing" | "apparel":
            advice = "Hold steady"
        case "food" | "grocery":
            advice = "Cut costs"
        case _:
            advice = "Review before investing"
 
    if is_profitable(revenue, cost):
        print(f"Profit: ${revenue - cost:,.2f}")
        print(f"Suggestion: {advice}")
    else:
        print("Not profitable. Do not invest.")
 
main()

