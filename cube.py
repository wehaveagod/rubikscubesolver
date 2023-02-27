import face
import numpy as np

# nums_to_colors = {0: "R",
#                   1: "B",
#                   2: "O",
#                   3: "G",
#                   4: "Y",
#                   5: "W"}

class Cube:
    def __init__(self, face1: face.Face, face2: face.Face, face3: face.Face, face4: face.Face, face5: face.Face, face6: face.Face):
        faces = np.array([face1, face2, face3, face4, face5, face6])

        self.red_face = None
        self.blue_face = None
        self.orange_face = None
        self.green_face = None
        self.yellow_face = None
        self.white_face = None

        self.color_faces = np.array([self.red_face, self.blue_face, self.orange_face, self.green_face, self.yellow_face, self.white_face])

        for face in faces:
            center_color_num = face.get_color_num(1, 1)
            self.color_faces[center_color_num] = face
    
    def get_color_num(self, center_color_num: int, first: int, second: int) -> int:
        return self.color_faces[center_color_num].get_color_num[first][second]

    def get_facing_front(self, center_color_num: int) -> bool:
        return self.color_faces[center_color_num].get_facing_front()

    def get_color_nums_array(self, center_color_num: int) -> np.array:
        return self.color_faces[center_color_num].get_color_nums_array()

    def set_facing_front(self, center_color_num: int):
        for i in range(len(self.color_faces)):
            if(i != center_color_num):
                self.color_faces[i].set_facing_front(False)
            else:
                self.color_faces[i].set_facing_front(True)
    
   
    
