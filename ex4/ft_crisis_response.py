def crisis_handler(filename: str) -> None:
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")

    try:
        with open(filename, "r") as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable. Lights steady.")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained. Seals intact.")
    except Exception:
        print("RESPONSE: System anomaly detected")
        print("STATUS: Crisis handled, system stable. Anomaly logged.")
    else:
        print(f"SUCCESS: Archive recovered - '{data}'")
        print("STATUS: Normal operations resumed. Archives breathe easy.")
    print()


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files = (
        "lost_archive.txt",
        "classified_data.txt",
        "corrupted_archive.txt",
        "standard_archive.txt",
    )
    for filename in files:
        crisis_handler(filename)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
