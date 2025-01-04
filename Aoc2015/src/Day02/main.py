def main():
    part_1()
    part_2()

def part_1():
    lines = get_input("input.txt")
    total_sq_feet=0
    for line in lines:
        (l, w, h)  = line.split('x')
        L = int(l)
        W = int(w)
        H = int(h)
        side1 = 2*L*W
        side2 = 2*W*H
        side3 = 2*H*L
        minSide = min(side1, side2, side3)
        minSide = minSide/2
        total_sq_feet = total_sq_feet + minSide +side1 + side2 + side3
    print(total_sq_feet)

def part_2():
    lines = get_input("input.txt")
    total_lin_feet=0
    for line in lines:
        (l, w, h) = line.split('x')
        L = int(l)
        W = int(w)
        H = int(h)
        p1 = 2*(H+W)
        p2 = 2*(H+L)
        p3 = 2*(W+L)
        p = min(p1, p2, p3)
        ribbon = L*W*H
        total_lin_feet = total_lin_feet + ribbon + p
    print(total_lin_feet)



def get_input(file_path:str) -> list():
    lines=()
    with open(file_path, 'r') as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()