# Written by Pramod Anandarao

from manim import *
import numpy as np
from numpy import array
import math
import random


class PileOfTheorems(Scene):
    def construct(self):
        # boxes
        rect1 = Rectangle(width=4.0, height=2.0, color=YELLOW).shift(LEFT*4.5+UP*1.25)
        rect2 = Rectangle(width=4.0, height=2.0, color=YELLOW).shift(LEFT*4.5+DOWN*1.25)
        rect3 = Rectangle(width=4.0, height=2.0, color=YELLOW).shift(UP*2.5)
        rect4 = Rectangle(width=4.0, height=2.0, color=YELLOW)
        rect5 = Rectangle(width=4.0, height=2.0, color=YELLOW).shift(DOWN*2.5)
        rect6 = Rectangle(width=4.0, height=2.0, color=YELLOW).shift(RIGHT*4.5+UP*1.25)
        rect7 = Rectangle(width=4.0, height=2.0, color=YELLOW).shift(RIGHT*4.5+DOWN*1.25)


        # Theorem 5.1
        sf1 = 0.4
        t1t = Tex(r'\underline{Products of Disjoint Cycles}', color=YELLOW).scale(sf1)
        t1l = Tex(r'Every permutation of a finite set can\\be written as a cycle or as a product\\of disjoint cycles.').scale(sf1)
        THEOREM1 = VGroup(t1t, t1l).arrange(DOWN, buff=0.1).move_to(rect1)
        W1 = VGroup(THEOREM1, rect1)

        # Theorem 5.2
        sf2 = 0.4
        t2t = Tex(r'\underline{Disjoint Cycles Commute}', color=YELLOW).scale(sf2)
        t2l = Tex(r'If the pair of cycles\\$\alpha=(a_1, a_2,\dots ,a_m)$ and $\beta=(b_1, b_2,\dots ,b_n)$\\have no entries in common, then $\alpha\beta=\beta\alpha$').scale(sf2)
        THEOREM2 = VGroup(t2t,t2l).arrange(DOWN, buff=0.1).move_to(rect2)
        W2 = VGroup(THEOREM2, rect2)

        # Theorem 5.3
        sf3 = 0.4
        t3t = Tex(r'\underline{Order of a Permutation}', color=YELLOW).scale(sf3)
        t3l = Tex(r'The order of a permutation of a finite\\set written in disjoint cycle form is the\\least common multiple of the lengths\\of the cycles.').scale(sf3)
        THEOREM3 = VGroup(t3t,t3l).arrange(DOWN, buff=0.1).move_to(rect3)
        W3 = VGroup(THEOREM3, rect3)

        # Theorem 5.4
        sf4 = 0.4
        t4t = Tex(r'\underline{Product of 2-Cycles}', color=YELLOW).scale(sf4)
        t4l = Tex(r'Every permutation in $S_n$, $n>1$, is\\a product of 2-cycles.').scale(sf4)
        THEOREM4 = VGroup(t4t,t4l).arrange(DOWN, buff=0.1).move_to(rect4)
        W4 = VGroup(THEOREM4, rect4)

        # Theorem 5.5
        sf5 = 0.4
        t5t = Tex(r'\underline{Always Even or Always Odd}', color=YELLOW).scale(sf5)
        t5l = Tex(r"If $\alpha=\beta_1\beta_2\dots\beta_r$ and $\alpha=\gamma_1\gamma_2\dots\gamma_s$\\where the $\beta$'s and the $\gamma$'s are 2-cycles,\\then $r$ and $s$ are both even or both odd.").scale(sf5)
        THEOREM5 = VGroup(t5t,t5l).arrange(DOWN, buff=0.1).move_to(rect5)
        W5 = VGroup(THEOREM5, rect5)

        # Theorem 5.6
        sf6 = 0.4
        t6t = Tex(r'\underline{Even Permutations Form a Group}', color=YELLOW).scale(sf6)
        t6l = Tex(r'The set of even permutations in $S_n$\\forms a subgroup of $S_n$.').scale(sf6)
        THEOREM6 = VGroup(t6t,t6l).arrange(DOWN, buff=0.1).move_to(rect6)
        W6 = VGroup(THEOREM6, rect6)

        # Theorem 5.7
        sf7 = 0.4
        t7t = Tex(r'\underline{Order of Alternating Group}', color=YELLOW).scale(sf7)
        t7l = Tex(r'For $n>1$, $A_n$ has order $n!/2$').scale(sf7)
        THEOREM7 = VGroup(t7t,t7l).arrange(DOWN, buff=0.1).move_to(rect7)
        W7 = VGroup(THEOREM7, rect7)

        #corn0.add_updater(lambda m: corn0.move_to(cornerdots[0].get_center()))


        # animations
        self.play(Create(rect1), Create(rect2), Create(rect3), Create(rect4), Create(rect5), Create(rect6), Create(rect7))
        self.play(Write(THEOREM1), Write(THEOREM2), Write(THEOREM3), Write(THEOREM5), Write(THEOREM4), Write(THEOREM6), Write(THEOREM7))

        def randomfloat(mobj, s):
            return mobj.animate(run_time=abs(s*20), rate_func=rate_functions.smooth).shift(UP*s)

        a = 0.05
        self.play(randomfloat(W1, a), randomfloat(W2, -a), randomfloat(W3, a), randomfloat(W4, -a), randomfloat(W5, a), randomfloat(W6, -a), randomfloat(W7, a))
        for i in range(4):
            #self.play(randomfloat(W1, a), randomfloat(W2, -a), randomfloat(W3, a), randomfloat(W4, -a), randomfloat(W5, a), randomfloat(W6, -a), randomfloat(W7, a))
            #self.play(randomfloat(W1, -a), randomfloat(W2, a), randomfloat(W3, -a), randomfloat(W4, a), randomfloat(W5, -a), randomfloat(W6, 0.1), randomfloat(W7, -0.1))
            self.play(randomfloat(W1, -a*2), randomfloat(W2, a*2), randomfloat(W3, -a*2), randomfloat(W4, a*2), randomfloat(W5, -a*2), randomfloat(W6, a*2), randomfloat(W7, -a*2))
            self.play(randomfloat(W1, a*2), randomfloat(W2, -a*2), randomfloat(W3, a*2), randomfloat(W4, -a*2), randomfloat(W5, a*2), randomfloat(W6, -a*2), randomfloat(W7, a*2))
        self.play(randomfloat(W1, -a), randomfloat(W2, a), randomfloat(W3, -a), randomfloat(W4, a), randomfloat(W5, -a), randomfloat(W6, a), randomfloat(W7, -a))
        #self.play(VGroup(THEOREM1, THEOREM2, THEOREM3, THEOREM4, THEOREM5, THEOREM6, THEOREM7).animate(run_time=2, rate_func=rate_functions.smooth).shift(UP*0.3))

class PileOfDefinitions(Scene):
    def construct(self):
        d1 = Line([-7/3, 5, 0], [-7/3, -5, 0], color=YELLOW)
        d2 = Line([7/3, 5, 0], [7/3, -5, 0], color=YELLOW)

        # disjoint cycles
        DisjointTitle = Tex(r'Disjoint Cycles', color=YELLOW).move_to([-14/3, 2, 0])
        DisjointDef = Tex(r'Two cycles are\\said to be \textit{disjoint}\\ if no element\\ appears in both.')
        DisjointDef.next_to(DisjointTitle, DOWN)
        #VGroup(DisjointTitle, DisjointDef).move_to([-14/3, 0, 0])

        # parity
        ParityTitle = Tex(r'Even and Odd\\ Permutations', color=YELLOW).move_to([0, 2, 0])
        ParityDef = Tex(r'A permutation that can be\\ expressed as a product of\\ an even number of 2-cycles\\ is called an \textit{even}\\ permutation. A permutation\\ that can be expressed as\\ a product of an odd number\\ of 2-cycles is called an \textit{odd}\\ permutation.').scale(0.65)
        ParityDef.next_to(ParityTitle, DOWN)
        #VGroup(ParityTitle, ParityDef).move_to([0, 0, 0])

        # alternating group
        AlternatingTitle = Tex(r'Alternating Groups', color=YELLOW).move_to([14/3, 2, 0])
        AlternatingDef = Tex(r'The group of\\ even permutations\\ of $n$ symbols\\ is denoted by $A_n$\\ and is called the\\ \textit{alternating group\\ of degree} $n$.')
        AlternatingDef.next_to(AlternatingTitle, DOWN)
        #VGroup(AlternatingTitle, AlternatingDef).move_to([14/3, 0, 0])


        self.play(Create(d1), Create(d2), Write(DisjointTitle), Write(ParityTitle), Write(AlternatingTitle))
        self.play(Write(DisjointDef), Write(ParityDef), Write(AlternatingDef))
