class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        coor = [0, 0]  # 로봇의 좌표
        dir = [0, 1]  # 방향 (다음번에 이동할 위치)
        
        for ins in instructions:
            if ins == 'G':
                coor[0] += dir[0]
                coor[1] += dir[1]
            elif ins == 'L':
                dir[0],dir[1] = -dir[1],dir[0]
            elif ins == 'R':
                dir[0],dir[1] = dir[1],-dir[0]
        
        # 1. 로봇이 맨 처음 위치로 왔거나
        # 2. 혹은 방향이 처음의 방향(북)만 아니면 싸이클 가능
        if coor == [0, 0] or dir != [0, 1]:
            return True
        
        return False
