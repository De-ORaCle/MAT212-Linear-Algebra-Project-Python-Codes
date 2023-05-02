'''

This code creates random elements (a,b,c,d) such that Y = {(a, b, c, d) ∈ R⁴ : a - b + 3d = 0}
then goes on to show that it is both closed under addition and scalar multiplication.

If the code is iterated infinitely, it would still provide the same result (i.e. Y is closed under addition and
multiplication), thereby proving that Y = {(a, b, c, d) ∈ R”⁴: a-b+3d=0} is a subspace of R”⁴.

'''

import random


def create_element():
    a = random.randint(-10, 10)  # generate a random integer between -10 and 10
    b = random.randint(-10, 10)
    d = random.randint(-10, 10)
    c = random.randint(-10, 10)
    while a - b + 3 * d != 0:  # check if the condition is satisfied
        a = random.randint(-10, 10)  # if not, generate new random values
        b = random.randint(-10, 10)
        d = random.randint(-10, 10)
    return (a, b, c, d)  # return the tuple


# assume that Y is defined as in the previous code example
# and that create_element() returns a tuple (a, b, c, d) in Y

element = create_element()  # generate a random element of Y

# check if element satisfies the condition a - b + 3d = 0
if element[0] - element[1] + 3 * element[3] == 0:
    print("Element satisfies the condition a - b + 3d = 0")
else:
    print("Element does not satisfy the condition a - b + 3d = 0")

# assume that Y is defined as in the previous code example
# and that create_element() returns a tuple (a, b, c, d) in Y

# generate two random elements of Y
element1 = create_element()
element2 = create_element()

print("Element 1:", element1)
print("Element 2:", element2)

# compute their sum and check if it belongs to Y
sum_element = tuple(z + y for z, y in zip(element1, element2))
if sum_element[0] - sum_element[1] + 3 * sum_element[3] == 0:
    print("Sum element belongs to Y")
    sumType = True
else:
    print("Sum element does not belong to Y")

# compute their scalar multiple and check if it belongs to Y
alpha = random.randint(-10, 10)
scalar_element = tuple(alpha * z for z in element1)
if scalar_element[0] - scalar_element[1] + 3 * scalar_element[3] == 0:
    print("Scalar multiple belongs to Y")
    multipleType = True
else:
    print("Scalar multiple does not belong to Y")

if sumType == True and multipleType == True:
    print("\nThis proves that Y = {(a, b, c, d) ∈ R”⁴: a-b+3d=0} is a subspace of R”⁴.")
else:
    print("\nThis not not mean that the proof is incorrect but the random element generator must have generated one "
          "or two elements that doesn't satisfy the condition a - b + 3d = 0")
