def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} from {', '.join(map(str, args))}")
        return func(*args)

    return wrapper
