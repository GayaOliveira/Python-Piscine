if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        file = open("new_discovery.txt", "w")
        print("Initializing new storage unit: new_discovery.txt\n"
              "Storage unit created successfully...\n\n"
              "Inscribing preservation data...")
        text = "[FRAGMENT 001] Digital preservation protocols "
        text += "established 2087\n"
        text += "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        text += "[FRAGMENT 003] Every byte saved is a victory "
        text += "against oblivion"
        file.write(text)
        print(text)
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception as e:
        print(f"Error: {e.args[1]}")
        print("Storage unit not created...")
    finally:
        file.close()
