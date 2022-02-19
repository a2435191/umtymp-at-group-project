from cmath import isclose
from ctypes import cast
from manim import *
from manim_rubikscube import *
from permutation_group_definition import write_group_defs
import numpy as np


class RubiksCubeGroup(Scene):
    def construct(self):
        write_group_defs(self, "Rubik's cube group", r"R_3", 
            ["F", "B", "U", "L", "D", "R"],
            "\circ"
        )
    
class DefineElements(ThreeDScene):
    def construct(self):
        cube = RubiksCube().scale(0.5).shift(IN)

        self.move_camera(phi=60 * DEGREES, theta = 45 * DEGREES)

        for cubie in cube.cubies.flatten():
            cubie: Cubie = cubie
            cubie.set_opacity(1.0)
         
        self.play(FadeIn(cube))
        actual_rubix_cube_center = VGroup(*cube.get_face("L"), *cube.get_face("R")).get_center()
        print(actual_rubix_cube_center)
        for axis in "FBUDLR":
            face = VGroup(*cube.get_face(axis))

            center = face.get_center() - actual_rubix_cube_center
            print("center", center)
            outwards_vector_normalized = center / np.sqrt(np.sum(center**2))
            
            arc = Arc(1.5, 0, 0.8 * TAU, color=GRAY)\
                .center()\
                .add_tip(tip_length=0.3)\
                .add_tip(at_start=True, tip_length=0.3)\
                .set_shade_in_3d()

            closeness = np.dot(arc.normal_vector, outwards_vector_normalized)
            if not isclose(abs(closeness), 1.0, abs_tol=0.01): # to avoid rotating around <0, 0, 0>
                
                rotate_around = np.cross(arc.normal_vector, outwards_vector_normalized)
                print(arc.normal_vector, outwards_vector_normalized, rotate_around)
                arc.rotate_about_origin(PI / 2, rotate_around)
                print(arc.normal_vector)

            arc.center()
            arc.shift(actual_rubix_cube_center + outwards_vector_normalized * 2.5)
            print("arc center", arc.get_arc_center())
            print("target", actual_rubix_cube_center + outwards_vector_normalized * 2.5)
            tex = Tex(
                f"${axis}$ ",
                "(clockwise)\n\n",
                f"${axis}'$ ",
                "(counterclockwise)", font_size=64)\
                .set_color_by_tex(axis, RED)\
                .shift(2.5 * UP, 3.5 * RIGHT)
            self.add_fixed_in_frame_mobjects(tex)
            self.add_fixed_orientation_mobjects(tex)

            self.play(
                AnimationGroup(
                    Write(arc),
                    FadeIn(tex),
                    CubeMove(cube, axis)
                )
            )
            self.wait(0.5)
            self.play(
                AnimationGroup(
                    CubeMove(cube, axis + "'"),
                    FadeOut(tex),
                    Unwrite(arc)
                )
            )
        
        self.play(FadeOut(cube))
        self.wait(0.5)
            
