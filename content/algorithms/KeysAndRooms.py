class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        isOpen = [False for i in range(len(rooms))]

        isOpen[0] = True  # 첫 방 이미 열림
        keyPocket = rooms[0]  # 이미 열린 첫번째방에서 열쇠 꺼냄

        while len(keyPocket) > 0:
            key = keyPocket.pop()  # 주머니에서 열쇠 하나꺼내서
            if isOpen[key] == False:  # 잠겨있으면?
                isOpen[key] = True  # 열고
                keyPocket.extend(rooms[key])  # 거기있는 열쇠 줍고

        if False in isOpen:
            return False
        return True