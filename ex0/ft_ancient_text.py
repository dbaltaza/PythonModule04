if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        f = open(filename, "r", encoding="utf-8")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        content = f.read()
        print(content)
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    except Exception as e:
        print(f"Unexpected error occured: {e}")