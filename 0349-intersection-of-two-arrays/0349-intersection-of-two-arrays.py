class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #isme hame intersection lena hai aur rsult mein duplicates nahi rehne chaiye 
        #duplicates nahi rehne ka matlb hai ki -> set ka use hona 
        set1=set(nums1)
        set2=set(nums2)
        return list(set1 & set2)