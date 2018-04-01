# draw a board X on X following user request

def draw(size):
    for block in range(1, size+1):
        print " ",
        print "-" * 3,
    print "\n"
    for pipe in range(1, size+2):
        print "|",
        print " " * 3,
    print "\n"

def lastline(size):
    for block in range(1, size+1):
        print " ",
        print "-" * 3,
    print "\n"

if __name__ == '__main__':
    BoardSize = input("Enter the board size you want to draw: ")
    for i in range(1, BoardSize+1):
        draw(BoardSize)
    lastline(BoardSize)
