def countCharacter(string):
    character_count = {}
    for c in string:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count


print(countCharacter("hello world"))
print(countCharacter("hello world hello world"))
print(countCharacter("hello world hello world hello world"))
print(countCharacter("hello world hello world hello world hello world"))
print(countCharacter("lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"))