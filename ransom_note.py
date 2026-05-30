def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    magazine_counts = {}

    # Build a frequency map of every available character in the magazine.
    for character in magazine:
        magazine_counts[character] = magazine_counts.get(character, 0) + 1

    # Spend one stored character at a time while checking the ransom note.
    for character in ransomNote:
        if magazine_counts.get(character, 0) == 0:
            return False

        magazine_counts[character] -= 1

    return True
