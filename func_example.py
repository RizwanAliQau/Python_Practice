def emoji_converter(message):
    words = message.split(" ")
    output = ""
    for word in words:
        output += word + " "
    return output


message = input(":>")
print(emoji_converter(message))

