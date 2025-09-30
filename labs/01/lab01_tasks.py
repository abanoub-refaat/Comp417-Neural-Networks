# write a method that takes a list and number and returns all the two numbers that equals to their sum
# ex: [1, 2, 3, 4, 5, 6], 7 --> 1,6 2,5  3,4

def target_sum(li:list, target):
    ans = []
    for i in range(len(li)):
        for j in range(i, len(li)):
            if(li[i] + li[j] == target):
                ans.append((li[i], li[j]))
    return ans

print(target_sum([1, 2, 3, 4, 5, 6], 7))
print(target_sum([10, 20, 30, 40, 50], 50))

# write a method that takes a list and returns each number and its freq
# [1, 1, 1, 2, 3 ,4 ,4]

def freq_elements(li:list):
    ans_map = {}
    for i in range(len(li)):
        if ans_map.get(li[i]):
            ans_map[li[i]] += 1
        else:
            ans_map[li[i]] = 1
    return ans_map

print(freq_elements([1, 1, 1, 2, 3, 4, 4]))
