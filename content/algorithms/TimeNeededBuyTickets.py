class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        kthTicketCnt = tickets[k]  # k번째 사람이 사려는 티켓 수
        time = kthTicketCnt
        for ticket in tickets[:k]:
            if ticket >= kthTicketCnt:  # k티켓수보다 크면 나머진 빼고 k티켓수만큼만 누적
                time += kthTicketCnt
            else:                       # k티켓수보다 작으면 그 값만큼만 누적
                time += ticket
        for ticket in tickets[k+1:]:
            if ticket >= kthTicketCnt-1:
                time += kthTicketCnt-1
            else:
                time += ticket
        return time

# 한장사면 맨뒤로 가니깐 k만큼은 돌고돌기를 반복한다는 뜻

# 0~k까지는
# k번째 사람이 사려는 티켓 숫자보다 같.작 인 갯수만큼만 카운트하면됨
# k~마지막은
# k번째 사람이 사려느 티켓 숫자보다 작은것만 셈(k번째 사람이 다 사기만하면 뒤에는 볼 필요 없으니까)

# 그러니 k보다 큰지, 같.크인지 나눠서 확인하면됨