from string import ascii_lowercase

# dic_alpha = [{x:i} for i, x in enumerate(list(ascii_lowercase))]



def solution(s, skip, index):
    answer = ''
    alpha_list = [k for k in ascii_lowercase if k not in skip]
    for chr in s:
        answer += alpha_list[(alpha_list.index(chr) + index) % len(alpha_list)]

    return answer

s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))