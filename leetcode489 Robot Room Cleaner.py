# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# Visual demo of the dfs trajectory: https://leetcode.com/problems/robot-room-cleaner/description/comments/1565306
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # initially the robot faces up
        self.dfs(robot, 0, 0, -1, 0, set())

    def dfs(self, robot: 'Robot', i: int, j: int, deltaI: int, deltaJ: int, visited: set):
        robot.clean()
        visited.add((i, j))

        for _ in range(4):
            ii, jj = i + deltaI, j + deltaJ
            # calling robot.move() will make robot move if there is no obstacle
            if (ii, jj) not in visited and robot.move():
                self.dfs(robot, ii, jj, deltaI, deltaJ, visited)
                # back to the starting point before dfs
                robot.turnLeft()
                robot.turnLeft()
                robot.move()

                # reset the direction. Because if we don't do:
                # 1) The direction will be messed up in the next for loop
                # 2) In the dfs recursion, the next backward recursion will run line 53 & 53 (turn robot 180 degree and
                # back by one cell), which requires the direction to be same as before doing dfs
                robot.turnRight()
                robot.turnRight()

            robot.turnRight()
            # clockwise change the dfs direction:
            # (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
            deltaI, deltaJ = deltaJ, -deltaI
