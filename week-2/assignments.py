# start

# assignment 1

def calculate(min, max):
    sum = 0
    for i in range(min,max+1):
        sum += i
    return(sum)


# 呼叫 calculate 函式

calculate(1, 3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


# assignment 2

def avg(data):
  sum = 0
  for i in range(data["count"]):
    sum += data["employees"][i]["salary"]
  return sum / data["count"]


# 呼叫 avg 函式

avg({
"count":3,
"employees":[
{"name":"John","salary":30000},
{"name":"Bob","salary":60000},
{"name":"Jenny","salary":50000}
]
})  


# assignment 3

def maxProduct(nums):
  result = nums[0] * nums [1]
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if  nums[i] * nums[j] > result:
        result = nums[i] * nums[j]
  return result

# 呼叫 maxProduct 函式
    
maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([-1, -2, 0]) # 得到 2


# assignment 4

def twoSum(nums, target):
  sum = target
  element = []
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i] + nums [j] == sum:
        element.extend([i,j])
        break
  return element
  
# 呼叫 twoSum 函式

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


# assignment 5

def maxZeros(nums):
  count = 0
  max = 0 
  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
      if count > max :
        max = count
    else:
        count = 0
  return max


# 呼叫 maxZeros 函式

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3
