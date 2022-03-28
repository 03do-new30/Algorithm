import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # use regular expression
        p = re.compile('[a-zA-Z]+')
        paragraph = p.findall(paragraph)
        # make lowercase
        paragraph = [x.lower() for x in paragraph]
        # Use Counter
        counter = collections.Counter(paragraph)
        # most common
        common_list = counter.most_common()
        for x in common_list:
            if x[0] in banned:
                continue
            else:
                return x[0]
        