def test(grades = '56r, 74, 38, 87, 77'):
    try:
        grades = grades.split(',')
        new_grade = [int(grade) for grade in grades]
    except ValueError as ve:
        print('Inside Except Block')
        print(ve)
def main():
    print(test())

if __name__=="__main__":
    main()
