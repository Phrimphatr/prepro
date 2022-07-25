'''pre pro'''
def main() :
    money = int(input())
    water = int(input())
    snack_1 = int(input())
    snack_2 = int(input())
    snack_3 = int(input())
    ans1 = 0
    ans2 = 0
    ans3 = 0
    save = money-water
    if (save % 3) == 0:
        save = save (10*snack_1)
        ans1 += 15*snack_1
    if save < 0:
        print