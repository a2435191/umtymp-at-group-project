from manim import *
import sys

def draw_intro(self: Scene, section_number: int, subtitle: str) -> None:
        text = MarkupText(
            f"Section {section_number}:\n<span size=\"xx-small\">{subtitle}</span>", 
            font_size=100
        )
        self.play(Write(text, run_time=5))
        self.wait(0.3)
        self.play(text.animate.shift(DOWN * 10))
        self.wait()


class Intro1(Scene):
    def construct(self):
        draw_intro(self, 1, "What is a permutation group?")

class Intro2(Scene):
    def construct(self):
        draw_intro(self, 2, "Examples of permutation groups")

class Intro3(Scene):
    def construct(self):
        draw_intro(self, 3, "Properties and theorems")

class Intro4(Scene):
    def construct(self):
        draw_intro(self, 4, "Related math theory")
        
    
    
