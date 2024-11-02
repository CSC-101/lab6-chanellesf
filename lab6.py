import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_alphabetically(values:list[data.Book], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title.replace(" ","").lower() < values[mindex].title.replace(" ","").lower():
            mindex = idx
    return mindex

# Takes a list of Book objects and sorts them in alphabetical order by title
# INPUT: list of Book objects to be sorted
# OUTPUT: no returns, just modifies list to be sorted
def selection_sort_books(books : list[data.Book]):
    for idx in range(len(books) - 1):
        mindex = index_smallest_alphabetically(books, idx)
        tmp = books[mindex]
        books[mindex] = books[idx]
        books[idx] = tmp

# Part 2
# Swaps uppercase chars to lowercase and vice versa
# INPUT: string whose characters will be swapped cases
# OUTPUT: string with characters swapped
def swap_case(text : str) -> str:
    new_text = []
    for i in range(len(text)):
        if text[i].islower():
            new_text.append(text[i].upper())
        elif text[i].isupper():
            new_text.append(text[i].lower())
        else: new_text.append(text[i])
    return "".join(new_text)

# Part 3
def str_translate(text : str, old : str, new : str) -> str:
    translated_text =[]
    for i in range(len(text)):
        char = text[i]
        if char == old:
            char = new
        translated_text.append(char)
    return "".join(translated_text)

# Part 4
# Returns a dictionary mapping the word to the count it appears in the string
# INPUT: string
# OUTPUT: dictionary
def histogram(text : str) -> dict:
    dict = {}
    words = text.split(" ")
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


