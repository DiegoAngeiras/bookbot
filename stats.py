def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict:
    count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count

def sort_char_count(count: dict) -> list:
    sorted_list = []
    for char, cnt in sorted(count.items(), key=lambda item: item[1], reverse=True):
        sorted_list.append({"char": char, "num": cnt})
    return sorted_list