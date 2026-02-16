def print_header():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")


def access_vault(filename):
    try:
        f = open(filename, "r")
        print("Accessing Storage Vault:", filename)
        print("Connection established...\n")
        data = f.read()
        return data, f
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return None


def display_recovered_data(data):
    print("RECOVERED DATA:")
    print(data, end="")
    print()


def print_completion(file_handle):
    file_handle.close()
    print("\nData recovery complete. Storage unit disconnected.")


def main():
    print_header()
    result = access_vault("classified_data.txt")
    if result is None:
        return
    data, file_handle = result
    display_recovered_data(data)
    print_completion(file_handle)


if __name__ == "__main__":
    main()
