books = open("books.txt", "a+")

class library(): 
    def list_books(self):
        with open("books.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                book_name, author = line.strip().split(", ")
                print(f"Kitap: {book_name}, Yazar: {author}")

    def add_books(self):
        book_name = input("Eklemek istediğiniz kitabın adını yazınız: ")
        author_name = input("Kitabın yazarının adını yazınız: ")
        with open("books.txt", "a") as file:
            file.write(f"{book_name}, {author_name}\n")
   
    def remove_book(self) :
       delbook_name = input("Silmek istediğiiniz kitabın adını yazın:")
       with open ("books.txt", "r") as file:
             lines = file.readlines()
       with open("books.txt", "w") as file:
          for line in lines:
            if delbook_name not in line:
                file.write(line) 
          print(f"{delbook_name} isimli kitap başarıyla silindi.")
       
lib = library()

while True:
    print("*** MENÜ ***")
    print("1) Kitapların Listesi")
    print("2) Kitap Ekle")
    print("3) Kitap Çıkar")
    print("4) Çıkış")

    choice = input("Bir seçim yapınız (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_books()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Programdan çıkılıyor.")
        continue
    else:
        print("Geçersiz seçim. Lütfen 1 ve 4 arasında bir seçim yapınız.")
        continue  

my_library = library()
my_library.add_books()
my_library.list_books()

#mesela 5 yazınca geçersiz diyo ama eklemek istediğiniz kitabın adını yazın da diyo neden 2 ye döndüğünü anlamadım bir türlü
