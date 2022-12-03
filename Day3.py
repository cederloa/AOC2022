from functions import readfile

priority = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
bags = readfile("Day 3/input.txt")


def part1():
    bagsHalved = list(map(lambda bag : [bag[slice(0, len(bag)//2)], bag[slice(len(bag)//2, len(bag))]], bags))
    result = 0
    for bag in bagsHalved[:-1]:
        l = set(bag[0]) & set(bag[1])
        result += priority.index(next(iter(l))) + 1
    return result


def part2():
    result = 0
    for i in range(0, len(bags)-1, 3):
        l = set(bags[i]) & set(bags[i+1]) & set(bags[i+2])
        result += priority.index(next(iter(l))) + 1
    return result


def main():
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")


if __name__ == "__main__":
    main()
