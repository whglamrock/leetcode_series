
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direction_to_length = {'north' : 0, 'south' : 0, 'west' : 0, 'east': 0}
        direction = 'north'
        left_order = {'north' : 'west', 'west' : 'south', 'south' : 'east', 'east': 'north'}
        right_order = {'north' : 'east', 'east' : 'south', 'south' : 'west', 'west': 'north'}

        for i in range(4):
            for step in instructions:
                if step == 'G':
                    direction_to_length[direction] += 1
                elif step == 'L':
                    direction = left_order[direction]
                else:
                    direction = right_order[direction]

        return direction_to_length['north'] == direction_to_length['south'] and direction_to_length['west'] == direction_to_length['east']