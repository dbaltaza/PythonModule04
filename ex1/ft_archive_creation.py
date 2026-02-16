def print_header():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")


def create_archive(filename):
    try:
        f = open(filename, "x")
        print("Initializing storage unit:", filename)
        print("Status: storage unit created.\n")
        return f
    except FileExistsError:
        print("ERROR: Storage unit already exists. Choose a new filename.")
        return None


def write_archive(f):
    print("Beginning data inscription...")
    print("[ENTRY 001] New quantum algorithm discovered")
    f.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 002] Efficiency increased by 347%")
    f.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 003] Archived by Data Archivist trainee")
    f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    f.close()


def main():
    print_header()
    f = create_archive("new_discovery.txt")
    if f is None:
        return
    write_archive(f)
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
