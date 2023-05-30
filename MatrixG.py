from manim import *

class MatrixExample(Scene):
    def construct(self):
        # Define the matrix elements
        matrix_elements = [
            ["a_{11}",  "a_{12}", "\\dots", "a_{1m}" ],
            ["a_{21}", "a_{22}", "\\dots", "a_{2m}"],
            ["\\vdots", "\\vdots", "\\ddots", "\\vdots"],
            ["a_{n1}", "a_{n2}", "\\dots", "a_{nm}"],
        ]

        # Create the matrix as a VGroup
        matrix = VGroup(*[
            MathTex(element) for row in matrix_elements for element in row
        ])

        # Position the matrix elements
        matrix.arrange_in_grid(buff=0.7)


        # Create left and right brackets
        left_bracket = Tex(r"\left[").scale(4).stretch_to_fit_height(4)
        right_bracket = Tex(r"\right]").scale(4).stretch_to_fit_height(4)
        left_bracket.next_to(matrix, LEFT)
        right_bracket.next_to(matrix, RIGHT)

        matrixBrack = VGroup(matrix, right_bracket, left_bracket)

        # Give a name
        NameA = MathTex("A =").next_to(matrixBrack, LEFT)

        # Add the matrix to the scene
        self.play(Create(matrixBrack), run_time = 6)
        self.play(Create(NameA), run_time = 2)
        self.wait(2)

        #Beschriftung

        N_Brace = Brace(matrixBrack, RIGHT)
        N_Brace_Text = Tex(r"n Zeilen", color=ORANGE).next_to(N_Brace,RIGHT)

        M_Brace = Brace(matrixBrack, DOWN)
        M_Brace_Text = Tex(r"m Spalten", color=ORANGE).next_to(M_Brace,DOWN)

        self.play(
            Write(N_Brace),
            Write(N_Brace_Text),
            Write(M_Brace),
            Write(M_Brace_Text),
            run_time=2
        )
        self.wait(2)

        matrixBrackBrace = VGroup(NameA,matrixBrack,M_Brace,M_Brace_Text,N_Brace,N_Brace_Text)

        self.play(matrixBrackBrace.animate.shift(LEFT*3).scale(0.7))
        self.wait(2)

        #Define Vector
        vector_elements = [
            ["y_{11}"],
            ["y_{21}"],
            ["\\vdots"],
            ["y_{n1}"],
        ]

        ve = [
            MathTex(element) for row in vector_elements for element in row
        ]

        # Create a VGroup and position the vector elements
        vector = VGroup(*ve)
        vector.arrange(DOWN, buff=0.7)
        # Position the vector
        #vector.to_corner(RIGHT).scale(0.7)
        left_bracket1 = Tex(r"\left(").scale(2).stretch_to_fit_height(3)
        right_bracket1 = Tex(r"\right)").scale(2).stretch_to_fit_height(3)
        left_bracket1.next_to(vector, LEFT)
        right_bracket1.next_to(vector, RIGHT)

        NameY = MathTex("\\vec{v} =").next_to(left_bracket1, LEFT)


        #again
        equal = MathTex("=").next_to(right_bracket1, RIGHT)
        vector_elements1 = [
            ["y_{1}"],
            ["y_{2}"],
            ["\\vdots"],
            ["y_{n}"],
        ]


        left_bracket2 = Tex(r"\left(").scale(2).stretch_to_fit_height(3)
        right_bracket2 = Tex(r"\right)").scale(2).stretch_to_fit_height(3)
        left_bracket2.next_to(equal, RIGHT)
        vector1 = VGroup(*[
            MathTex(element) for row in vector_elements1 for element in row
        ]).arrange(DOWN, buff=0.7).next_to(left_bracket2,RIGHT)
        right_bracket2.next_to(vector1, RIGHT)


        #Position
        Whole_vector = VGroup(vector,NameY,left_bracket1,right_bracket1,vector1,left_bracket2,right_bracket2,equal).to_corner(RIGHT).scale(0.7)

        self.play(Create(vector),Write(left_bracket1), Write(right_bracket1),Write(NameY),run_time=3)
        self.wait(2)

        Y_Brace = Brace(vector, DOWN)
        Y_Brace_Text = Tex(r"Eine Spalte!", color=ORANGE).next_to(Y_Brace,DOWN)
        self.play(Write(Y_Brace),Create(Y_Brace_Text),run_time=2)
        self.wait(1)

        self.play(Write(equal),Create(vector1),Write(left_bracket2),Write(right_bracket2),run_time=2)
        self.wait(2)









