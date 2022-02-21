from manim import *
import numpy as np
from numpy import array
from copy import deepcopy
import math

class ArrayNotationMappingObjects(Scene):
    def construct(self):
        r = 0.5

        vg = VGroup()
        michael = Circle(radius=r, color='#0000FF', fill_color='#0000FF', fill_opacity=0.75)
        pramod = Circle(radius=r, color='#FF0000', fill_color='#FF0000', fill_opacity=0.75)
        will = Circle(radius=r, color='#FFFF00', fill_color='#FFFF00', fill_opacity=0.75)
        michael.move_to(array([-2, 0, 0]))
        will.move_to(array([2, 0, 0]))

        vg.add(michael, pramod, will)

        transforms = []
        horiz_spread = 4
        vert_spread = 4
        vert_shift = 0.75

        for j in reversed(range(2)):
            for i in range(3):
                new = vg.copy().scale(0.5)
                new.move_to(array([(i-1)*horiz_spread, (j-0.5)*vert_spread + vert_shift, 0]))
                transforms.append(new)


        self.play(
            Create(vg)
        )

        self.wait(2)

        perms = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        inv_perms = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [2, 0, 1], [1, 2, 0], [2, 1, 0]]

        translated = []
        for i in range(6):
            pos = {j: transforms[i][j].get_center() for j in range(3)}
            new_group = transforms[i].copy()
            for n in range(3):
                new_group[n].move_to(pos[n])
                new_group[n].shift(array([0, -1.5, 0]))
            translated.append(new_group)

        permed = []
        for i in range(6):
            pos = {j: transforms[i][perms[i][j]].get_center() for j in range(3)}
            new_group = transforms[i].copy()
            for n in range(3):
                new_group[n].move_to(pos[n])
                new_group[n].shift(array([0, -1.5, 0]))
            permed.append(new_group)

        arrows = [Line(
                        start=transforms[i][j].get_center() + 0.33 * (permed[i][j].get_center() - transforms[i][j].get_center()) / np.linalg.norm((permed[i][j].get_center() - transforms[i][j].get_center())),
                        end=permed[i][j].get_center() - 0.33 * (permed[i][j].get_center() - transforms[i][j].get_center()) / np.linalg.norm((permed[i][j].get_center() - transforms[i][j].get_center())),
        ).add_tip(tip_length=0.15) for i in range(6) for j in range(3)]

        shifted_arrows = [Line(
            start=transforms[i][j].get_center() + 0.33 * (
                        permed[i][inv_perms[i][j]].get_center() - transforms[i][j].get_center()) / np.linalg.norm(
                (permed[i][inv_perms[i][j]].get_center() - transforms[i][j].get_center())),
            end=permed[i][inv_perms[i][j]].get_center() - 0.33 * (
                        permed[i][inv_perms[i][j]].get_center() - transforms[i][j].get_center()) / np.linalg.norm(
                (permed[i][inv_perms[i][j]].get_center() - transforms[i][j].get_center())),
        ).add_tip(tip_length=0.15) for i in range(6) for j in range(3)]

        self.remove(vg)

        self.play(
            *[ReplacementTransform(mobject=vg.copy(), target_mobject=obj) for obj in transforms],
        )

        self.wait(2)

        self.play(
            *[ReplacementTransform(mobject=transforms[i].copy(), target_mobject=translated[i]) for i in range(6)],
            *[Create(arrow) for arrow in shifted_arrows]
        )

        self.wait(2)

        labels = [MathTex(str(i)).scale(0.75) for i in range(1, 4)]

        top_label_groups = []
        for i in range(6):
            new_group = VGroup()
            top_label_groups.append(new_group)
            for j in range(3):
                new_label = labels[j].copy().move_to(
                    transforms[i][j].get_center()
                )
                new_group.add(new_label)

        bottom_label_groups = []
        for i in range(6):
            new_group = VGroup()
            bottom_label_groups.append(new_group)
            for j in range(3):
                new_label = labels[j].copy().move_to(
                    translated[i][j].get_center()
                )
                new_group.add(new_label)

        self.play(
            *[Write(top_label_groups[i], lag_ratio=0.5, run_time=1) for i in range(6)]
        )

        self.play(
            *[Write(bottom_label_groups[i], lag_ratio=0.5, run_time=1) for i in range(6)]
        )

        self.wait(2)

        ref_translated = deepcopy(translated)
        ref_labels = deepcopy(bottom_label_groups)
        self.play(
            *[translated[i][j].animate.move_to(ref_translated[i][perms[i][j]]) for i in range(6) for j in range(3)],
            *[bottom_label_groups[i][j].animate.move_to(ref_labels[i][perms[i][j]]) for i in range(6) for j in range(3)]
        )

        self.wait(2)

        self.play(
            *[FadeOut(obj) for obj in [*transforms, *translated]],
            *[FadeOut(obj) for obj in shifted_arrows]
        )

        reindex_perms = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        recomb_labels = [VGroup(top_label_groups[i], bottom_label_groups[i]) for i in range(6)]
        matrices = [
            Matrix([[1, 2, 3], reindex_perms[i]], h_buff=1).move_to(recomb_labels[i].get_center())
            for i in range(6)
        ]
        to_matrix_anims = []
        for i in range(6):
            new = recomb_labels[i].copy()
            for j in range(2):
                for k in range(3):
                    new[j][k].scale(1 / 0.75)
                new[j].move_to(matrices[i].get_rows()[j].get_center())
            to_matrix_anims.append(new)

        self.play(
            *[ReplacementTransform(mobject=recomb_labels[i][j], target_mobject=to_matrix_anims[i][j]) for i in range(6) for j in range(2)],
            *[Write(matrix.get_brackets()) for matrix in matrices]
        )

        self.wait(2)


class ArrayNotationMappingPositions(Scene):
    def construct(self):
        r = 0.5
        vg1 = VGroup()
        michael = Circle(radius=r, color='#0000FF', fill_color='#0000FF', fill_opacity=0.75)
        pramod = Circle(radius=r, color='#FF0000', fill_color='#FF0000', fill_opacity=0.75)
        will = Circle(radius=r, color='#FFFF00', fill_color='#FFFF00', fill_opacity=0.75)
        michael.move_to(array([-2, 0, 0]))
        will.move_to(array([2, 0, 0]))

        vg1.add(michael, pramod, will)

        r_diff = 0.1

        vg3 = VGroup()
        michael = Circle(radius=r - r_diff, color='#0000FF', fill_color='#0000FF', fill_opacity=0.75)
        pramod = Circle(radius=r - r_diff, color='#FF0000', fill_color='#FF0000', fill_opacity=0.75)
        will = Circle(radius=r - r_diff, color='#FFFF00', fill_color='#FFFF00', fill_opacity=0.75)
        michael.move_to(array([-2, 0, 0]))
        will.move_to(array([2, 0, 0]))

        vg3.add(michael, pramod, will)

        vg2 = VGroup()
        michael = VGroup(
            # Circle(radius=r - r_diff, color='#0000FF', fill_color='#0000FF', fill_opacity=0.75),
            Circle(radius=r + r_diff, color='#FFFFFF')
        )
        pramod = VGroup(
            # Circle(radius=r - r_diff, color='#FF0000', fill_color='#FF0000', fill_opacity=0.75),
            Circle(radius=r + r_diff, color='#FFFFFF')
        )
        will = VGroup(
            # Circle(radius=r - r_diff, color='#FFFF00', fill_color='#FFFF00', fill_opacity=0.75),
            Circle(radius=r + r_diff, color='#FFFFFF')
        )
        michael.move_to(array([-2, 0, 0]))
        will.move_to(array([2, 0, 0]))

        vg2.add(michael, pramod, will)

        transforms = []
        horiz_spread = 4
        vert_spread = 4
        vert_shift = 0.75

        for j in reversed(range(2)):
            for i in range(3):
                new = vg2.copy().scale(0.5)
                new.move_to(array([(i-1)*horiz_spread, (j-0.5)*vert_spread + vert_shift, 0]))
                transforms.append(new)


        self.play(
            Create(vg1)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(mobject=vg1, target_mobject=vg2)
        )

        self.play(
            Create(vg3)
        )

        self.wait(2)

        perms = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        inv_perms = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [2, 0, 1], [1, 2, 0], [2, 1, 0]]
        translated = []
        for i in range(6):
            # pos = {j: transforms[i][perms[i][j]].get_center() for j in range(3)}
            pos = {j: transforms[i][j].get_center() for j in range(3)}
            new_group = transforms[i].copy()
            for n in range(3):
                new_group[n].move_to(pos[n])
                new_group[n].shift(array([0, -1.5, 0]))
            translated.append(new_group)

        elements = []
        for j in reversed(range(2)):
            for i in range(3):
                new = vg3.copy().scale(0.5)
                new.move_to(array([(i-1)*horiz_spread, (j-0.5)*vert_spread + vert_shift, 0]))
                elements.append(new)

        permed = []
        for i in range(6):
            pos = {j: elements[i][perms[i][j]].get_center() for j in range(3)}
            new_group = elements[i].copy()
            for n in range(3):
                new_group[n].move_to(pos[n])
                new_group[n].shift(array([0, -1.5, 0]))
            permed.append(new_group)

        arrows = [Line(
                        start=elements[i][j].get_center() + 0.36 * (permed[i][j].get_center() - elements[i][j].get_center()) / np.linalg.norm((permed[i][j].get_center() - elements[i][j].get_center())),
                        end=permed[i][j].get_center() - 0.36 * (permed[i][j].get_center() - elements[i][j].get_center()) / np.linalg.norm((permed[i][j].get_center() - elements[i][j].get_center())),
        ).add_tip(tip_length=0.15) for i in range(6) for j in range(3)]

        shifted_arrows = [Line(
            start=elements[i][j].get_center() + 0.36 * (
                        permed[i][inv_perms[i][j]].get_center() - elements[i][j].get_center()) / np.linalg.norm(
                (permed[i][inv_perms[i][j]].get_center() - elements[i][j].get_center())),
            end=permed[i][inv_perms[i][j]].get_center() - 0.36 * (
                        permed[i][inv_perms[i][j]].get_center() - elements[i][j].get_center()) / np.linalg.norm(
                (permed[i][inv_perms[i][j]].get_center() - elements[i][j].get_center())),
        ).add_tip(tip_length=0.15) for i in range(6) for j in range(3)]

        translate_anims = [ReplacementTransform(mobject=transforms[i].copy(), target_mobject=translated[i], run_time=0.5) for i in range(6)]
        arrow_anims = [Create(arrow) for arrow in arrows]
        perm_anims = [ReplacementTransform(mobject=elements[i].copy(), target_mobject=permed[i], run_time=0.5) for i in range(6)]
        # perm_anims = [ReplacementTransform(mobject=elements[i][j].copy(), target_mobject=permed[i][j], run_time=0.5) for i in range(6)]

        self.remove(vg2)
        self.remove(vg3)

        self.play(
            *[ReplacementTransform(mobject=vg2.copy(), target_mobject=obj) for obj in transforms],
            *[ReplacementTransform(mobject=vg3.copy(), target_mobject=element) for element in elements]
        )

        self.wait(2)

        self.play(*translate_anims)

        self.wait(2)

        for i in range(6):
            self.play(*arrow_anims[i*3 : (i+1)*3], perm_anims[i])
            self.wait(0.2)

        self.wait(2)

        labels = [MathTex(str(i)).scale(0.75) for i in range(1, 4)]

        top_label_groups = []
        for i in range(6):
            new_group = VGroup()
            top_label_groups.append(new_group)
            for j in range(3):
                new_label = labels[j].copy().move_to(
                    transforms[i][j].get_center() + array([0, 0.5, 0])
                )
                new_group.add(new_label)

        bottom_label_groups = []
        for i in range(6):
            new_group = VGroup()
            bottom_label_groups.append(new_group)
            for j in range(3):
                new_label = labels[j].copy().move_to(
                    translated[i][j].get_center() + array([0, -0.5, 0])
                )
                new_group.add(new_label)

        self.play(
            *[Write(top_label_groups[i], lag_ratio=0.5, run_time=1) for i in range(6)]
        )

        self.play(
            *[Write(bottom_label_groups[i], lag_ratio=0.5, run_time=1) for i in range(6)]
        )

        self.wait(2)

        self.play(
            *[Uncreate(obj) for obj in [*permed, *elements]]
        )

        self.wait(2)

        ref_translated = deepcopy(translated)
        ref_labels = deepcopy(bottom_label_groups)
        self.play(
            *[ReplacementTransform(mobject=arrows[i], target_mobject=shifted_arrows[i]) for i in range(len(arrows))],
            *[translated[i][j].animate.move_to(ref_translated[i][inv_perms[i][j]].get_center()) for i in range(6) for j in range(3)],
            *[bottom_label_groups[i][j].animate.move_to(ref_labels[i][inv_perms[i][j]].get_center()) for i in range(6) for j in range(3)]
        )

        self.wait(2)

        self.play(
            *[FadeOut(obj) for obj in [*transforms, *translated]],
            *[FadeOut(obj) for obj in shifted_arrows]
        )

        reindex_perms = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        recomb_labels = [VGroup(top_label_groups[i], bottom_label_groups[i]) for i in range(6)]
        matrices = [
            Matrix([[1, 2, 3], reindex_perms[i]], h_buff=1).move_to(recomb_labels[i].get_center())
            for i in range(6)
        ]
        to_matrix_anims = []
        for i in range(6):
            new = recomb_labels[i].copy()
            for j in range(2):
                for k in range(3):
                    new[j][k].scale(1/0.75)
                new[j].move_to(matrices[i].get_rows()[j].get_center())
            to_matrix_anims.append(new)

        self.play(
            *[ReplacementTransform(mobject=recomb_labels[i][j], target_mobject=to_matrix_anims[i][j]) for i in range(6) for j in range(2)],
            *[Write(matrix.get_brackets()) for matrix in matrices]
        )

        self.wait(2)