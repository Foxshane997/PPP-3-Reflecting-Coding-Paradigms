# Prompt 1 -
print("----- Prompt 1 Start -----")
def flatten(arr):
    if not isinstance(arr, list):
        return [arr]
    return [item for sublist in arr for item in flatten(sublist)]

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_array(left) + middle + sort_array(right)

def flatten_and_sort(arr):
    return sort_array(flatten(arr))

nested_array = [3, [1, 2], [4, [5, 6]], 7]
result = flatten_and_sort(nested_array)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]

print("----- Prompt 1 End -----")
print("----- Prompt 2 Start -----")

# Prompt 2 -
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"
    
    def __str__(self):
        return f"Podracer(speed: {self:max_speed}, condition: {self.condition}, price: {self.price})"
    

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

    def __str__(self):
        return f"Anakin's Pod (speed: {self.max_speed}, condition: {self.condition}, price: ${self.price})"
    

class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        if isinstance(other_pod, Podracer):
            other_pod.condition = "trashed"

    def __str__(self):
        return f"Sebulba's Pod (speed: {self.max_speed}, condition: {self.condition}, price: ${self.price})"
    
class AnotherPod(Podracer):
    def flame_jet(self, other_pod):
        if isinstance(other_pod, Podracer):
            other_pod.condition = "trashed"

    def __str__(self):
        return f"Other's Pod (speed: {self.max_speed}, condition: {self.condition}, price: ${self.price})"


anakin_pod = AnakinsPod(max_speed=300, condition="Perfect", price=13000)
sebulba_pod = SebulbasPod(max_speed=250, condition="Perfect", price=10000)
another_pod = AnotherPod(max_speed=350, condition="Okay", price=15000)

print(anakin_pod) 
print(sebulba_pod) 
print(another_pod)

# Adding speed to Anakin's Podracer
anakin_pod.boost()
print(anakin_pod)

# Reducing conditin of Anakin's Podracer through Sebulba's
sebulba_pod.flame_jet(another_pod)
print(another_pod) 

# Repairing Anakin's Podracer
anakin_pod.repair()
print(anakin_pod);
print("----- Prompt 3 End -----")