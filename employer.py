class Employee:
    def __init__(self):
        print("Employee created:")

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("Making object...")
    obj=Employee()
    print("Function end...")
    return obj

print("Calling Create_obj function...")
obj=Create_obj()
print("Program end..")