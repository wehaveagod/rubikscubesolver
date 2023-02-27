import numpy as np
import face
import cube

nums_to_colors = {0: "R",
                  1: "B",
                  2: "O",
                  3: "G",
                  4: "Y",
                  5: "W"}

face1 = face.Face(np.array(
                      [[0, 0, 0], 
                       [0, 0, 0], 
                       [0, 0, 0]]), False)

face2 = face.Face(np.array(
                      [[1, 1, 1], 
                       [1, 1, 1], 
                       [1, 1, 1]]), False)

face3 = face.Face(np.array(
                      [[2, 2, 2], 
                       [2, 2, 2], 
                       [2, 2, 2]]), False)

face4 = face.Face(np.array(
                      [[3, 3, 3], 
                       [3, 3, 3], 
                       [3, 3, 3]]), False)

face5 = face.Face(np.array(
                      [[4, 4, 4], 
                       [4, 4, 4], 
                       [4, 4, 4]]), False)

face6 = face.Face(np.array(
                      [[5, 5, 5], 
                       [5, 5, 5], 
                       [5, 5, 5]]), False)

rubiks = cube.Cube(face1, face2, face3, face4, face5, face6)

