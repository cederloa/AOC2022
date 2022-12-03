
def main():
    with open("input.txt", 'r') as f:
        data = f.read().split("\n")
    
    points = 0
    for entry in data:
        if len(entry) > 0:
            if entry[2] == "X":
                points += 1
            if entry[2] == "Y":
                points += 2
            if entry[2] == "Z":
                points += 3
            points += addScore(entry)
    
    print(points)
    
    points2 = 0
    for entry in data:
        if len(entry) > 0:
            if entry[2] == "X":
                points2 += 0
            if entry[2] == "Y":
                points2 += 3
            if entry[2] == "Z":
                points2 += 6
            points2 += addScore2(entry)
            
    print(points2)
    
    
def addScore(entry):
    diff = ord("X") - ord("A")
    opponent = chr(ord(entry[0]) + diff)
    me = entry[2]
    
    if me == opponent:
        return 3
    if (me == "X" and opponent == "Y") or (me == "Y" and opponent == "Z") or (me == "Z" and opponent == "X"):
        return 0
    return 6

def addScore2(entry):
    diff = ord("X") - ord("A")
    opponent = chr(ord(entry[0]) + diff)
    me = entry[2]
    
    if (opponent == "X" and me == "Y") or (opponent == "Y" and me == "X") or (opponent == "Z" and me == "Z"):
        return 1
    if (opponent == "X" and me == "Z") or (opponent == "Y" and me == "Y") or (opponent == "Z" and me == "X"):
        return 2
    return 3

main()
