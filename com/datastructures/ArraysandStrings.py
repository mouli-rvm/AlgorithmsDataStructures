def isUnique(str):

    if len(str) > 128:
        return "Not Unique"
    char_array = list(str)
    seen_characters = set()

    for char in str:
        if char.lower() in seen_characters:
            return "Not Unique"
        seen_characters.add(char.lower())
    return "Unique"

print(isUnique("Srinth"))