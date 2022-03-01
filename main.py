# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello")
print(1032)
print(2.34)
print("a:", 1)
a: 1
one = 1
two = 2
three = 3
print(one, two, three)
print("gemo" + "dialis")
print(10 - 2.5/2)
pupil = "Yulia"
old = 41
experience = 15
print("experience")
print("Второе задание")
def convert_to_preferred_format (sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print("seconds value in hours:",hour)
    print("seconds value in minutes:",min)
    return "%02d:%02d:%02d" % (hour,min,sec)

import time
n = 10000
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Time in preferred format:-", time_format)



























