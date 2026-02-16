if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("\nInitializing new storage unit: new_discovery.txt")
    try:
        f = open("new_discovery.txt", "w")
        print("Storage unit created successfully")
        print("\nInscribing preservation data...")
        data = (
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n"
        )
        print(data)
        f.write(data)
        f.close()
    except Exception as e:
        print(f"Error: {e}")
    print("\nData inscription complete. Storage units sealed.")
    print("\nArchive 'new_discovery.txt' ready for long-term preservation.")