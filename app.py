import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Quality Stat",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------------------------------------------------
       GLOBAL
    --------------------------------------------------- */

    .main {
        padding-top: 1.5rem;
    }

    h1 {
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    h2 {
        font-weight: 650;
    }

    h3 {
        font-weight: 600;
    }


    /* ---------------------------------------------------
       SIDEBAR
    --------------------------------------------------- */

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.2);
    }

    section[data-testid="stSidebar"] h1 {
        font-size: 1.25rem;
    }


    /* ---------------------------------------------------
       METRIC CARDS
    --------------------------------------------------- */

    div[data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.06);
        border: 1px solid rgba(128, 128, 128, 0.18);
        padding: 14px;
        border-radius: 10px;
    }


    /* ---------------------------------------------------
       BUTTONS
    --------------------------------------------------- */

    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        min-height: 42px;
    }


    /* ---------------------------------------------------
       INFO / SUCCESS / WARNING BOXES
    --------------------------------------------------- */

    div[data-testid="stAlert"] {
        border-radius: 8px;
    }


    /* ---------------------------------------------------
       DATAFRAME
    --------------------------------------------------- */

    div[data-testid="stDataFrame"] {
        border-radius: 8px;
        overflow: hidden;
    }


    /* ---------------------------------------------------
       FOOTER
    --------------------------------------------------- */

    .qe-footer {
        text-align: center;
        color: #777;
        font-size: 0.85rem;
        padding: 1rem 0 0.5rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HOME PAGE
# =========================================================

st.title("📊 Quality Engineering Toolkit")

st.subheader(
    "Practical Statistical & Quality Engineering Tools"
)

st.write(
    """
    A practical toolkit for engineers working with
    manufacturing quality, process capability, SPC,
    and statistical analysis.
    """)


st.divider()


# =========================================================
# WHAT IS THIS WEBSITE?
# =========================================================

st.header("What is this website?")

st.write(
    """
    The Quality Engineering Toolkit is being developed as
    a collection of practical engineering tools that help
    convert quality data into meaningful engineering
    information.
    """
)

st.write(
    """
    The first module focuses on **Process Capability**,
    starting with Cp and Cpk analysis.
    """
)


# =========================================================
# CURRENT TOOLS
# =========================================================

st.header("Available Tools")

tool_col1, tool_col2 = st.columns(2)


with tool_col1:

    with st.container(border=True):

        st.subheader("📊 Cp / Cpk Calculator")

        st.write(
            """
            Analyze process capability using measurement
            data and specification limits.
            """
        )

        st.markdown(
            """
            **Includes**

            • Cp and Cpk  
            • Cpu and Cpl  
            • Process mean and variation  
            • Capability assessment  
            • Engineering interpretation  
            • Process capability histogram
            """
        )


with tool_col2:

    with st.container(border=True):

        st.subheader("📘 Cp / Cpk Theory")

        st.write(
            """
            Understand the theory behind process capability
            and learn how variation and centering influence
            Cp and Cpk.
            """
        )

        st.markdown(
            """
            **Topics**

            • Process capability  
            • Specification limits  
            • Process variation  
            • Cp and Cpk  
            • Cpu and Cpl  
            • Process centering  
            • Worked examples
            """
        )


# =========================================================
# COMING NEXT
# =========================================================

st.divider()

st.header("Coming Next")

next_col1, next_col2, next_col3 = st.columns(3)


with next_col1:

    with st.container(border=True):

        st.subheader("📈 Pp / Ppk")

        st.write(
            "Long-term process performance indices."
        )


with next_col2:

    with st.container(border=True):

        st.subheader("📉 Control Charts")

        st.write(
            "I-MR, X-bar/R and other SPC tools."
        )


with next_col3:

    with st.container(border=True):

        st.subheader("📊 SPC Tools")

        st.write(
            "Additional statistical quality tools."
        )


# =========================================================
# ENGINEERING APPROACH
# =========================================================

st.divider()

st.header("Engineering Approach")

st.write(
    """
    The objective of this toolkit is not only to calculate
    statistical indices, but also to explain what the results
    mean from an engineering perspective.
    """
)

st.info(
    """
    Capability indices should be interpreted together with
    process stability, measurement-system adequacy,
    data characteristics, and applicable customer or
    site requirements.
    """
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="qe-footer">
        Quality Engineering Toolkit
        &nbsp;•&nbsp;
        Process Capability
        &nbsp;•&nbsp;
        SPC
        &nbsp;•&nbsp;
        Statistical Quality
    </div>
    """,
    unsafe_allow_html=True
)