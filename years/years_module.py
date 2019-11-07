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
    in2 = int(in2)
    print(years(in2))
    return


if __name__ == '__main__':
    main()
