class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # it depends on the traval time
        # use (target - position[i]) / speed[i] to get time, then we can group by time
        position_speed = [(position[i], speed[i]) for i in range(len(position))]
        position_speed.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for ps in position_speed:
            time = (target - ps[0]) / ps[1]
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)