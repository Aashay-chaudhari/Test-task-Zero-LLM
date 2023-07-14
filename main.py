import streamlit as st
from helper import get_columns, get_temp_columns, get_replace_cols
import pandas as pd

st.title("Upload CSV files")

template = st.file_uploader("upload template file", type={"csv", "txt"})
if template is not None:
    template_df = pd.read_csv(template)
    st.write(template_df)
    template_cols = get_temp_columns(template_df)
    print("template_cols are: ", template_cols)

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    st.write(spectra_df)

if "Map Columns" not in st.session_state:
    st.session_state["Map Columns"] = False

if "Transform" not in st.session_state:
    st.session_state["Transform"] = False


if st.button("Map Columns"):
    columns = get_columns(spectra_df, template_cols)
    print("columns: ", columns)
    st.write(columns)
    st.session_state["Map Columns"] = not st.session_state["Map Columns"]

if st.session_state["Map Columns"]:
    if st.button("Transform"):
        print("Inside proceed")
        new_cols = get_replace_cols(spectra_df, template_cols)
        spectra_df = spectra_df[eval(new_cols)]
        spectra_df = spectra_df.rename(columns=dict(zip(spectra_df.columns, eval(template_cols))))
        st.write(spectra_df)
        st.session_state["Transform"] = not st.session_state["Transform"]

