#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1  # Default starting page

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self.current_page += 1