"""
Congressional Trade Disclosure Analysis Tool - CLI Prototype (Assignment 4)

This version:
- Uses an in-memory global list to store trade records.
- Provides a simple text menu with options to add, list, and exit.
- Keeps each trade as a single formatted string (to be refactored later).
"""

# Global data store: list of trade entries
TRADES = []  # each item is a string for now


def add_trade():
    """Prompt the user for trade details and add a new trade to TRADES."""
    print("\n--- Add New Trade ---")

    representative = input("Representative name: ").strip()
    trade_date = input("Trade date (YYYY-MM-DD): ").strip()
    disclosure_date = input("Disclosure date (YYYY-MM-DD): ").strip()
    ticker = input("Ticker symbol (e.g., AAPL, NVDA): ").strip()
    asset_type = input("Asset type (e.g., Stock, Option, ETF): ").strip()
    transaction_type = input("Transaction type (Purchase, Sale, Exchange): ").strip()
    amount_min = input("Amount minimum (e.g., 1000): ").strip()
    amount_max = input("Amount maximum (e.g., 5000): ").strip()
    source = input("Source (e.g., API name or URL): ").strip()

    # For Assignment 4, we store a simple formatted string.
    trade_entry = (
        f"Representative: {representative} | "
        f"Trade Date: {trade_date} | "
        f"Disclosure Date: {disclosure_date} | "
        f"Ticker: {ticker} | "
        f"Asset Type: {asset_type} | "
        f"Transaction Type: {transaction_type} | "
        f"Amount Range: {amount_min} - {amount_max} | "
        f"Source: {source}"
    )

    TRADES.append(trade_entry)
    print("\nTrade added successfully.\n")


def list_trades():
    """Display all trades stored in TRADES."""
    print("\n--- List of Trades ---")

    if not TRADES:
        print("No trades have been recorded yet.\n")
        return

    for index, trade in enumerate(TRADES, start=1):
        print(f"{index}. {trade}")

    print()  # blank line for spacing


def show_menu():
    """Print the main menu options."""
    print("=== Congressional Trade Disclosure Analysis Tool ===")
    print("1) Add new trade")
    print("2) List all trades")
    print("3) Exit")


def main():
    """Main application loop."""
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_trade()
        elif choice == "2":
            list_trades()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()