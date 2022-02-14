from manim import *
from manim_rubikscube import *
import math

class Rubiks(ThreeDScene):
    def construct(self):
        # After creating the RubiksCube, it may be necessary to scale it to
        # comfortably see the cube in the camera's frame
        cube = RubiksCube().scale(0.6)
        cube.set_sheen(0)

        # Setup where the camera looks
        self.move_camera(phi=45 * DEGREES, theta=135 * DEGREES)
        self.renderer.camera.frame_center = cube.get_center()

        # At this point, you have created a RubiksCube object.
        # All that's left is to add it to the scene.

        # A RubiksCube acts as any other Mobject. It can be added with
        # self.add() or any Manim creation animation
        self.play(
            FadeIn(cube)
        )
        self.wait(2)

        self.play(
            CubeMove(cube, 'F', run_time=0.5)
        )
        self.wait(2)
