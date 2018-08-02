from PyQt5.QtGui import QMatrix4x4, QVector3D
import OpenGL.GL as gl
import numpy as np


class Cube(object):

    LEN = 0.5
    N_VERTEX = 24
    VERTICES = np.array([
         1,  1,  1,
        -1,  1,  1,
        -1, -1,  1,
         1, -1,  1,

         1,  1, -1,
        -1,  1, -1,
        -1, -1, -1,
         1, -1, -1,

         1, -1,  1,
        -1, -1,  1,
        -1, -1, -1,
         1, -1, -1,

         1,  1,  1,
        -1,  1,  1,
        -1,  1, -1,
         1,  1, -1,

        -1,  1,  1,
        -1, -1,  1,
        -1, -1, -1,
        -1,  1, -1,

         1,  1,  1,
         1, -1,  1,
         1, -1, -1,
         1,  1, -1,

    ], dtype=np.float32) * LEN

    COLORS = np.array([
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        1, 1, 0,
        1, 1, 0,
        1, 1, 0,
        1, 1, 0,
        0, 1, 1,
        0, 1, 1,
        0, 1, 1,
        0, 1, 1,
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
    ], dtype=np.uint8) * 255

    def __init__(self, size=1, pose=None):
        self.size = size
        self.pose = QMatrix4x4() if pose is None else QMatrix4x4(pose)

    def draw(self):
        gl.glPushMatrix()
        gl.glMultMatrixf(self.pose.data())

        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.VERTICES)
        gl.glColorPointer(3, gl.GL_UNSIGNED_BYTE, 0, self.COLORS)
        gl.glDrawArrays(gl.GL_QUADS, 0, self.N_VERTEX)

        gl.glPopMatrix()