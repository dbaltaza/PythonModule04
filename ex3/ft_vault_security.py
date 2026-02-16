if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    with open("classified_data.txt", "a+") as f:
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        f.seek(0)
        print(f.read())

        print("\nSECURE PRESERVATION:")
        new = "[classified] new security protocols archived"
        print(new)
        f.write(new)
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")
