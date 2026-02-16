def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "a+", encoding="utf-8") as f:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            f.seek(0)
            print(f.read())

            print("\nSECURE PRESERVATION:")
            new = "[classified] new security protocols archived"
            print(new)
            f.write(new)
    except Exception as exc:
        print(f"Error: {exc}")
    print("Vault automatically sealed upon completion.")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
