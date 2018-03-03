"""
Contour tracing algorithm
"""

class Contour(object):
    """
    given a start pixel

    Directions
    =============
    d-u-l   v-u     d-u-r
    h-l     pixel   h-r
    d-d-l   v-d     d-d-r
    """

    directions = {"d-u-l": (-1, 1),
                    "d-u-r": (1, 1),
                    "v-u": (0, 1),
                    "v-d": (0, -1),
                    "d-d-l": (-1, -1),
                    "d-d-r": (1, -1),
                    "r": (1, 0),
                    "l": (-1, 0),}
    def __init__(self, img, start):
        """
        Initialize the parameters of the contour
        """
        self.start = start
        self.current = self.start
        self.img = img
        self.points = [self.start]
        self.direction = ""
        self.visited_directions = []
        self.start_trace()

    def get_next_pixel(self, delta):
        return (self.current[0] + delta[0],
                self.current[1] + delta[1])

    def start_trace(self):
        """
        sets the starting direction
        """
        for d in self.directions:
            coords = self.get_next_pixel(self.directions[d])
            if self.img[coords]:
                self.direction = d
                self.visited_directions.append(d)
                self.points.append(coords)
                self.current = coords
                self.trace()



    def retrace(self):
        """
        If all the points in a given direction have been expended
        tries a different passing direction
        """
        self.current = self.start
        for d in self.directions:
            if not d in self.visited_directions:
                coords = self.get_next_pixel(self.directions[d])
                
                if self.img[coords]:
                    self.direction = d
                    self.visited_directions.append(d)
                    self.points.append(coords)
                    self.trace()

        

    def trace(self):
        """
        Runs after the first pixel is found 
        """
        while True:
            coords = self.get_next_pixel(self.direction)

            if not self.img[coords]: 
                break
            else:
                self.points.append(coords)
                self.current = coords

        self.retrace()