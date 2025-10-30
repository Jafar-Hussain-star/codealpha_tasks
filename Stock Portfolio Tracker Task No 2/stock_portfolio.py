import csv
from datetime import datetime

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 170,
    "META": 320,
    "NVIDIA": 875
}


def display_available_stocks():
    """Display all available stocks and their prices."""
    print("\n" + "=" * 50)
    print("AVAILABLE STOCKS:")
    print("=" * 50)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: ${price}")
    print("=" * 50 + "\n")


def get_portfolio():
    """Get stock portfolio from user input."""
    portfolio = {}
    print("Enter your stock portfolio (type 'done' when finished)")
    print("Format: Stock Name Quantity\n")

    while True:
        user_input = input("Enter stock and quantity (or 'done'): ").strip().upper()

        if user_input == "DONE":
            if not portfolio:
                print("Portfolio is empty! Please add at least one stock.")
                continue
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid format! Please enter stock name and quantity (e.g., AAPL 10)")
            continue

        stock_name, quantity_str = parts

        if stock_name not in STOCK_PRICES:
            print(f"'{stock_name}' not found in available stocks. Please try again.")
            display_available_stocks()
            continue

        try:
            quantity = float(quantity_str)
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
            portfolio[stock_name] = quantity
            print(f"✓ Added {quantity} shares of {stock_name}")
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            continue

    return portfolio


def calculate_portfolio_value(portfolio):
    """Calculate total portfolio value and return detailed breakdown."""
    total_value = 0
    breakdown = []

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        stock_value = price * quantity
        total_value += stock_value
        breakdown.append({
            'stock': stock,
            'quantity': quantity,
            'price': price,
            'value': stock_value
        })

    return total_value, breakdown


def display_portfolio_summary(portfolio, total_value, breakdown):
    """Display portfolio summary."""
    print("\n" + "=" * 60)
    print("PORTFOLIO SUMMARY")
    print("=" * 60)
    print(f"{'Stock':<10} {'Quantity':<12} {'Price':<12} {'Total Value':<12}")
    print("-" * 60)

    for item in breakdown:
        print(f"{item['stock']:<10} {item['quantity']:<12.2f} ${item['price']:<11.2f} ${item['value']:<11.2f}")

    print("-" * 60)
    print(f"{'TOTAL INVESTMENT VALUE:':<34} ${total_value:,.2f}")
    print("=" * 60 + "\n")


def save_to_txt(portfolio, total_value, breakdown):
    """Save portfolio to a text file."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("STOCK PORTFOLIO TRACKER\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"{'Stock':<10} {'Quantity':<12} {'Price':<12} {'Total Value':<12}\n")
        f.write("-" * 60 + "\n")

        for item in breakdown:
            f.write(f"{item['stock']:<10} {item['quantity']:<12.2f} ${item['price']:<11.2f} ${item['value']:<11.2f}\n")

        f.write("-" * 60 + "\n")
        f.write(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}\n")
        f.write("=" * 60 + "\n")

    print(f"✓ Portfolio saved to {filename}")


def save_to_csv(portfolio, total_value, breakdown):
    """Save portfolio to a CSV file."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])

        for item in breakdown:
            writer.writerow([item['stock'], f"{item['quantity']:.2f}",
                             f"${item['price']:.2f}", f"${item['value']:.2f}"])

        writer.writerow([])
        writer.writerow(["Total Investment Value", f"${total_value:,.2f}"])

    print(f"✓ Portfolio saved to {filename}")


def main():
    """Main function to run the stock portfolio tracker."""
    print("\n" + "=" * 60)
    print("WELCOME TO STOCK PORTFOLIO TRACKER")
    print("=" * 60)

    # Display available stocks
    display_available_stocks()

    # Get portfolio from user
    portfolio = get_portfolio()

    # Calculate total value
    total_value, breakdown = calculate_portfolio_value(portfolio)

    # Display summary
    display_portfolio_summary(portfolio, total_value, breakdown)

    # Ask user to save results
    while True:
        save_choice = input("Save portfolio to file? (yes/no): ").strip().lower()

        if save_choice in ['yes', 'y']:
            while True:
                format_choice = input("Choose format (txt/csv): ").strip().lower()

                if format_choice == 'txt':
                    save_to_txt(portfolio, total_value, breakdown)
                    break
                elif format_choice == 'csv':
                    save_to_csv(portfolio, total_value, breakdown)
                    break
                else:
                    print("Invalid choice! Please enter 'txt' or 'csv'.")
            break
        elif save_choice in ['no', 'n']:
            print("Portfolio not saved.")
            break
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()