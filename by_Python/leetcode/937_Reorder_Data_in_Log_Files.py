class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # separate letter-logs and digit-logs
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier = log.split()[0]
            contents = log[len(identifier) + 1:]
            if contents[0].isalpha():
                letter_logs.append((identifier, contents))
            else:
                digit_logs.append((identifier, contents))
        
        # sort letter-logs lexicographically by their contents
        # if their contents are the same, then sort them lexicographically by their identifiers
        letter_logs = sorted(letter_logs, key = lambda x : (x[1], x[0]))
        
        # output
        answer = []
        for log in letter_logs:
            answer.append(log[0] + " " + log[1])
        for log in digit_logs:
            answer.append(log[0] + " " + log[1])
        return answer