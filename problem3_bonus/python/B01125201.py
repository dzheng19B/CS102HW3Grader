#4/7, 2069. Walking Robot Simulation II (I chose a bad day to do this)

class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """

        self.dir = "East"
        self.pos = [0, 0]
        self.width = width
        self.height = height
                
        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        og = num
        num = num % ((2 * (self.width - 1)) + (2 * (self.height - 1)))
        if num == 0 and og > 0 and self.pos == [0, 0]:
            self.dir = "South"

        while num > 0:
            if self.dir == "East":
                new = self.pos[0] + num
                if new < self.width:
                    self.pos = [new, 0]
                    num = 0
                else:
                    num -= self.width - 1 - self.pos[0]
                    self.dir = "North"
                    self.pos[0] = self.width - 1

            if self.dir == "North":
                new = self.pos[1] + num
                if new < self.height:
                    self.pos = [self.width - 1, new]
                    num = 0
                else:
                    num -= self.height - 1 - self.pos[1]
                    self.dir = "West"
                    self.pos[1] = self.height - 1
            
            if self.dir == "West":
                new = self.pos[0] - num
                if new >= 0:
                    self.pos = [new, self.height - 1]
                    num = 0
                else:
                    num -= self.pos[0]
                    self.dir = "South"
                    self.pos[0] = 0

            if self.dir == "South":
                new = self.pos[1] - num
                if new >= 0:
                    self.pos = [0, new]
                    num = 0
                else:
                    num -= self.pos[1]
                    self.dir = "East"
                    self.pos[1] = 0



        

    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.pos
        

    def getDir(self):
        """
        :rtype: str
        """
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
