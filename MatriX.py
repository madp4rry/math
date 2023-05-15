TestCodeHere
from manim import *

class Transfo(Scene):
    def construct(self):
        
        equations = Tex(r"""
            $\begin{aligned}
                x_1 - 2x_2 + x_3 = 2 \\
                3x_1 + x_2 - x_3 = 1 \\
                2x_1 - 3x_2 + 2x_3 = 3
            \end{aligned}$
        """, height=1.25, width=4.5).shift(LEFT*3)
    

        Matrix1= Tex(r"""
        \[
        \left[
        \begin{array}{ccc|c}
         1 & -2 & 1 & 2 \\
         3 & 1 & -1 & 1 \\
         2 & -3 & 2 & 3 \\
        \end{array}
        \right]
        \]""").shift(RIGHT*3)

        self.play(Create(equations), run_time=3)
        self.wait(3)
        self.play(TransformFromCopy(equations, Matrix1), run_time=1.5)
        self.wait(3)

