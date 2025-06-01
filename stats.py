def get_word_count(text):
    words = text.split()
    return len(words)
def text_stats(text):
    text_lower = text.lower()
    # Convert text to lowercase to ensure case-insensitivity
    words = text_lower.split()
    # Split the text into words
    stats = {"a" : 0, "b": 0, "c": 0 , "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0 ,
              "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0 , "!": 0, "\"": 0, "#": 0, "$": 0, "%": 0, "&": 0, "'": 0, "(": 0, ")": 0, "*": 0, "+": 0, ",": 0, "-": 0, ".": 0, "/": 0,
              ":": 0, ";": 0, "<": 0, "=": 0, ">": 0, "?": 0, "@": 0, "[": 0, "\\": 0, "]": 0, "^": 0, "_": 0, "`": 0, "{": 0, "|": 0, "}": 0, "~": 0 , " " : 0}
    for word in words:
        for char in word:
            if char in stats:
                stats[char] += 1
    return stats
def sort_stats(stats):
    # Sort the stats dictionary by value in descending order
    sorted_stats = sorted(stats.items(), key=lambda item: item[1], reverse=True)
    return sorted_stats