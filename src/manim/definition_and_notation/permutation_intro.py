from manim import *

class PermutationIntro(Scene):
    def construct(self):
        original_text = Tex("What is a permutation", " group", "?", font_size=75)
        self.play(Write(original_text))
        self.play(
            original_text[0].animate.shift(RIGHT * 1.1),
            original_text[1].animate.shift(DOWN * 10),
            original_text[2].animate.shift(LEFT * 1.1)
        )
        self.wait(1.0)
        self.play(original_text.animate.shift(DOWN * 10))
        self.wait()