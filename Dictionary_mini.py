Dictionary_1={}
while True:
    print("\nDictionary Mangement System")
    print("1. Add a word")
    print("2. Search for meaning")
    print("3. Display all the words")
    print("4. Update Meaning")
    print("5. Delete word")
    print("6. Exit")

    choice=input("Enter your choice : ")
                     
    if choice == "1": 
         word =input("Enter the word :").lower()
         meaning= input("Enter the meaning :")
         Dictionary_1[word] = meaning
         print("word added successfully")

    elif choice == "2":
         word=input("Enter the word to search: ").lower()
         if word in Dictionary_1:
            print("meaning :", Dictionary_1[word])
         else:
            print("word not found in dictionary.")
    elif choice == "3":
        if word in Dictionary_1:
            print(Dictionary_1)
        else:
            print(f"Dictionary is empty")

    elif choice == "4":
        word = input("enter a word :").lower()
        if word in Dictionary_1:
            meaning = input("Enter new meaning of word : ")
            Dictionary_1[word]=meaning
            print(f"word updated and new meaning of word {word}: {meaning}")
        else:
            print("Enter word not found in dictionary")
    elif choice == "5":
        word =input("Enter a word : ").lower()
        if word in Dictionary_1:
            del Dictionary_1[word]
            print(f"entered word : {word} deleted succesfully")
        else:
            print(f"{word} is word not found in Dictionary_1")
    elif choice == "6":
        print("Exiting the dictionary management system")
        break
    else:
        print("Invalid choice,please try again")

