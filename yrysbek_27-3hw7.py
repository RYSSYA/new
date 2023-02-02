ten = list(range(1, 11))

evens = list(filter(lambda x: x % 2 == 0, ten))

squared_evens = list(map(lambda x: x ** 2, evens))
print(squared_evens)

def get_list_item(lst=ten):
    while True:
        try:
            index = int(input("Введите индекс (или 'q' для выхода): "))
            if index == 'q':
                break
            print(lst[index])
        except ValueError:
            print("Пожалуйста, введите корректный индекс.")
        except IndexError:
            print("Пожалуйста, введите индекс между 0 и", len(lst) - 1)
 
            