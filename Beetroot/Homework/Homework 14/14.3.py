def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Тип не {type_.__name__}: отримано {type(arg).__name__}")
                return False
            if len(arg) > max_length:
                print(f"Перевищена довжина {max_length}: {len(arg)}")
                return False
            for item in contains:
                if item not in arg:
                    print(f"Не містить обов'язковий фрагмент: '{item}'")
                    return False
            return func(arg)

        return wrapper

    return decorator
