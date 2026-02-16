def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("Connection established... vault wards aligned.\n")
            print("RECOVERED DATA:")
            content = f.read()
            print(content)
        print("\nData recovery complete. Storage unit disconnected with honor.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. The corridors are silent.")
    except Exception as exc:
        print(f"Unexpected error occured: {exc}")


if __name__ == "__main__":
    main()
