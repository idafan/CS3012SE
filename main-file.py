from binarytreefile import BinaryTree

def main():
    #creating a binary tree and adding some values
    Bintree = BinaryTree()
    numbers = [10, 8, 15, 2, 12, 9, 18]
    
    for number in numbers:
        Bintree.add(number)

    value1 = int(input("1st value: "))
    value2 = int(input("2nd value: "))
    print("LCA(" + str(value1) + "," + str(value2) + ") = " + str(Bintree.LCA(value1,value2)))



main()
