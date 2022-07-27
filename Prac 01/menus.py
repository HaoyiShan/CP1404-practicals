Name = input("Enter name:")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello",Name)
    elif choice == "G":
        print("Goodbye",Name)
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>>").upper()
print("Finished.")