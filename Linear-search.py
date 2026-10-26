arr = [12,34,32,56,43,78]
search = int(input("Enter the element to search : "))
found = False
for i in range (len(arr)):
    if arr[i] == search:
        print("Element found at index:" , i)
        found = True
        break
if not found:
    print("Element is not found in array")    
    