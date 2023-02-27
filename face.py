import numpy as np

# nums_to_colors = {0: "R",
#                   1: "B",
#                   2: "O",
#                   3: "G",
#                   4: "Y",
#                   5: "W"}

class Face:
    def __init__(self, color_nums_array: np.array, facing_front: bool):
        if(np.shape(color_nums_array) != (3, 3)):
            raise ValueError("Shape must be 3x3")
        
        for arr in color_nums_array:
            for n in arr:
                if(n < 0 or n > 6):
                    raise ValueError("All numbers must be between greater than or equal to 0 and less than or equal to 6")
        
        self.color_nums_array = color_nums_array
        self.facing_front = facing_front
    
    def get_color_num(self, first: int, second: int) -> int:
        return self.color_nums_array[first][second]
    
    def get_facing_front(self) -> bool:
        return self.facing_front
    
    def get_color_nums_array(self) -> np.array:
        return self.color_nums_array
    
    def set_facing_front(self, change_facing: bool):
        self.facing_front = change_facing

    # def __str__(self) -> str:
    #     return (np.array2string(np.vectorize(lambda k: nums_to_colors[k])(self.nums)))