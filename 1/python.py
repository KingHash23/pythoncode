#Write a program that can search an element in an array and returns the result if the elements are not found ,it should return element not in the list .your code should have loops arrays and functions combined .


def search_element(arr, target):
    for element in arr:
        if element == target:
            return f"Element {target} found in the list."
    return f"Element {target} not found in the list."

# Example usage:
array = [1, 3, 5, 7, 9]
element_to_search = 5
print(search_element(array, element_to_search))

element_to_search = 6
print(search_element(array, element_to_search))
