from arithmetic_arranger import arithmetic_arranger

def main():
    print(arithmetic_arranger(["123 + 456", "789 - 1011", "1213 + 1415", "1617 + 1819"]))
    print("\n")
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))


if __name__ == "__main__":
    main()
