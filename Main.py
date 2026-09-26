
def calculate_profit():
    print("  Broiler Profit Calculator")
    print("-----------------------------------")
    
    try:
        num_chicks = int(input("Number of chicks bought: "))
        chick_price = float(input("Price per chick (R): "))
        feed_per_bird_kg = float(input("Feed per bird for 6 weeks (kg) - usually 4.5kg: "))
        feed_price_per_kg = float(input("Feed price per kg (R): "))
        mortality = int(input("Birds died: "))
        selling_price = float(input("Selling price per live bird (R): "))

        surviving = num_chicks - mortality
        if surviving < 0:
            print("Error: mortality can't be more than chicks")
            return

        total_chick_cost = num_chicks * chick_price
        total_feed_kg = surviving * feed_per_bird_kg
        total_feed_cost = total_feed_kg * feed_price_per_kg
        total_cost = total_chick_cost + total_feed_cost

        total_income = surviving * selling_price
        profit = total_income - total_cost
        profit_per_bird = profit / surviving if surviving > 0 else 0

        # Feed Conversion Ratio -
        fcr = feed_per_bird_kg / 2.0  # market weight 
        break_even_price = total_cost / surviving if surviving > 0 else 0

        print("\n--- RESULTS ---")
        print(f"Surviving birds: {surviving}")
        print(f"Total feed used: {total_feed_kg:.1f} kg")
        print(f"Total cost: R{total_cost:.2f}")
        print(f"Total income: R{total_income:.2f}")
        print(f"PROFIT: R{profit:.2f}")
        print(f"Profit per bird: R{profit_per_bird:.2f}")
        print(f"Break-even price: R{break_even_price:.2f}")
        print(f"Est. FCR: {fcr:.2f}")

        if profit > 0:
            print("Profitable batch!")
        else:
            print("Loss - check feed price or selling price")

    except ValueError:
        print("Please enter numbers only, e.g., 100 not 'one hundred'")

if __name__ == "__main__":
    calculate_profit()
