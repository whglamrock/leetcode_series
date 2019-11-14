
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

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # initially the robot faces up
        self.dfs(robot, 0, 0, -1, 0, set())

    def dfs(self, robot, i, j, direction_i, direction_j, visited):
        robot.clean()
        visited.add((i, j))

        for _ in xrange(4):
            next_i, next_j = i + direction_i, j + direction_j
            # calling robot.move() will make robot move if there is no obstacle
            if (next_i, next_j) not in visited and robot.move():
                self.dfs(robot, next_i, next_j, direction_i, direction_j, visited)
                # get back to the starting point before dfs
                robot.turnLeft()
                robot.turnLeft()
                robot.move()

                # turn robot to the original facing direction
                robot.turnRight()
                robot.turnRight()

            robot.turnRight()
            # clockwise change the dfs direction:
                # (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
            direction_i, direction_j = direction_j, -direction_i










