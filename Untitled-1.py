'''DROP DROP'''
def main():
    '''function'''
    grade = float(input())
    if 0 <= grade < 1:
        print("I'm so sad.")
    elif 1 <= grade < 2:
        print("%.2f"%(4-grade))
    else:
        print("I'm so happy.")
main()
