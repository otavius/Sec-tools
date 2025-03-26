# import threading
# import time 

# def print_number():
#     for i in range(1, 6):
#         print(f"number: {i}")
#         time.sleep(1)

# def print_letters():
#     for letter in "ABCDE":
#         print(f"Letter: {letter}")
#         time.sleep(1)

# thread1 = threading.Thread(target=print_number)
# thread2 = threading.Thread(target=print_letters)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Both threads have finished execution.")

with open("data.txt", "w") as file:
    file.write("hello there!\n")
    file.write("I am moose")

with open("data.txt", "r") as file:
    data = file.read()
    print(data)