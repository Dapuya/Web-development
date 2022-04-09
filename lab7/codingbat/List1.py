def first_last6(nums):
  return True if nums[0] == 6 or nums[-1] == 6 else False


def same_first_last(nums):
  return True if len(nums) > 0 and nums[0] == nums[-1] else False


def make_pi():
  return [3, 1, 4]


def common_end(a, b):
  return True if a[0] == b[0] or a[-1] == b[-1] else False


def sum3(nums):
  return sum(nums)


def rotate_left3(nums):
  return nums[1:] + nums[0:1]


def reverse3(nums):
    return [nums[2], nums[1], nums[0]]


def max_end3(nums):
  if nums[0] > nums[-1]:
    nums[0:] = [nums[0]] * len(nums)
  else:
    nums[0:] = [nums[-1]] * len(nums)
  return nums



def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0


def middle_way(a, b):
   return [ a[1] , b[1] ]


def make_ends(nums):
  return [nums[0]] + [nums[-1]]


def has23(nums):
  return 2 in nums or 3 in nums
