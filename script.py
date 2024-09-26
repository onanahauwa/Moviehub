from movies import genres, movies
from tree import Trie

def greet():
    print("   *       *       * ")
    print("  ***     ***     ***")
    print(" *****   *****   ***** ")
    print("***********************")
    print("***********************")
    print("***********************")
    print("***********************")
    print("________________________")
    print("*                       *")
    print("*                       *")
    print("* Welcome to Movie Hub! *")
    print("*                       *")
    print("*_______________________*")
    print("\n")


def input_one_genre_char():
  trie = Trie()
  for genre in genres:
    trie.insert_word(genre)
  print("\nWhat genres of movie do you like?")
  choice = input("Type the first letter of the genres you might be interested in.\n")
  result = [choice + genre for genre in trie.find_words(choice)]
  first_letter_result = [word[0] for word in result]
  if choice[0] in first_letter_result:
    return result
  else:
    print("Sorry, that's not a genre we have data on. Please make another choice.")
    return input_one_genre_char()

def input_two_genre_char():
  updated_genres = input_one_genre_char()
  trie2 = Trie()
  for genre in updated_genres:
    trie2.insert_word(genre)
  print("With that beginning letter your choices are {0}".format(updated_genres))
  print("\nWhich of the available genres would you like to choose?")
  choice = input("Type the first two letters of that genre and press enter.\n")
  result = [choice + genre for genre in trie2.find_words(choice)]
  first_two_letters_result = [word[:2] for word in result]
  if choice[:2] in first_two_letters_result:
    option = result.pop()
    return option
  else:
    print("Sorry, that's not a valid input.")
    return input_two_genre_char()

def get_movie_options():
  genre = input_two_genre_char()
  print("\nThe only option with those beginning letters is {0}.".format(genre))
  choice = input("Do you want to look at the {0} movies available? Enter 'y' for yes and 'n' for no: ".format(genre))
  if choice == 'y':
    for movie in movies:
      if movie[0] == genre:
        print("------------------------")
        print("\nTitle: {0}\nRating: {1} \nYear: {2}\n".format(movie[1], movie[2], movie[3]))
    again = input("Do you want to try another genre? Enter 'y' for yes and 'n' for no: ")
    if again == 'y':
      return get_movie_options()
    else:
      print("Thank You for using Movie Hub. Enjoy your movie!")
  else:
    print("Sorry to see you go, come back soon!")
        

def movie_hub():
  greet()
  get_movie_options()
  
movie_hub()