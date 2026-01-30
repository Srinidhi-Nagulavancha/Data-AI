try:
    print("step1")
    a=int(input("Enter numerator: "))
    b=int(input("Enter denominator: "))
    result = a/b
    print("step2")      
    print("Result is:", result)
except Exception as e:
    print("Error:", e)
finally:
    print("Execution completed.")

