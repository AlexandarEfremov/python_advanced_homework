def tags(letter):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return f"<{letter}>{function(*args)}</{letter}>"
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()

print(to_upper('hello'))