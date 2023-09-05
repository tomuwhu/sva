import streamlit as st
import pandas as pd
import numpy as np
import cmath

fb = 51
x = st.slider("Kitevő", min_value=0.0, max_value=5.0, value=0.0, step=0.01)
n = complex(x, 0)

"""
$$f(x) = x^{%s}$$
""" % round(
    x, 2
)

lr = list(
    map(
        lambda x: (complex(x[0] - ((fb - 1) // 2), 0) ** n).real,
        enumerate([0] * fb),
    )
)

lc = list(
    map(
        lambda x: (complex(x[0] - ((fb - 1) // 2), 0) ** n).imag,
        enumerate([0] * fb),
    )
)

k = list(map(lambda x: x[0] - (fb - 1) / 2, enumerate([0] * fb)))

chart_data = pd.DataFrame({"x": k, "real": lr, "imag": lc})

st.line_chart(chart_data, x="x", y=["imag", "real"])
