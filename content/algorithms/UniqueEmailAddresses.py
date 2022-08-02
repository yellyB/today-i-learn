class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        confirmed = set()
        for email in emails:
            splited = email.split('@')
            splitedWithPlus = splited[0].split('+')[0]
            confirmed.add(splitedWithPlus.replace('.','')+'@'+splited[-1])
            
        return len(confirmed)
