#experimentally verifying the amortized O(1) runtime of append() on lists (dynamic array)
import time

def get_append_time(N):
    '''returns average time spent on .append() on a list as it grows to a final length N'''
    temp = []
    start = time.perf_counter()
    for _ in range(N):
        temp.append(None) #may cause dynamic resizing of underlying reference array
    end = time.perf_counter()
    return (end-start)/N #avg time per append

def avg_return_val(func, N, tests=40):
    '''returns average return value of func (with arg N passed to it) over 40 experiments'''
    sum = 0
    for _ in range(tests):
        sum = sum + func(N)
    return sum/tests


print('N=2:', avg_return_val(get_append_time, 2)) #is larger number bc range() creation step skews the time average
print('N=100:', avg_return_val(get_append_time, 100))
print('N=1000:', avg_return_val(get_append_time, 1000))
print('N=10000:', avg_return_val(get_append_time, 10000))
print('N=100000:', avg_return_val(get_append_time, 100000))
print('N=1000000:', avg_return_val(get_append_time, 1000000))

'''Conclusion: average runtime of each append() is independent of length of final list
-- in accordance with amortized O(1) runtime for each append'''