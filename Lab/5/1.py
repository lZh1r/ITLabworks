class Book:
    title = "99 Франков"
    author = "Фредерик Бегбедер"
    year = 2000

    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

p = Book()

p.get_info()