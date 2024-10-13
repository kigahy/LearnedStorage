# BFS로 풀려고 했는데, 방문체크가 어려워서 DFS로 접근하였습니다. (그런데 재귀도 방문체크가 필요한가요?)
# words 중 begin의 길이와 -1만큼 일치하는 단어가 있다면 그 단어로 재귀호출합니다.

def changeWord(begin, target, words, answer):  # 시작단어, 타깃단어, 단어들, 바꾼 횟수
    if target not in words:  # 바꿀 수 없는 경우라면 0 리턴
        return 0

    if begin == target:
        return  # 시작값이 타깃과 같아졌다면 재귀 종료

    for i in range(len(words)):  # words의 단어는 인덱스 번호인 i로 접근하여 visited를 쉽게 체크하도록 함
        count = 0  # begin과 words의 단어 길이 비교할 변수

        for j in words[i]:  # 해당 words의 알파벳 하나하나 떼어 봄
            for k in begin:  # begin의 알파벳 하나하나 떼어 봄

                if j == k:  # 각 단어들이 같다면
                    count += 1  # count += 1 세어줌
                if count == len(begin) - 1 and visited[i] == 0:  # 만약 알파벳 한 개 빼고 다 맞다면, 해당 word를 방문하지 않았다면
                    answer += 1  # 변경 숫자 세어줌
                    visited[i] = 1  # 해당 인덱스의 방문체크
                    changeWord(words[i], target, words, answer)  # 해당 word로 바꾼 후 재귀호출
                    break

            else:  # 단어들이 모두 틀렸다는 말이므로 다음 word 순회하러 break
                break


def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)  # 방문체크 할 리스트
    changeWord(begin, target, words, answer)
    return answer