def solution(string):
    answer = 0
    length = len(string)

    if length is 1:
        return 1
    else:
        for i in range(1, (length // 2) + 1):
            temp = string
            '''
            문자열을 잘라줌
            '''
            begin = 0
            end = begin + i

            splits = list()
            while temp:
                splits.append(temp[begin:end])
                temp = temp[end:]
            '''
            자른 문자열 순회
            '''
            newStr = ""
            before = splits[0]
            cnt = 1

            for idx, content in enumerate(splits):
                splits_length = len(splits)
                if idx:
                    if content == before:
                        cnt += 1
                        if idx == splits_length - 1:
                            newStr += (str(cnt) + before)
                    else:
                        if cnt > 1:
                            newStr += (str(cnt) + before)
                            if idx == (splits_length - 1):
                                newStr += content
                        else:
                            newStr += content
                            if idx == (splits_length - 1):
                                newStr += content
                        cnt += 1
                        before = content

            new_str_length = len(newStr)
            if new_str_length < answer:
                answer = new_str_length

    return answer


s = "abcabcdede"
print(solution(s))
