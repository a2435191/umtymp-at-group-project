from manim import *
from typing import List

def write_group_defs(self: Scene, title_str: str, group_name_str: str,
    elements: List[str], operator_str: str, 
    title_font_size: int = 72, math_font_size: int = 64, *args, **kwargs) -> None:
    elements_with_commas: List[str] = []

    for elem in elements:
        elements_with_commas.append(",")
        elements_with_commas.append(elem)
    elements_with_commas = elements_with_commas[1:]
    

    title = Tex(r"\underline{" + title_str + r"}", font_size=title_font_size).shift(UP * 2)

    math = MathTex(
        group_name_str,
        r" = \left(\left\{",
        *elements_with_commas,
        r"\right\}, ",
        operator_str,
        r"\right)",

        font_size=math_font_size,
        *args, **kwargs
    )

    for elem in math[2:-3:2]:
        elem.set_color(RED)
    math[-2].set_color(BLUE)

    self.play(Write(title), Write(math))
    self.wait(1.7)
    self.play(Unwrite(title), Unwrite(math))
    self.wait(0.6)
