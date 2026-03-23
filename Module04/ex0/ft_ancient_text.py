if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("==> Accessing Storage Vault: ancient_fragment.txt")

    file = None
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        content = file.read()
        print("RECOVERED DATA:")
        print(content)
        print("\nData recovery complete.")
        file.close()
    except FileNotFoundError as err:
        print(f"Error: {err.args[1]}. Impossible to established connection.")
    except Exception as err:
        print(f"An unexpected error occurred: {err.args[1]}")
    finally:
        if file is not None:
            file.close()
        print("Storage unit disconnected.")

    print("\n==> Accessing Storage Vault: recent_fragment.txt")

    file = None
    try:
        file = open("recent_fragment.txt", "r")
        print("Connection established...\n")
        content = file.read()
        print("RECOVERED DATA:")
        print(content)
        print("\nData recovery complete.")
    except FileNotFoundError as err:
        print(f"Error: {err.args[1]}. Impossible to established connection.")
    except Exception as err:
        print(f"An unexpected error occurred: {err.args[1]}")
    finally:
        if file is not None:
            file.close()
        print("Storage unit disconnected.")
