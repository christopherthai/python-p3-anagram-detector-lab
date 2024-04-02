class Anagram:
    def __init__(self, word):
        self.word_letters = sorted(
            [letter.lower() for letter in word]
        )  # sort the letters of the word

    # match the word with a list of words
    def match(self, word_list):
        return [
            word for word in word_list if self.is_anagram(word)
        ]  # return a list of words that are anagrams of the word

    # check if the word is an anagram of the word
    def is_anagram(self, word):
        """
        Check if a given word is an anagram of the instance's word.

        Parameters:
        - word (str): The word to check for anagram.

        Returns:
        - bool: True if the given word is an anagram, False otherwise.
        """
        return self.word_letters == sorted(
            [letter.lower() for letter in word]
        ) and word.lower() != "".join(self.word_letters)
