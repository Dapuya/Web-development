def count_evens(nums):
  cnt = 0
  for i in nums:
    if i % 2 == 0:
      cnt += 1
  return cnt


def big_diff(nums):
  return max(nums) - min(nums)


def centered_average(nums):
  return (sum(nums) - max(nums) - min(nums)) // (len(nums)-2)


def sum13(nums):
  if len(nums) == 0: return 0
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 13 or (i > 0 and nums[i-1] == 13): continue
    sum+=nums[i]
  return sum


def sum67(nums):
  if len(nums) == 0: return 0
  isOk = True
  sum = 0
  for i in nums:
    if i == 6: isOk = False
    elif isOk == False and i == 7: isOk = True
    elif isOk: sum += i
  return sum


def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False