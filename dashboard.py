import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Vector Norms', layout="wide")

page = st.sidebar.selectbox('Vector Norm', ['Introduction', 'Experiment'])

_, row_one, _ = st.columns([15, 20, 0.5])

row_one.title("VECTOR NORMS")

if page == 'Introduction':

    _, row_two_col2, row_two_col3 = st.columns([1, 5, 10])

    row_two_col2.write("#")
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

    row_two_col3.write("#")
    row_two_col3.write("#")
    # row_two_col3.write("#")
    # row_two_col3.write("#")
    row_two_col3.image('norm_resized.png')
    row_two_col3.write(
        'Distance measures. (credit [Alex wang](https://www.linkedin.com/posts/mengyaowang11_artificialintelligence-machinelearning-datascience-activity-6868501725100302337-lu1p))')

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

else:
    st.subheader('Level set of $l^p$ norm')
    p_values = [0., 0.04, 0.5, 1, 1.5, 2, 7, np.inf]
    xx, yy = np.meshgrid(np.linspace(-3, 3, num=101),
                         np.linspace(-3, 3, num=101))
    zz = np.c_[xx.ravel(), yy.ravel()]

    row_one_col = st.columns(4)
    for p in range(len(p_values)):
        with row_one_col[p % 4]:
            norms = np.linalg.norm(zz, ord=p_values[p], axis=1)
            norms = norms.reshape(xx.shape)
            fig = plt.figure()
            plt.contourf(xx, yy, norms, levels=np.linspace(
                0, norms.max(), 20), cmap=plt.cm.RdBu_r)
            b = plt.contour(xx, yy, norms, levels=[
                            1], linewidths=2, colors='darkred')
            #plt.title('Level sets of the $l^p$ norm')
            plt.legend(b.collections, [
                '$\{{x: \mid x\mid_{} =1\}}$'.format({p_values[p]})], fontsize=15)
            st.pyplot(fig=fig)

    st.title('#')
    st.title('#')
    row_two_col = st.columns(2)

    with row_two_col[0]:
        st.subheader('Try it out')
        P = st.slider('p', min_value=0, max_value=50, value=0)
        norms = np.linalg.norm(zz, ord=P, axis=1)
        norms = norms.reshape(xx.shape)
        fig = plt.figure()
        plt.contourf(xx, yy, norms, levels=np.linspace(
            0, norms.max(), 20), cmap=plt.cm.RdBu_r)
        b = plt.contour(xx, yy, norms, levels=[
            1], linewidths=2, colors='darkred')
        #plt.title('Level sets of the $l^p$ norm')
        plt.legend(b.collections, [
            '$\{{x: \mid x\mid_{} =1\}}$'.format({P})], fontsize=15)
        st.pyplot(fig=fig)

    with row_two_col[1]:
        st.subheader('Explore other values ($0 \leq p \leq 645$)')
        p = st.number_input('p', min_value=0.0,
                            max_value=645.0, value=0.0)
        norms = np.linalg.norm(zz, ord=p, axis=1)
        norms = norms.reshape(xx.shape)
        fig = plt.figure()
        plt.contourf(xx, yy, norms, levels=np.linspace(
            0, norms.max(), 20), cmap=plt.cm.RdBu_r)
        b = plt.contour(xx, yy, norms, levels=[
            1], linewidths=2, colors='darkred')
        #plt.title('Level sets of the $l^p$ norm')
        plt.legend(b.collections, [
            '$\{{x: \mid x\mid_{} =1\}}$'.format({p})], fontsize=15)
        st.pyplot(fig=fig)


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
