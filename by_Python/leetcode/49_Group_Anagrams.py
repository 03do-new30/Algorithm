import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        for s in strs:
            # 애너그램 관계인 단어들을 정렬하면 서로 같은 값을 가진다
            key = "".join(sorted(s)) # join을 이용하여 문자열로 결합
            anagram[key].append(s)
        
        # return
        return anagram.values()