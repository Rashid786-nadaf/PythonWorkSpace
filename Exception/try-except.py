try:
    num = int(input("Enter an number: "))
    print("This will work")
    print(10 /num)
    print("Phase 1 Completed")
except ZeroDivisionError:
    print("Value entered cannot be Zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed") 