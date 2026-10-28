# Simple registration form system using dictionaries.
# The user can add information, search for specific fields,
# and display all data stored in the record.

option = 0
record = {}  # Dictionary used to store registration data

# Main application loop
while option != 4:

    # Display menu options
    print("\nWELCOME TO THE REGISTRATION SYSTEM")
    print("1 - Add information")
    print("2 - Search information")
    print("3 - Display complete record")
    print("4 - Exit")

    option = int(input("Select an option: "))

    # Option 1 - Add new fields to the record
    if option == 1:

        # Receive field name and value from the user
        key = input("Enter the field name: ")
        value = input("Enter the value for this field: ")

        # Store data in the dictionary
        record[key] = value

    # Option 2 - Retrieve a specific field
    elif option == 2:

        # Display available fields
        print(f"Available fields: {list(record.keys())}")

        key = input("Enter the field you want to view: ")

        # Check if the field exists
        if key in record.keys():

            # Display the associated value
            print(f"The field '{key}' contains the value: {record.get(key)}")

        else:
            print("The specified field does not exist.")

    # Option 3 - Display the complete record
    elif option == 3:

        print("\nREGISTRATION RECORD")

        # Iterate through all dictionary entries
        for field, data in record.items():
            print(f"{field.upper()} --> {data}")

    # Option 4 - Exit application
    elif option == 4:

        print("Closing the registration system.")
        break

    # Handle invalid menu options
    else:

        print("Invalid option. Please try again.")