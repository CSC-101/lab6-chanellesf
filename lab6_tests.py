from unittest import expectedFailure

import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    # Part 1
    def test_selection_sort_books(self):
        input = [data.Book(["Harper Lee"],"To Kill a Mockingbird"),
                 data.Book(["George Orwell"],"Animal Farm"),
                 data.Book(["J.D. Salinger"],"The Catcher in the Rye"),
                 data.Book(["Anthony Burgess"],"A Clockwork Orange")]
        lab6.selection_sort_books(input)
        expected = [data.Book(["Anthony Burgess"],"A Clockwork Orange"),
                    data.Book(["George Orwell"],"Animal Farm"),
                    data.Book(["J.D. Salinger"],"The Catcher in the Rye"),
                    data.Book(["Harper Lee"],"To Kill a Mockingbird")]
        self.assertEqual(expected,input)

    def test_selection_sort_books_2(self):
        input = [data.Book(["A"],"bbcbbc"),
                 data.Book(["B"],"bbabaaa"),
                 data.Book(["C"],"bbabbba")]
        lab6.selection_sort_books(input)
        expected = [data.Book(["B"],"bbabaaa"),
                    data.Book(["C"], "bbabbba"),
                    data.Book(["A"],"bbcbbc")]
        self.assertEqual(expected,input)

    def test_selection_sort_books_3(self):
        input = []
        lab6.selection_sort(input)
        expected = []
        self.assertEqual(expected,input)

    # Part 2
    def test_swap_case_1(self):
        text = "hEllo ! 012"
        actual = lab6.swap_case(text)
        expected = "HeLLO ! 012"
        self.assertEqual(expected,actual)

    def test_swap_case_2(self):
        text = "ALL UPPERCASE!!"
        actual = lab6.swap_case(text)
        expected = "all uppercase!!"
        self.assertEqual(expected,actual)

    def test_swap_case_3(self):
        text = ""
        actual = lab6.swap_case(text)
        expected = ""
        self.assertEqual(expected, actual)

    # Part 3
    def test_str_translate_1(self):
        text = 'abcdcba'
        actual = lab6.str_translate(text, 'a', 'x')
        expected = 'xbcdcbx'
        self.assertEqual(expected,actual)

    def test_str_translate_2(self):
        text = 'ripadoodledoo'
        actual = lab6.str_translate(text,'o','e')
        expected = 'ripadeedledee'
        self.assertEqual(expected,actual)

    # Part 4
    def test_histogram_1(self):
        input = "hello world i am a test string string world"
        actual = lab6.histogram(input)
        expected = {"hello":1, "world":2, "i":1,"am":1, "a":1,"test":1, "string":2}
        self.assertEqual(expected,actual)

    def test_histogram_2(self):
        input = "random words random words word help help"
        actual = lab6.histogram(input)
        expected = {"random":2, "words":2, "word":1, "help":2}
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()
