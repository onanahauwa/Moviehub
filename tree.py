class Trie:
  def __init__(self):
    self.letter_indices= {}
  def insert_word(self, word):
    letter_indices = self.letter_indices
    for letter in word:
      if letter not in letter_indices:
        letter_indices[letter] = {}
      letter_indices = letter_indices[letter]
    letter_indices["#"] = "END"

  def find_sub_elements(self, letter_indices):
    result = []
    for letter, child_letter_indices in letter_indices.items():
      if letter == '#':
        sub_result = [""]
      else:
        sub_result = [letter + child_letter for
                  child_letter in self.find_sub_elements(child_letter_indices)]
      result.extend(sub_result)
    return result

  def find_words(self, search_prefix = None):
    letter_indices = self.letter_indices
    if search_prefix:
      for letter in search_prefix:
        if letter in letter_indices:
          letter_indices = letter_indices[letter]
          continue
        return []
    return self.find_sub_elements(letter_indices)
