if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in file:
                print(line.strip())
    except Exception as e:
        print("Vault connection could not be established")
        print(f"Error (read attempt): {e.args}")
    try:
        with open("security_protocols.txt", "w") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
    except Exception as e:
        print("Vault connection could not be established")
        print(f"Error (write attempt): {e.args}")
    finally:
        print("\nAll vault operations completed with maximum security.")

    # print(file.closed)
