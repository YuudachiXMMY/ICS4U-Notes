def main():
    # List of the possible monetary values in the cases
    case_values = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
    
    while True:
        # Get the list of opened cases from the user input
        cases_input = input("Enter the case numbers separated by commas (or press enter to quit): ").strip()
        
        if not cases_input:
            break  # Exit the loop if the input is blank (user wants to quit)
        
        # Parse the input into a list of opened case numbers
        opened_cases = list(map(int, cases_input.split(',')))
        
        # Get the banker's offer
        banker_offer = float(input("Enter the banker's offer: ").strip())
        
        # Remove the opened cases' values from the case_values list
        remaining_values = [case_values[i-1] for i in range(1, 11) if i not in opened_cases]
        
        # Calculate the average of the remaining unopened cases
        average_remaining = sum(remaining_values) / len(remaining_values)
        
        # Output the average of remaining cases and the decision
        print("Average of remaining unopened cases: $",average_remaining)
        
        if banker_offer >= average_remaining:
            print("Take the deal!")
        else:
            print("Do not take the deal!")

main()