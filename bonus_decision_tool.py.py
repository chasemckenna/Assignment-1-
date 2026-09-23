# Bonus Challenge: Integrated Decision Tool
# Combines functions, conditionals, and match-case logic


def is_profitable(revenue, cost):
    return revenue > cost


def suggest_investment(category):
    match category:
        case "electronics" | "gadget" | "tech":
            return "Reinvest"
        case "clothing" | "apparel":
            return "Review pricing"
        case "food" | "grocery":
            return "Expand distribution"
        case _:
            return "Needs review"


def main():
    revenue = float(input("What's the business revenue? "))
    cost = float(input("What's the business cost? "))
    category = input("What's the category? ").strip().lower()

    if is_profitable(revenue, cost):
        profit = revenue - cost
        recommendation = suggest_investment(category)
        print(f"Profit: ${profit:,.2f}")
        print(f"Recommendation: {recommendation}")
    else:
        print("The business is not profitable right now.")


if __name__ == "__main__":
    main()
