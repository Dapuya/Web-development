def string_times(str, n):
  	res = ''
  	for i in range(n): res += str
  	return res


def front_times(str, n):
  	res = ''
  	for i in range(n): res += str[:3]
  	return res


def string_bits(str):
  	res = ''
  	for i in range(len(str)):
            if i % 2 == 0:res += str[i]

  	return res


def string_splosion(str):
  	res = ''
  	for i in range(len(str)):
  	    res += str[:i + 1]
  	return res


def last2(str):
  	if len(str) < 2:
  	  return 0
  	t = str[-2:]
  	cnt = 0
  	for i in range(len(str) - 2):
  	  if str[i:i + 2] == t:
  	    cnt += 1
  	return cnt


def array_count9(nums):
  	cnt = 0
  	for i in nums:
  	  if i == 9:
  	    cnt += 1
  	return cnt


def array_front9(nums):
  	for i in range(min(4, len(nums))):
  	  if nums[i] == 9:
  	    return True
  	return False


def array123(nums):
  for i in range(1, len(nums) - 1):
    if nums[i] == 2 and nums[i - 1] == 1 and nums[i + 1] == 3:
      return True
  return False


def string_match(a, b):
  cnt = 0
  l = min(len(a), len(b))
  for i in range(l - 1):
	  if a[i:i + 2] == b[i:i + 2]:
	    cnt += 1
  return cnt