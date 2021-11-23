import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')


st.set_page_config(page_title='Vector Norms', layout="wide")

_, row_one, _ = st.columns([15, 20, 0.5])

row_one.title("VECTOR NORMS")

_, row_two_col2, row_two_col3 = st.columns([1, 5, 10])

row_two_col2.header("Distances and norms")
row_two_col2.write(r'''
Norm is a ** qualitative measure of smallness of a vector ** and is typically denoted as $\Vert x \Vert$.

The norm should satisfy certain properties:

- $\Vert \alpha x \Vert = |\alpha | \Vert x \Vert$,
- $\Vert x + y \Vert \leq \Vert x \Vert + \Vert y \Vert$ (triangle inequality),
- If $\Vert x \Vert = 0$ then $x = 0$.

The distance between two vectors is then defined as
$$
d(x, y) = \Vert x - y \Vert.
$$
''')

row_two_col3.image('norm_distance.jpeg', use_column_width='always')

row_three_col_1, _, row_three_col_3 = st.columns([3, 0.1, 2])

row_three_col_1.header(r'''$p$-norm''')

row_three_col_1.write(r'''
The $p$- norms is a general class of vector norm and defined as:
$$
\Vert x \Vert_p = \Big(\sum_{i=1} ^ n | x_i | ^p\Big) ^ {1/p}.
$$
it has two very important special cases:
- Infinity norm, or Chebyshev norm which is defined as the maximal element: $\Vert x \Vert_{\infty} = \max_i | x_i|$
- $L_1$ norm ( or **Manhattan distance**) which is defined as the sum of modules of the elements of $x$: $\Vert x \Vert_1 = \sum_i | x_i|$
''')

row_three_col_3.header("Standard norm")

row_three_col_3.write(r'''
         **Euclidean norm**, or **$2$- norm**, is a subclass of the $p$-norms widely known and used:
         $$
         \Vert x \Vert_2= \sqrt{\sum_{i=1} ^ n | x_i | ^2},
         $$
         this corresponds to the distance in our real life (the vectors might have complex elements, thus is the modulus here).
         ''')

# p = np.inf  # , 0.04, 0.5, 1, 1.5, 2, 7, np.inf]
# xx, yy = np.meshgrid(np.linspace(-3, 3, num=101), np.linspace(-3, 3, num=101))
# zz = np.c_[xx.ravel(), yy.ravel()]
# norms = np.linalg.norm(zz, ord=p, axis=1)
# norms = norms.reshape(xx.shape)
# fig = plt.figure(figsize=(5, 5))
# plt.contourf(xx, yy, norms, levels=np.linspace(
#     0, norms.max(), 20), cmap=plt.cm.RdBu_r)
# b = plt.contour(xx, yy, norms, levels=[1], linewidths=2, colors='darkred')
# plt.legend(b.collections, [f'$\{{x: \mid x\mid_{p} =1\}}$'])


p_values = [0., 0.04, 0.5, 1, 1.5, 2, 7, np.inf]
xx, yy = np.meshgrid(np.linspace(-3, 3, num=101), np.linspace(-3, 3, num=101))

# fig, axes = plt.subplots(ncols=(len(p_values) + 1) //
#                          2, nrows=2, figsize=(14, 7))
zz = np.c_[xx.ravel(), yy.ravel()]
# for p, ax in zip(p_values, axes.flat):
#     norms = np.linalg.norm(zz, ord=p, axis=1)
#     norms = norms.reshape(xx.shape)
#     ax.contourf(xx, yy, norms, levels=np.linspace(
#         0, norms.max(), 20), cmap=plt.cm.RdBu_r)
#     a = ax.contour(xx, yy, norms, levels=[1], linewidths=2, colors='darkred')
#     ax.legend(a.collections, ['$\{{x: \mid x\mid_{} =1\}}$'.format({p})])

#st.select_slider("p", options=p_values)

col = st.columns(4)

for p in range(len(p_values)):
    with col[p % 4]:
        norms = np.linalg.norm(zz, ord=p_values[p], axis=1)
        norms = norms.reshape(xx.shape)
        fig = plt.figure()
        plt.contourf(xx, yy, norms, levels=np.linspace(
            0, norms.max(), 20), cmap=plt.cm.RdBu_r)
        b = plt.contour(xx, yy, norms, levels=[
                        1], linewidths=2, colors='darkred')
        plt.legend(b.collections, [
                   '$\{{x: \mid x\mid_{} =1\}}$'.format({p_values[p]})])
        st.pyplot(fig=fig)


# footer = "<style > your css code put here < /style ><div class = 'footer' ><p > the word you want to tell < a style = 'display:block;text-align:center;'href = 'https://www.streamlit.io' target = '_blank' > your email address put here < /a > </p ></div >"

# st.markdown(footer, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
            content:'Made with Streamlit by Usman'; 
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
