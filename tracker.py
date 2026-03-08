def add_session():
    print("\n--- Add a new screen time session ---")
    
    # 1. App / site name (cannot be empty)
    name = input("Enter app/site name: ").strip()
    while not name:
        print("Error: Name cannot be empty!")
        name = input("Enter app/site name: ").strip()
    
    # 2. Minutes (must be positive whole number)
    while True:
        try:
            minutes = int(input("Enter minutes spent: ").strip())
            if minutes > 0:
                break
            print("Error: Please enter a number bigger than 0.")
        except ValueError:
            print("Error: That's not a valid number. Try again.")
    
    # 3. Category (ask — keep simple for now)
    category = input("Enter category (Social/School/Entertainment/Other): ").strip()
    
    # 4. Notes (optional)
    notes = input("Enter notes (press enter if none): ").strip()
    
    # Save to the shared lists
    app_names.append(name)
    minutes_list.append(minutes)
    categories.append(category)
    notes_list.append(notes)
    
    print("\nSession added successfully!")