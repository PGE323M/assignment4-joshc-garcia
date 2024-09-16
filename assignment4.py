#!/usr/bin/env python
# coding: utf-8

# ## Assignment 4
# 
# Consider the domain shown in the figure below which has $N_x$ grids in the $x$-direction and $N_y$ grids in the $y$-direction, or a total of $N = N_x \times N_y$ grids. The grids are numbered from $k = 0$ to $k = N - 1$, starting ($k = 0$) from the bottom-left corner and finishing ($k = N - 1$) at the top-right corner. Grids are considered connected if they are neighbors, i.e. adjacent to each other. In general $N_x$ does not equal to $N_y$ (although they could be equal).
# 
# 
# <table border="1">
#   <tr style="border: 1px solid black">
#     <td style="border: 1px solid black">8</td>
#     <td style="border: 1px solid black">9</td>
#     <td style="border: 1px solid black">10</td>
#     <td style="border: 1px solid black">11</td>
#   </tr>
#   <tr style="border: 1px solid black">
#     <td style="border: 1px solid black">4</td>
#     <td style="border: 1px solid black">5</td>
#     <td style="border: 1px solid black">6</td>
#     <td style="border: 1px solid black">7
#     </td>
#   </tr>
#   <tr style="border: 1px solid black">
#     <td style="border: 1px solid black">0</td>
#     <td style="border: 1px solid black">1</td>
#     <td style="border: 1px solid black">2</td>
#     <td style="border: 1px solid black">3</td>
#   </tr>
# </table>
# 
# 
# For example in the figure, $N_x=4$ and $N_y=3$ (therefore $N=12$). Grid $k=5$ has $4$ neighbors: $k = 4$ (left), $k = 6$ (right), $k = 1$ (bottom), and $k = 9$ (top). In fact, all interior grids have 4 neighbors. However, grids on the edges have only 2 or 3 neighbors. For example, grid $k = 3$ is only neighbors with $k = 2$ (left) and $k = 7$ (top). It has no neighbor to the right ($k = 4$ is NOT its neighbor) or bottom.
# 
# In reservoir simulation, we often use similar grid systems to solve for pressures, saturations, etc. in the reservoir. To do so we map the grid onto an $N \times N$ matrix (called $\mathbf{A}$), where each $k$ grid represents a row in the matrix. Most of the elements of the matrix are zero (so it is a *sparse* matrix). But an element of the matrix is equal to $-1$ if the matrix row and column for that element are neighbors in the original grid system. For the main diagonal terms (i.e. row $k$, column $k$), it is equal to the total number of neighbors grid $k$ has.
# 
# For the matrix system
# 
# $$
# \mathbf{A} = \left(
# \begin{matrix}
#  2 & -1 &    &    & -1 &    &    &    &    &    &    &        \\
# -1 &  3 & -1 &    &    & -1 &    &    &    &    &    &        \\
#    & -1 &  3 & -1 &    &    & -1 &    &    &    &    &        \\
#    &    & -1 &  2 &    &    &    & -1 &    &    &    &        \\
# -1 &    &    &    &  3 & -1 &    &    & -1 &    &    &        \\
#    & -1 &    &    & -1 &  4 & -1 &    &    & -1 &    &        \\
#    &    & -1 &    &    & -1 &  4 & -1 &    &    & -1 &        \\
#    &    &    & -1 &    &    & -1 &  3 &    &    &    & -1     \\
#    &    &    &    & -1 &    &    &    &  2 & -1 &    &        \\
#    &    &    &    &    & -1 &    &    & -1 &  3 & -1 &        \\
#    &    &    &    &    &    & -1 &    &    & -1 &  3 & -1     \\
#    &    &    &    &    &    &    & -1 &    &    & -1 &  2 
# \end{matrix}
# \right)
# $$
# 
# 
# 
# consider gridblock $5$, which is neighbor to gridblocks 4, 6, 1 and 9. In the corresponding matrix $\mathbf{A}$, $A_{5 4}=A_{5 6}=A_{5 1}=A_{5 9}= -1$. $A_{5 5} = 4$ because gridblock 5 has 4 neighbors. Likewise, $A_{3 2} = A_{3 7} = -1$, but $A_{3 4} = 0$ since grids 3 and 4 are not neighbors. $A_{3 3} = 2$ because grid 3 has 2 neighbors... Doing this for all $k = 0$ to $k = N-1$ grids, results in a **pentadiagonal** matrix.
# 
# The matrix $\mathbf{A}$ is an $N \times N$ matrix. The matrix is pentadiagonal because there are 5 (penta) diagonal bands. Sometimes the number of columns separating the leftmost and rightmost bands is called the bandwith. There are 5 bands because a grid has at most 4 neighbors + its self (main diagonal).
# 
# ## Problem 1
# 
# Complete the function to create the pentadiagonal matrix ($\mathbf A$) described above when given $N_x$ and $N_y$ as inputs. The matrix should be of size $N \times N$, where $N = N_x \times N_y$.

# In[1]:


def pentadiagonal(Nx, Ny):
    # some pseudocode has been added to guide you, 
    # but feel free to ignore if you have an alternate way.

    ## Begin by initializing the matrix (A) with N rows and N columns of zeros. N = Nx * Ny
    A = [[0 for i in range(Nx*Ny)] for i in range(Nx*Ny)]

    ## Next, loop through each gridblock in the grid
    for i in range(Nx*Ny):
        x = i % Nx
        y = i // Nx
        ## if i is not on bottom edge of grid
            ##insert code here to populate matrix
        if y > 0:
            bottom_neighbor = i - Nx
            A[i][bottom_neighbor] = -1
        ## if i is not on top edge of grid
            ##insert code here to populate matrix
        if y < Ny - 1:
            top_neighbor = i + Nx
            A[i][top_neighbor] = -1
        ## if i is not on left edge of grid
            ##insert code here to populate matrix
        if x > 0:
            left_neighbor = i - 1
            A[i][left_neighbor] = -1
        ## if i is not on right edge of grid
            ##insert code here to populate matrix
        if x < Nx - 1:
            right_neighbor = i + 1
            A[i][right_neighbor] = -1
        ## insert code here to fill in the diagonal of 
        ## the matrix by getting the absolute value of the sum of off-diagonals.
        A[i][i] = abs(sum(A[i]))

    return A

