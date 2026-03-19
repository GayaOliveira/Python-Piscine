import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    archivist_id = sys.stdin.readline().strip()
    print("Input Stream active. Enter status report: ", end="", flush=True)
    status_report = sys.stdin.readline().strip()

    print()
    msg1 = f"[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    alert = "[ALERT] System diagnostic: Communication channels verified\n"
    msg2 = "[STANDARD] Data transmission complete\n"
    sys.stdout.write(msg1)
    sys.stderr.write(alert)
    sys.stdout.write(msg2)

    print("\nThree-channel communication test successful.")
