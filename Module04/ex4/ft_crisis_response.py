if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open('lost_archive.txt', 'r') as file:
            print(file.readlines())
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open('classified_vault.txt', 'r') as file:
            print(file.readlines())
        print("STATUS: Normal operations resumed\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to 'standard_archive.txt'...")
        with open('standard_archive.txt', 'r') as file:
            text = file.readlines()[0]
            print("SUCCESS: Archive recovered - ", end="")
            print(f"''{text}''")
        print("STATUS: Normal operations resumed\n")
    except Exception as err:
        print(f"RESPONSE: {err.args[1]}")
        print("STATUS: Crisis handled, system stable\n")

    print("All crisis scenarios handled successfully. Archives secure.")
