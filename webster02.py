#!/usr/bin/python3

def main():
    hostipdict = {'host1': '10.0.2.3', 'host2': '10.0.3.3', 'host3': '10.3.4.10'}
    print(hostipdict)
    print(hostipdict['host1'])
    hostipdict['host4']= '10.4.5.6'
    print(hostipdict)
    print(hostipdict.keys())
    print(list(hostipdict.values()))


if __name__ == '__main__':
    main()
