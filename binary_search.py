def find_min_rotations(rotated_list):
   first = 0
   last = len(rotated_list) -1
   print("starting...")
   while first < last:
      mid = (first + last) // 2
      if rotated_list[mid] < rotated_list[mid-1]:
         return mid
      elif rotated_list[mid] < rotated_list[last]:
         last = mid
      else: 
         first = mid
   return -1
   

tests = [
   [35,38, 70, 1, 4, 8, 16, 20, 21],
   [35,38, 70, 90, 91, 92, 95, 99, 102, 1, 4, 8, 16, 20, 21],
   [1, 4, 8, 16, 20, 21],
   [21],
   [],
]
answers= [3, 9, 0, -1, -1]

def test_rotations():
   test_results = []
   count = 0
   for test in tests:
      test_results.append(find_min_rotations(test))
      print("It was rotated", test_results[count], "times \n Expected answer is", answers[count], "\n")
      count +=1

test_rotations()