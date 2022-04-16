n = int(input())
positives = []
negatives = []
for num in range(n):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)
print(f"positives: {positives} <=> negatives: {negatives}.")
print(len(positives))
print(len(negatives))
