from refrigerator import Refrigerator
from product import Product
from datetime import datetime


def main():
    try:
        print("===Настройка холодильника===")
        main_cap = int(input("Введите вместимость основной камеры: "))
        freezer_cap = int(input("Введите вместимость морозильной камеры: "))
        owner_name = input("Введите имя владельца: ").strip()
        fridge = Refrigerator(main_cap, freezer_cap, owner_name)
        print(f"\nХолодильник готов! Владелец: {owner_name}")
        print(
            "Перед работой с холодильником ознакомьтесь с командами(help) и авторизуйтесь.")
        while True:
            command = input("\n>").strip()
            if not command:
                continue
            parts = command.split()
            cmd = parts[0].lower()
            if cmd == 'exit':
                print("До свидания!")
                break
            elif cmd == "help":
                print("""
Команды:
  login <имя>
  open <основная/морозилка>
  close <основная/морозилка>
  add <название> <цена> <срок> <год> <мес> <день> <зона>
  remove <название> <зона>
  get_expired <год> <мес> <день>(нынешние) <зона>
  status
  exit
            """)
            elif cmd == "login":
                if len(parts) != 2:
                    print("Используйте: login <имя>")
                    continue
                fridge.login(parts[1])
                print(f"Вошёл: {fridge.get_current_user_info()}")
            elif cmd == 'status':
                print(fridge)
            elif cmd == 'open':
                if len(parts) != 2:
                    print("Используйте: open <основная/морозилка>")
                    continue
                fridge.open_door(parts[1])
            elif cmd == 'close':
                if len(parts) != 2:
                    print("Используйте: close <основная/морозилка>")
                    continue
                fridge.close_door(parts[1])
            elif cmd == 'add':
                if len(parts) != 8:
                    print(
                        "Используйте: add <название> <цена> <срок> <год> <мес> <день> <зона>")
                    continue

                name = parts[1]
                try:
                    price = float(parts[2])
                    shelf_life = int(parts[3])
                    year = int(parts[4])
                    month = int(parts[5])
                    day = int(parts[6])
                    zone = parts[7]

                    production_date = datetime(year, month, day)
                    product = Product(name, price, shelf_life, production_date)
                    fridge.add(product, zone)
                except ValueError as e:
                    print(f"Ошибка ввода: {e}")
            elif cmd == 'remove':
                if len(parts) != 3:
                    print(
                        "Используйте: remove <название> <зона>")
                    continue
                fridge.remove(parts[1], parts[2])
            elif cmd == 'get_expired':
                if len(parts) != 5:
                    print(
                        "Используйте: get_expired <год> <мес> <день> <зона>")
                    continue

                try:
                    year = int(parts[1])
                    month = int(parts[2])
                    day = int(parts[3])
                    zone = parts[4]

                    today = datetime(year, month, day)
                    fridge.get_expired(today, zone)
                except ValueError as e:
                    print(f"Ошибка ввода: {e}")
            else:
                print("Неизвестная команда! Используйте help.")

    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()
