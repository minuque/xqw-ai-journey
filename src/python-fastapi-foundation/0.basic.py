def main():
    person = {"name": "xqw", "age": 18}
    arr = [1, 3, 5, 6]

    # print(f"{ person.get('name').upper() }")
    # print(f"arr length ={len(arr)}")

    # 9 * 9乘法口诀表
    for x in range(10):
        for y in range(x + 1):
            print(f"{ x }* { y } = { x * y}", end="\t")
        print()


if __name__ == "__main__":
    main()
