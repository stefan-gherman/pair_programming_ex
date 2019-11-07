import string
import random as rd

def passwordgen():
   all_possible_chars = list(string.printable[:-6]) 

   len_passw = 0
   passw = ""

   while len_passw <= 20:
       passw += all_possible_chars[rd.randint(0,len(all_possible_chars)-1)]
       len_passw += 1
   return passw   


def main():
    in1 = input("Password Strenght w for weak, s for strong:")
    if in1 == 'w':
        weak_passwd = ['passwd', 'user', 'admin' , 'root']
        print(weak_passwd[rd.randint(0,len(weak_passwd)-1)])
    elif in1 == 's':
        print(passwordgen())
    return


if __name__ == '__main__':
    main()
