def stop_words(words):
    def wrapper():
        text = create_slogan("Stepan")
        for word in words:
            text = text.replace(word, "*")
        return text

    return wrapper


def create_slogan(name):
    return f"{name} п'є пепсі у своєму новому BMW"


create_slogan = stop_words(["пепсі", "BMW"])
# print(create_slogan())
