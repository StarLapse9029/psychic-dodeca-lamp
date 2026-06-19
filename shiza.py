import sys

def main():
    if len(sys.argv) > 2:
        print("Too many arguments!!!")
        return

    orig = sys.argv[1]
    for i in range(26):
        print(f"{i}: {rotate(orig, i)}")

# A = 65 Z = 90
# a = 97 z = 122
def rotate(string, amount):
    new_str = ""
    for character in string:
        i = ord(character)
        if i > 64 and i < 91:
            i += amount
            if i > 90:
                i -= 26
        elif i > 96 and i < 123:
            i += amount
            if i > 122:
                i -= 26
        else:
            i = i
        new_str += chr(i)
    return new_str

main()
