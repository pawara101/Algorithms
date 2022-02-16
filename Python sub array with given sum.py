def subarr(l1,target):
  k=0
  nums=list()
  while k<len(l1):
    sum10=0
    for i in range(k,len(l1)):
        
        sum10=sum10+l1[i]
        if sum10<target:
          nums.append(i)
        if sum10 == target:
          print("sum is target value")
          nums.append(i)
          print(nums)
          break
        if sum10>target:
          #print("sum is greater than 10,The sum is",sum10)
          nums.clear()
          break  
    for num in nums:
      final_sum = 0
      final_sum = final_sum+l1[num]
  

    k=k+1
  if final_sum!=target:
    print("No match")