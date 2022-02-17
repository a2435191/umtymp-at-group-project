# Written by Pramod Anandarao

from manim import *
import numpy as np
import math

class PermutationDefinition(Scene):
    def construct(self):
        title = Tex(r'\textbf{Definitions:}',r' Permutation of $A$, Permutation Group of $A$', color=YELLOW)
        text = Tex(r'A \textit{permutation} of a set $A$ is a function from $A$ to $A$\\that is both one-to-one and onto. A \textit{permutation group}\\ of a set $A$ is a set of permutations of $A$ that forms a\\ group under function composition.')
        #text[1].set_color(YELLOW)
        #text[3].set_color(YELLOW)

        VGroup(title, text).arrange(DOWN)

        self.play(Write(title), Write(text))
