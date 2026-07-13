def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def character_count_map(text: str) -> dict:
    char_map = {}
    for char in text:
        char = char.lower()
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map

def sort_on(item: tuple[str, int]) -> int:
    return item[1]

def chars_dict_to_sorted_list(char_map: dict[str, int]) -> list[tuple[str, int]]:
    listOfTuples = list(char_map.items())
    sortedList = sorted(listOfTuples, key=sort_on, reverse=True)
    return sortedList

def print_report(path: str, word_count: int, sortedList: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sortedList:
        if(item[0].isalpha()):
            print(f"{item[0]}: {item[1]}")
    print("============= END ================")
