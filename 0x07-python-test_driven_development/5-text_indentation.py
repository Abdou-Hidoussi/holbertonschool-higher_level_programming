#!/usr/bin/python3
def text_indentation(text):
    new = ""

    if not isinstance(text, str):
        raise TypeError('text must be a string')
        return

    for x in text:
        new += x
        if x in [".", "?", ":"]:
                print(new.lstrip(), end='\n\n')
                new = ""
    if x in [".", "?", ":"]:
        print(new.lstrip(), end="")
    else:
        print(new.lstrip(), end="\n")
