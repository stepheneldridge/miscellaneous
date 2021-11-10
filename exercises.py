# returns number of integers in <collection> above or below <threshold>
# values equal to <threshold> are not counted
def aboveBelow(collection, threshold):
    result = {"above": 0, "below": 0}
    for i in collection:
        if i > threshold:
            result["above"] += 1
        elif i < threshold:
            result["below"] += 1
    return result

# returns <string> rotated to the right by <rotate> characters with overflow appended to the beginning
def stringRotation(string, rotate):
    assert len(string) > 0
    rotate = rotate % len(string)
    return string[-rotate:] + string[:-rotate] 

if __name__ == "__main__":
    print("Examples")
    collection = [1, 2, 3, 4, 5, 6]
    threshold = 3
    print("aboveBelow:", collection, threshold)
    print("output:", aboveBelow(collection, threshold))
    string = "MyString"
    rotate = 2
    print("\nstringRotation:", string, rotate)
    print("output:", stringRotation(string, rotate))