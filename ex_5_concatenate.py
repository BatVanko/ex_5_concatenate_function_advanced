def concatenate(*args, **kwargs):
    result_text = ''
    for t in args:
        result_text += t
    for key, value in kwargs.items():
        if key in result_text:
            result_text = result_text.replace(key,value)
    return result_text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
