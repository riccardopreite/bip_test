import unittest
import kadane as solution

class TestMaxSubArray(unittest.TestCase):
    def test_empty(self):
        # trivial case, empty array
        array = []
        max = "Empty array"
        self.assertEqual(solution.kadane_with_sub_array(array), max , "Should be: Empty array")

    def test_single(self):
        # trivial case, one element
        array = [1]
        sub_array = [1]
        max = 1
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_simple(self):
        # trivial case, all positive
        array = [1, 2, 3]
        sub_array = [1, 2, 3]
        max = 6
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_with_negative(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        sub_array = [4, -1, 2, 1]
        max = 6
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_with_all_negative_result(self):
        # trivial case, all negative: max of the array
        array = [-8, -3, -6, -2, -5, -4]
        sub_array = [-2]
        max = -2
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_with_first_sub_best_result(self):
        array = [1,2,-5,1,1]
        sub_array = [1,2]
        max = 3
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )
    
    def test_with_second_sub_best_result(self):
        array = [1,1,-5,2,1]
        sub_array = [2,1]
        max = 3
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )
    
    def test_with_medium_array_result(self):
        array = [4,6,-11,4,5,-7,3]
        sub_array = [4,6]
        max = 10
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )
    
    def test_with_big_array_result(self):
        array = [4,6,-11,4,5,-7,3,7,-5,9,-4,12]
        sub_array = [4,5,-7,3,7,-5,9,-4,12]
        max = 24
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_with_two_sub_array(self):
        # finds only the first maximum sub array.
        # in this case also [16] has same max of [4, 5, -7, 3, 7, -5, 9]
        array = [4,6,-11,4,5,-7,3,7,-5,9,-18,16]
        sub_array = [4, 5, -7, 3, 7, -5, 9]
        max = 16
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_with_first_element_max(self):
        array = [17,-18,6,-11,4,5,-7,3,7,-5,9]
        sub_array = [17]
        max = 17
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )

    def test_with_last_element_max(self):
        array = [4,6,-11,4,5,-7,3,7,-5,9,-18,17]
        sub_array = [17]
        max = 17
        message = "Should be ("+str(sub_array)+", "+str(max)+")"
        self.assertEqual(solution.kadane_with_sub_array(array), (sub_array,max), message )


if __name__ == '__main__':
    unittest.main()