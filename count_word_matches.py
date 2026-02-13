def count_word_matches(text, target):
    """
    Counts how many times a target word appears as a standalone word in the text.
    The match is case-insensitive, and words are separated by spaces.

    Args:
        text (str): Input text in which to search.
        target (str): The word to search for.

    Returns:
        int: Number of occurrences of the target word as a standalone word
    """
    if not text or not target:
        return 0

    words = text.lower().split()
    target = target.lower()

    return words.count(target)
