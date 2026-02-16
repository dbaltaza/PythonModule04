def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("\nInitializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", "w", encoding="utf-8") as f:
            print("Storage unit created successfully. Seals are fresh.")
            print("\nInscribing preservation data...")
            data = (
                "[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee\n"
            )
            print(data)
            f.write(data)
    except Exception as exc:
        print(f"Error: {exc}")
    print("\nData inscription complete. Storage units sealed.")
    print("\nArchive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
