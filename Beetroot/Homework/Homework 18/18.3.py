class TypeDecorators:
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                raise ValueError(f"Can`t convert '{result}' to int")

        return wrapper

    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                lowered = result.strip().lower()
                if lowered in ['true', '1']:
                    return True
                elif lowered in ['false', '0']:
                    return False

            else:
                raise ValueError(f"Innocent bool value '{result}'")

    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                raise ValueError(f"Can`t convert '{result}' to float")

        return wrapper
