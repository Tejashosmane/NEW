class Solution(object):
    def threeSum(self,nums):
        list1=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+1,len(nums)):
                    if(i!=j and i!=k and j!=k):
                        sum=nums[i]+nums[j]+nums[k]
                        if(sum==0):
                            list1.add([nums[i],nums[j],nums[k]])  
        print(list1)           

p=Solution()
list=[-10,0,20,10,-20]
p.threeSum(list)
