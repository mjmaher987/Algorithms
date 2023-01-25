# از دیسچوینت ست ها همانطور که در ادامه میبینید استفاده  کرده ایم
class disjoint_set_to_find_hambandy:
    def __init__(self, n):
        self.main_array = [i for i in range(n)]
        self.rank_of_main_array = [1] * n

    def union_disjoint_set(self, first_to_union, second_to_union):
        f_parent_first_to_union, f_parent_second_to_union = self.find_disjoint_set(
            first_to_union), self.find_disjoint_set(second_to_union)
        if f_parent_second_to_union == f_parent_first_to_union:
            return
        if self.rank_of_main_array[f_parent_second_to_union] > self.rank_of_main_array[f_parent_first_to_union]:
            self.main_array[f_parent_first_to_union] = f_parent_second_to_union
        elif self.rank_of_main_array[f_parent_first_to_union] > self.rank_of_main_array[f_parent_second_to_union]:
            self.main_array[f_parent_second_to_union] = f_parent_first_to_union
        else:
            self.main_array[f_parent_first_to_union] = f_parent_second_to_union
            self.rank_of_main_array[f_parent_second_to_union] += 1

    def find_disjoint_set(self, to_find):
        while to_find != self.main_array[to_find]:
            self.main_array[to_find] = self.main_array[self.main_array[to_find]]
            to_find = self.main_array[to_find]
        return to_find


class E:
    def __init__(self, weight, start, end, real_index):
        self.weight = weight
        self.start = start
        self.end = end
        self.real_index = real_index

    def __lt__(self, other):
        return self.weight < other.weight


def initialize(m):
    all_E = []
    all_weights = 0
    for i in range(m):
        start, end, weight = map(int, input().split())
        all_E.append(E(weight, start - 1, end - 1, i))
        all_weights += weight
    all_E.sort()
    return all_E, all_weights


def find_first_answer():
    k = disjoint_set_to_find_hambandy(n)
    first_answer = 0
    for e in all_E:
        a = e.start
        b = e.end
        set_of_a = k.find_disjoint_set(a)
        set_of_b = k.find_disjoint_set(b)
        if set_of_a != set_of_b:
            first_answer += e.weight
            k.union_disjoint_set(a, b)
    return first_answer


def check(main_e):
    k = disjoint_set_to_find_hambandy(n)
    weight_of_e = main_e.weight
    for e_ in all_E:
        if e_.weight >= weight_of_e:
            break
        a = e_.start
        b = e_.end
        a_index = k.find_disjoint_set(a)
        b_index = k.find_disjoint_set(b)
        if a_index != b_index:
            k.union_disjoint_set(a, b)
    a_of_e = main_e.start
    b_of_b = main_e.end
    index_a_main = k.find_disjoint_set(a_of_e)
    index_b_main = k.find_disjoint_set(b_of_b)
    if index_a_main != index_b_main:
        return True
    return False


def find_second_answer():
    answer_two = ["0" for i in range(m)]
    for e in all_E:
        check_ = check(e)
        if check_:
            answer_two[e.real_index] = "1"
    return "".join(answer_two)


if __name__ == '__main__':
    n, m = map(int, input().split())
    all_E, all_weights = initialize(m)
    first_answer = find_first_answer()
    print(all_weights - first_answer)
    second_answer = find_second_answer()
    print(second_answer)

'''
در قسمت پایین شبه کد مربوط به این سوال نوشته شده است
for e in sorted(E):
	e = (a, b)
	set_of_a = find_set(a)
	set_of_b = find_set(b)
	if set_of_a == set_of_b:
		nothing
	else:
		union(set_of_a, set_of_b)

# disjoint sets

for e in sorted(E):
	check(e)

def check(e):
	smaller = all_smaller_edges_than_e
	if can add e to smaller such that no circules is created --> it can be in any answer
	otherwise: it cants
'''
