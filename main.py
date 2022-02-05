import Kitchen
import sys
import os, os.path

# from dadata import Dadata
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # token = "19b7a6cd682bdabb9a35c22f266b8464fcec7398"
    # dadata = Dadata(token)
    # result = dadata.find_by_id("party", "1644042259")

    # print(result)
    # result = result[0]
    # result2 = result['data']
    # for i in result2.keys():
    #   print(" %20s | %s " % (i, result2[i]))
    #  # print(len(result))
    # print(str(type({})))
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    # res = ()
    # print(isinstance(res, dict))


    #print(dir(Foods))
    #print("%s +++" %sys.argv)

    #r = Kitchen.Recipe()
    #print(r.rs)
    print(os.getcwd())
    print(os.path.split(os.getcwd()))
    print(os.stat("."))
