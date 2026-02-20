import logging
from refrigerator import Refrigerator
from product import Product
from datetime import datetime


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('fridge.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    logging.info("== Запуск программы ==")

    try:
        logging.info("=== Настройка холодильника ===")

        while True:
            try:
                main_cap = int(input("Введите вместимость основной камеры: "))
                if main_cap <= 0:
                    print("Вместимость должна быть положительным числом.")
                    continue
                break
            except ValueError:
                logging.error("Ошибка: введите целое число.")

        while True:
            try:
                freezer_cap = int(
                    input("Введите вместимость морозильной камеры: "))
                if freezer_cap <= 0:
                    print("Вместимость должна быть положительным числом.")
                    continue
                break
            except ValueError:
                logging.error("Ошибка: введите целое число.")

        while True:
            owner_name = input("Введите имя владельца: ").strip()
            if not owner_name:
                print("Имя не может быть пустым.")
                continue
            break

        fridge = Refrigerator(main_cap, freezer_cap, owner_name)
        logging.info(f"\nХолодильник готов! Владелец: {owner_name}")
        print(
            "Перед работой с холодильником ознакомьтесь с командами (help) и авторизуйтесь.")

        while True:
            command = input("\n>").strip()
            if not command:
                continue
            parts = command.split()
            cmd = parts[0].lower()
            if cmd == 'exit':
                print("Вы уверены, что хотите выйти?(да/нет)")
                confirm = input("> ").strip().lower()

                if confirm == 'да':
                    logging.info("Пользователь подтвердил выход.")
                    print("До свидания!")
                    break
                elif confirm == 'нет':
                    logging.info("Пользователь отменил выход.")
                    print("Работа продолжается.")
                    continue
                else:
                    logging.warning(
                        f"Неверный ввод подтверждения: '{confirm}'")
                    print("Введен неверный ответ. Попробуйте ещё раз.")
                    continue
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
                logging.info(f"Вошёл: {fridge.get_current_user_info()}")
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
                    logging.error(f"Ошибка ввода: {e}")
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
                    logging.error(f"Ошибка ввода: {e}")
            else:
                logging.warning("Неизвестная команда! Используйте help.")

    except KeyboardInterrupt:
        logging.info("\nПрограмма завершена.")
    except Exception as e:
        logging.exception(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()
