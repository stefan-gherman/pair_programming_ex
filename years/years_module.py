import datetime


def years(age):
    year = datetime.date.today().year
    if age < 100:
        years_left = 100 - age
        return years_left + year
    else:
        return year    
    return


def main():
    in1 = input("Name:")
    in2 = input("Age:")
    in3 = input("Copies:")
    in2 = int(in2)
    in3 = int(in3)
    print(years(in2))
    for i in range(in3):
        #print(years(in2))
        print(years(in2), end = ' ')
    return


if __name__ == '__main__':
    main()
