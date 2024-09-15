def calculate_investment(principal, rate, fee, days):
    # Convert the rate to a decimal
    rate /= 100.0
    
    # Calculate the number of 30-day periods
    periods = days // 30

    # Calculate the final amount after each period
    for _ in range(periods):
        principal = principal + (principal * rate) - fee

    return principal

# Input values
initial_principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the return rate (in %): "))
platform_fee = float(input("Enter the platform fees: "))
investment_days = int(input("Enter the number of days: "))

# Calculate the final amount
final_amount = calculate_investment(initial_principal, annual_rate, platform_fee, investment_days)

print(f"The final amount after {investment_days} days is: {final_amount:.2f}")
