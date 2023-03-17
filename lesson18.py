def reversed_string(text):
    result = ""
    index = len(text) - 1
    while index >= 0:
        result += text[index]
        index -= 1
    return result

print(reversed_string("Hi everyone"))

# Цикл while используется для неоднократного исполнения определенной инструкции до тех пор,
# пока заданное условие остается истинным.