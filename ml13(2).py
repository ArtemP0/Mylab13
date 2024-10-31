from film import FILM

if __name__ == "__main__":
    film1 = FILM("Гаррі Поттер", "Кріс Коламбу", "Warner Bros.", 200000000, 2021)
    film2 = FILM("Дюна", "Дені Вільнев", "Warner Bros.", 108000000, 2021)
    print("Початкові властивості фільмів:")
    film1.show()
    film2.show()
    film1.add_money(50000000)
    film2.add_money(20000000) 
    print("Оновлені властивості фільмів:")
    film1.show()
    film2.show()
