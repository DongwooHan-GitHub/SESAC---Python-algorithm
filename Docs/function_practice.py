import random 

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

def my_max(lst, cmp = lambda x, y: x):
    pass 

def my_min(lst, cmp = lambda x, y: x):
    pass 

lst = [(1,2), (2,3), (5,3), (19, 2), (6, 100)]

def max_by_first_element(lst):
    max_elem = lst[0]

    for e in lst[1:]:
        if e[0] > max_elem[0] :
            max_elem = e 
    
    return max_elem

def max_by_sum(lst):
    max_elem = lst[0]

    for e in lst[1:]:
        if sum(e) > sum(max_elem):
            max_elem = e 
    
    return max_elem 

def my_max(lst, cmp = lambda x,y:x):
    max_elem = lst[0]

    for e in lst[1:]:
        max_elem = cmp(e, max_elem)
    
    return max_elem 

def compare_by_sum(x, y):
    if sum(x) > sum(y): return x
    else: return y 

def compare_by_first_element(x, y):
    if x[0] > y[0]: return x 
    else: return y 

print(my_max(lst, cmp = compare_by_sum))
print(my_max(lst, cmp = compare_by_first_element))

def my_min(lst, cmp = lambda x, y:x, tie_breaker = lambda x,y:x):
    min_elem = lst[0]

    for e in lst[1:]:
        case = cmp(e, min_elem)
        if case == min_elem:
            min_elem = e
        elif case == e:
            pass 
        else:
            tie_case = tie_breaker(e, min_elem)
            if tie_case == min_elem:
                min_elem = e 

    return min_elem






# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기 
# --------------------------------------------

    # 함수 만들기
def sort1(lst, cmp, upper_to_lower=False):
    # 리스트 만들기
    res = lst[:]
    n = len(res)

    for i in range(n):
        for j in range(n - i - 1):
            # 내림차순 정렬
            if upper_to_lower:
                if cmp(res[j], res[j + 1]) == res[j]:
                    res[j], res[j + 1] = res[j + 1], res[j]
            # 오름차순 정렬
            else:
                if cmp(res[j], res[j + 1]) == res[j + 1]:
                    res[j], res[j + 1] = res[j + 1], res[j]

    return res

def my_compare(x, y):
    if x[0] > y[0]:
        return x
    elif y[0] > x[0]:
        return y
    else:
        return "equal"
    

lst = [(1, 2), (2, 3), (5, 3), (19, 2), (6, 100)]
desc = sort1(lst, my_compare)
print(desc)
asc = sort1(lst, my_compare, upper_to_lower=True)
print(asc)
