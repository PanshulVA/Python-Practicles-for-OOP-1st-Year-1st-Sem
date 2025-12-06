try:
    name=input("Enter your name here:")
    for char in name:
        if not char.isalpha or char.isspace:
            raise ValueError("Names usually don't carry numbers or special characters, please make sure you type it correctly!")
        print(f"Hello! {name} your name is valid congratulations")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")        
        