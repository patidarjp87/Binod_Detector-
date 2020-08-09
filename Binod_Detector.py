import os
def isBinod(file):
    with open(file,"r") as f:
        filecontent=f.read()
    if "BINOD" in filecontent.upper():
        return True
    else:
        return False
if __name__=='__main__':
    dir_=os.listdir()
    for item in dir_:
        if item.endswith('txt'):
            if isBinod(item):
                print(f"Binod found in {item}")
            else:
                print(f"Binod not found in {item}")

    