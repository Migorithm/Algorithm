#https://leetcode.com/problems/two-sum/

#we have two chances of getting the solution example arr=[1,2,3,5] and target=6
		#we have two chances of getting sum 6
		# 1)3+5 and 2)5+3 in this code we utilize the second chance by creating dictionary
		# of previous list element having key as the element and index as values.

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		val={}
		lst=[]
		for i in range (len(nums)):
			diff=target-nums[i]
            # 5
            # 4
            # 3
            # 1
#This is a point where difference of target - num[3] becomes 1, and 1 is stored as key in dictionary
#with value signifying its index

			if diff in val:
				lst.append(i)
				lst.append(val[diff])
				return lst
			val[nums[i]]=i
            # val[1] = 0
            # val[2] = 1
            # val[3] = 2
            # val[5] = 3
