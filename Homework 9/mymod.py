def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())

def count_chars(filename):
    with open(filename) as f:
        return len(f.read())

def test(filename):
    print(
        f"Number of lines in {filename}: {count_lines(filename)}"
    )

    print(
        f"Number of characters in {filename}: {count_chars(filename)}"
    )


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        test(sys.argv[1])
    else:
        print("Usage: mymod.py filename")

# dmytro@dmytro-LR:~/Desktop/Python/Beetroot/Homework/Homework 9$ python3
# Python 3.13.5 (main, Jun 22 2025, 08:28:01) [GCC 13.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from mymod import count_chars
# >>> count_chars('Lorem ipsum.txt')
# 1000
# >>> from mymod import count_lines
# >>> count_lines('Lorem ipsum.txt')
# 4
# >>> from mymod import test
# >>> test('Lorem ipsum.txt')
# Number of lines in Lorem ipsum.txt: 4
# Number of characters in Lorem ipsum.txt: 1000
# >>> exit()

# dmytro@dmytro-LR:~/Desktop/Python/Beetroot/Homework/Homework 9$ python3 mymod.py
# Usage: mymod.py filename
# dmytro@dmytro-LR:~/Desktop/Python/Beetroot/Homework/Homework 9$ python3 mymod.py mymod.py
# Number of lines in mymod.py: 36
# Number of characters in mymod.py: 1156