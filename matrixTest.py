from manim import *


class Video1(Scene):
    def construct(self):
        config.tex_template = TexTemplate(compiler="cairo")

       # equations = VGroup(
       #     Tex(r"$a_{11}x_1 + a_{12}x_2 +  a_{1m}x_m = b_1$"),
        #    Tex(r"$a_{21}x_1 + a_{22}x_2 +  a_{2m}x_m = b_2$"),
       #     Tex(r"$a_{n1}x_1 + a_{n2}x_2 +  a_{nm}x_m = b_n$"),
        #).scale(0.7)
        #equations.arrange(DOWN)

        Name_M = Tex("A=").to_corner(LEFT)
        test_M = MobjectMatrix(
            [[MathTex("a_{11}"), MathTex("a_{12}"), MathTex("a_{13}")],
             [MathTex("a_{21}"), MathTex("a_{22}"), MathTex("a_{23}")],
             [MathTex("a_{31}"), MathTex("a_{32}"), MathTex("a_{33}")]]).next_to(Name_M)
        test_Copy = test_M.copy()

        #Transponierte Matrix

        t11 = test_M[0][0]
        t12 = test_M[0][3]
        t13 = test_M[0][6]

        t21 = test_M[0][1]
        t22 = test_M[0][4]
        t23 = test_M[0][7]

        t31 = test_M[0][2]
        t32 = test_M[0][5]
        t33 = test_M[0][8]



        column1 = VGroup(test_M[0][0],test_M[0][1],test_M[0][2])
       # column2 = VGroup(test_M[1][0], test_M[1][1], test_M[1][2])
        #column2 = VGroup(test_M[2][0], test_M[2][1], test_M[2][2])

        row1 = VGroup(test_M[0][0],test_M[1][0],test_M[2][0])
       # row2 = VGroup(test_M[0][1], test_M[1][1], test_M[2][1])
        #row3 = VGroup(test_M[0][2], test_M[1][2], test_M[2][2])






        #colum2 = VGroup(())




        #M_copy=VGroup(*VGroup(*test_M)[0]).copy()
        #test_P = MobjectMatrix([]).scale(5)
        #test_P = MobjectMatrix([((),(),()),
                              #  ((), (), ()),
                              #  ((), (), ())])
        left_bracket = Tex(r"\left[").scale(3).stretch_to_fit_height(4).shift(RIGHT * 0.8)
        right_bracket = Tex(r"\right]").scale(3).stretch_to_fit_height(4).shift(RIGHT * 7.5)

        matrix_outline = VGroup(left_bracket, right_bracket).scale(0.6)

        matrix_outline.to_corner(RIGHT)
        Name_MO = MathTex("A^{T} =").next_to(matrix_outline, LEFT)

        self.play(Write(test_Copy),Write(test_M), Write(Name_M), run_time = 4)
        self.play(test_M.animate.set_column_colors(RED,GREEN,BLUE), run_tim = 2)

        #test_M.set_column_colors(RED,GREEN,BLUE)
        self.play(Write(matrix_outline), Write(Name_MO), run_time=2)
        self.play(t11.animate.scale(1).to_corner(RIGHT*7.5),
                  t12.animate.scale(1).to_corner(RIGHT * 4.5).shift(UP*0.8),
                  t13.animate.scale(1).to_corner(RIGHT * 1.5).shift(UP*1.6)
                  )

        self.wait(3)
        self.play(t21.animate.scale(1).to_corner(RIGHT*7.5).shift(DOWN*0.8),
                  t22.animate.scale(1).to_corner(RIGHT * 4.5),
                  t23.animate.scale(1).to_corner(RIGHT * 1.5).shift(UP*0.8)
                  )

        self.wait(3)

        self.play(t31.animate.scale(1).to_corner(RIGHT*7.5).shift(DOWN*1.6),
                  t32.animate.scale(1).to_corner(RIGHT * 4.5).shift(DOWN*0.8),
                  t33.animate.scale(1).to_corner(RIGHT * 1.5)
                  )

        self.wait(3)