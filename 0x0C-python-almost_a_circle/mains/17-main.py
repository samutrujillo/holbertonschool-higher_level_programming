#!/usr/bin/python3
""" 17-main """
__import__("sys").path.append("..")

if __name__ == "__main__":
    from models.rectangle import Rectangle

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
