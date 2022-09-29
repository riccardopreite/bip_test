import sys
 
'''Return sub_array with maximum sum and the sum.'''
def kadane_with_sub_array(array):
    
    '''Trivial case: empty array'''
    if len(array) == 0:
        return "Empty array"

    '''Trivial case: one element array'''
    if len(array) == 1:
        return array, array[0]
    
    '''sub_list maximum'''
    max_so_far = -sys.maxsize
    max_ending_here = 0

    '''sub_list index'''
    start_index = 0
    end_index = 0

    '''start index of a better sub_list'''
    new_positive_start = 0
 
    for index, current_element in enumerate(array):
 
        max_ending_here = max_ending_here + current_element
 
        '''if max_ending_here < current element, start_index from current element.'''
        if max_ending_here < current_element:
            # print("update begin",index,max_ending_here,"<",current_element)
            max_ending_here = current_element
            new_positive_start = index
 
        ''' 
            update start_index to last maximum positive start;
            update end_index to current element that is the maximum ending.
        '''
        if max_so_far < max_ending_here:
            # print("update end_index",new_positive_start,index,max_so_far,"<",max_ending_here)
            max_so_far = max_ending_here
            start_index = new_positive_start
            end_index = index
            
 
    return array[start_index: end_index + 1], max_so_far
 
 
if __name__ == '__main__':
 
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane_with_sub_array(array))