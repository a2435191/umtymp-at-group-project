# Written by Prmaod Anandarao

from manim import *
from numpy import array
import math
import string
from copy import deepcopy

# you need the font installed
class CaesarCypher(Scene):
    def construct(self):
        font_name = 'Red Hat Mono Light'

        pmatrix = Matrix([[str(i) for i in range(26)],['23','24','25']+[str(i) for i in range(23)]], h_buff=0.7, element_alignment_corner=array([ 0., 0., 0.])).scale(0.65)

        rectt = Rectangle(width=28, height=14/26, grid_xstep=14/26, color=BLUE).shift(UP)
        rectb = Rectangle(width=28, height=14/26, grid_xstep=14/26, color=RED).shift(DOWN)

        linet = Line(start=[-8,0,0], end=[8,0,0], color=BLUE)
        lineb = Line(start=[-8,0,0], end=[8,0,0], color=RED)
        linet.next_to(rectt, UP*14/6.5)
        lineb.next_to(rectb, DOWN*14/6.5)
        linett = Line(start=[-8,0,0], end=[8,0,0], color=BLUE)
        linebb = Line(start=[-8,0,0], end=[8,0,0], color=RED)
        linett.move_to(linet.get_center()+DOWN*14/26)
        linebb.move_to(lineb.get_center()+UP*14/26)

        capt = Tex('Standard Alphabet').scale(0.75)
        capb = Tex('Shifted Alphabet').scale(0.75)
        capt.shift(UP*(1+14/26))
        capb.shift(DOWN*(1+14/26))

        letterst = VGroup(*[Text(i, font=font_name).scale(0.8) for i in 3*string.ascii_uppercase])
        lettersb = VGroup(*[Text(i, font=font_name).scale(0.8) for i in 3*string.ascii_uppercase])

        numst = VGroup(*[Tex(str(i)).scale(0.75) for i in 3*[j for j in range(26)]])
        numsb = VGroup(*[Tex(str(i)).scale(0.75) for i in 3*[j for j in range(26)]])

        for i in range(78):
            letterst[i].move_to([-14-7+7/26+14/26*i,1,0])
            lettersb[i].move_to([-14-7+7/26+14/26*i,-1,0])
            numst[i].move_to([-14-7+7/26+14/26*i,1,0])
            numsb[i].move_to([-14-7+7/26+14/26*i,-1,0])

        arr0 = VGroup(*[Arrow(start=[0,0.75,0], end=[0,-0.75,0], tip_length=0.15, color=YELLOW, stroke_width=4) for i in range(26*3)])
        for i in range(26*3):
                arr0[i].move_to([-14-7+14/26*i+7/26, 0, 0])


        arr3 = VGroup(*[Arrow(start=[0,0.75,0], end=[-3*14/26-7/26-7/52,-0.75,0], tip_length=0.15, color=YELLOW, stroke_width=4) for i in range(26*3)])
        for i in range(26*3):
                arr3[i].move_to([-14-7+14/26*(i+2+7/26)-7/52-3*14/26, 0, 0])
        arr0recolor = VGroup(*[arr0[i] for i in [41, 30, 43, 38, 46, 45, 26, 45, 34, 40, 39]])

        self.play(Create(rectt), Create(rectb), Write(letterst), Write(lettersb))

        self.wait(2)

        self.add(linett, linebb)
        self.play(Write(arr3))
        self.play(ReplacementTransform(arr3, arr0), VGroup(lettersb, rectb).animate.shift(RIGHT*3*14/26))
        self.play(Write(linet), Write(lineb), Write(capt), Write(capb))

        self.wait(2)

        inputtext1 = Tex(r'Plaintext:')
        inputtext2 = VGroup(*[Text(i, font=font_name).scale(0.8) for i in 'PERMUTATION']).arrange()
        inputtext2ul = VGroup(*[deepcopy(Underline(inputtext2[3], color=YELLOW)).next_to(inputtext2[i], DOWN/2) for i in range(len(inputtext2))])
        inputtext2ul.arrange()
        inputtext2 = VGroup(*[inputtext2[i].next_to(inputtext2ul[i], UP/2) for i in range(len(inputtext2))])
        inputtext2 = VGroup(inputtext1, VGroup(inputtext2ul, inputtext2)).arrange()

        inputtext2.move_to([0,(4+linet.get_y())/2,0])

        outputtext1 = Tex(r'Ciphertext:')
        outputtext2 = VGroup(*[Text(i, font=font_name, color=RED).scale(0.8) for i in 'MBOJRQXQFLK']).arrange()
        outputtext2ul = deepcopy(inputtext2ul)
        outputtext2 = VGroup(*[outputtext2[i].next_to(outputtext2ul[i], UP/2) for i in range(len(outputtext2))])
        outputtext2 = VGroup(outputtext1, VGroup(outputtext2ul, outputtext2)).arrange()

        outputtext2.move_to([0,(-4+lineb.get_y())/2,0])

        alertrect = Rectangle(width=14/26, height=14/26, fill_color=BLUE).set_fill(opacity=0)
        alertst = VGroup(*[deepcopy(alertrect).move_to(letterst[i]) for i in [41, 30, 43, 38, 46, 45, 26, 45, 34, 40, 39]])
        alertsb = VGroup(*[deepcopy(alertrect.set_fill(color=RED)).move_to(lettersb[i]) for i in [41-3, 30-3, 43-3, 38-3, 46-3, 45-3, 26-3, 45-3, 34-3, 40-3, 39-3]])

        self.play(Write(inputtext2), Write(outputtext2[0]), Write(outputtext2[1][0]))

        self.wait(2)

        self.add_foreground_mobjects(rectt, letterst, rectb, lettersb)

        lr = 0.75
        rt=5
        self.play(arr0recolor.animate(lag_ratio=lr, run_time=rt).set_stroke(color=BLUE).set_fill(color=RED), alertst.animate(lag_ratio=lr, run_time=rt).set_fill(opacity=0.5), alertsb.animate(lag_ratio=lr, run_time=rt).set_fill(opacity=0.5), inputtext2[1][1].animate(lag_ratio=lr, run_time=rt).set_fill(color=BLUE), Write(outputtext2[1][1], lag_ratio=lr, run_time=rt))

        self.wait(2)

        self.play(Unwrite(arr0), Uncreate(alertst), Uncreate(alertsb), Unwrite(inputtext2), Unwrite(outputtext2))
        #self.play(VGroup(lettersb, rectb).animate.shift(LEFT*3*14/26))
        self.play(ReplacementTransform(letterst, numst), ReplacementTransform(lettersb, numsb.shift(RIGHT*3*14/26)))

        ent = Tex(r'Encryption:', color=BLUE)
        dnt = Tex(r'Decryption:', color=RED)
        en = MathTex(r'E_n(x)=(x+n)\,\mod\,26')
        dn = MathTex(r'D_n(x)=(x-n)\,\mod\,26')

        ent = VGroup(ent, en).arrange().move_to(inputtext2)
        dnt = VGroup(dnt, dn).arrange().move_to(outputtext2)

        e3 = MathTex(r'E_3(x)=(x+3)\,\mod\,26').move_to(ent[1])
        d3 = MathTex(r'D_3(x)=(x-3)\,\mod\,26').move_to(dnt[1])

        self.play(Write(ent))

        self.wait(2)

        self.play(Write(dnt))

        self.wait(2)

        self.play(ReplacementTransform(en, e3), ReplacementTransform(dn, d3))

        self.wait(2)

        # self.play(ReplacementTransform(VGroup(rectt, rectb, numst, numsb), pmatrix))
        rows = pmatrix.get_rows()
        self.play(
            FadeOut(rectt),
            FadeOut(rectb),
            *[FadeOut(obj) for obj in [numst[:26], numst[52:], numsb[:26-3], numsb[52-3:]]]
        )
        self.play(
            ReplacementTransform(numst[26:52], rows[0]),
            ReplacementTransform(numsb[26-3:52-3], rows[1])
        )
        self.play(
            Write(pmatrix.get_brackets())
        )

        self.wait(0.2)
