from turtle import right
from manim import *
from typing import List

class ArrayDefinition(Scene):
    """In the style of arraynotation.py
    """
    def construct(self):
        BRACKET_SIZE = 160
        CIRCLE_COLORS = ['#0000FF', '#FF0000', '#FFFF00']
        POSITIONS = [3 * LEFT, 0, 3 * RIGHT]

        set_label = Tex(r"$A\!=$", font_size=BRACKET_SIZE).shift(3 * LEFT + 0.8 * RIGHT)
        left_bracket = Tex(r"\{", font_size=BRACKET_SIZE).shift(1.0 * LEFT + 0.8 * RIGHT)
        right_bracket = Tex(r"\}", font_size=BRACKET_SIZE).shift(1.0 * RIGHT + 0.8 * RIGHT)

        self.play(
            left_bracket.animate.shift(3 * LEFT),
            set_label.animate.shift(3 * LEFT),
            right_bracket.animate.shift(3 * RIGHT)
        )

        circles = VGroup(*[Circle(0.8, color, fill_opacity=0.75).shift(pos + 0.8 * RIGHT) 
            for color, pos in zip(CIRCLE_COLORS, POSITIONS)])

        self.play(Create(circles))

        upper = VGroup(*circles, left_bracket, right_bracket)
        lower = upper.copy()
        upper.add(set_label)

        function_label = Tex(r"\underline{$f: A \rightarrow A$}").shift(5 * LEFT)

        
        self.play(upper.animate.shift(UP * 2), lower.animate.shift(DOWN * 2))
        self.play(Create(function_label))
        

        mapping = {0: 1, 2: 0, 1: 2}
        
        for i, (top_index, btm_index) in enumerate(mapping.items()):
            upper_circle = upper[top_index]
            lower_circle = lower[btm_index]


            arrow = Arrow(upper_circle, lower_circle)

            function_text_opener = Tex(r"$f($").shift(DOWN * 0.7 * (i + 1), LEFT * 5.9)
            function_input = upper_circle.copy().scale(0.2 / 100).move_to(function_text_opener).shift(0.4 * RIGHT)
            function_text_middle = Tex(r"$) = $").shift(DOWN * 0.7 * (i + 1) , LEFT * 5)
            function_output = lower_circle.copy().scale(0.2 / 100).move_to(function_text_middle).shift(0.6 * RIGHT)
        
            function_text = VGroup(function_text_opener, function_text_middle)
            
            self.play(AnimationGroup(
                Create(arrow), 
                Create(function_text), 
                ScaleInPlace(function_input, 100),
                ScaleInPlace(function_output, 100)
            ))

            self.wait()

class CycleDefinition(Scene):
    """In the style of cyclenotation.py
    """
    def construct(self):
        r = 0.5

        michael = Circle(radius=r, color='#0000FF', fill_color='#0000FF', fill_opacity=0.75)
        pramod = Circle(radius=r, color='#FF0000', fill_color='#FF0000', fill_opacity=0.75)
        will = Circle(radius=r, color='#FFFF00', fill_color='#FFFF00', fill_opacity=0.75)
        michael.move_to(array([-2, 0, 0]))
        will.move_to(array([2, 0, 0]))

        arr = [michael, pramod, will]
        ref_arr = deepcopy(arr)
        pos = [array([-2, 0, 0]), array([0, 0, 0]), array([2, 0, 0])]
        right = [Arc(radius=1, start_angle=PI, angle=PI).shift(array([1, 0, 0])),
                 Arc(radius=1, start_angle=0, angle=PI).shift(array([1, 0, 0]))]
        left = [Arc(radius=1, start_angle=PI, angle=-PI).shift(array([-1, 0, 0])),
                 Arc(radius=1, start_angle=0, angle=-PI).shift(array([-1, 0, 0]))]

        self.play(
            *[Create(obj) for obj in arr]
        )

        self.play(
            MoveAlongPath(arr[1], right[0]),
            MoveAlongPath(arr[2], right[1])
        )

        self.play(
            MoveAlongPath(arr[0], left[0]),
            MoveAlongPath(arr[2], left[1])
        )

        self.play(
            MoveAlongPath(arr[0], right[0]),
            MoveAlongPath(arr[1], right[1])
        )

        self.play(
            MoveAlongPath(arr[2], left[0]),
            MoveAlongPath(arr[1], left[1])
        )

        self.play(
            MoveAlongPath(arr[2], right[0]),
            MoveAlongPath(arr[0], right[1])
        )

        self.play(
            MoveAlongPath(arr[1], left[0]),
            MoveAlongPath(arr[0], left[1])
        )






        


