##########################################
#     Reflecting on Coding Paradigms     #
##########################################


# Functional Prompt
def flatten_and_sort(arrays):
    flattened = [item for sublist in arrays for item in sublist]
    sorted_result = sorted(flattened)
    return sorted_result

nested_arrays = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
result = flatten_and_sort(nested_arrays)
print(result)
array2 = [[5, 4, 9, 6], [7, 12], [91, 57, 31, 41, 65], [10, 19]]
result2 = flatten_and_sort(array2)
print(result2)


# Object Oriented Prompt
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self):
        self.condition = "thrashed"



pod1 = Podracer(3, "thrashed", 1000)
pod2 = AnakinsPod(2, "perfect", 1500)
pod3 = SebulbasPod(4, "repaired", 1200)


pod1.repair()
print(pod1.condition)

pod2.boost()
print(pod2.max_speed)

pod3.flame_jet()
print(pod3.condition)