#!/usr/bin/python3

def main():
    mylist = []
    mylist.append('192.168.30.1')
    print(mylist)

    mylist.append('10.0.0.1')

    print(mylist)
    print(mylist[0])
    mylist2 = ['172.16.7.3', '10.0.1.1']
    mylist.extend(mylist2)
    print(mylist)

    print(mylist[-1])
    mylist3 = ['india']
    mylist4 = mylist + mylist2 + mylist3
    print (mylist4)

if __name__ == '__main__'
main()
