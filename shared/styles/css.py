"""
Sports Intelligence Platform

File: css.py
Author: Syed Faran Ali

Description:
Global application CSS.
"""

import streamlit as st


def load_css() -> None:
    """Load global CSS."""

    st.markdown(
        """
<style>

/* Hide Streamlit default UI */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:#ffffff;
border-right:1px solid #e5e7eb;
}

/* Buttons */

.stButton>button{

width:100%;

border-radius:10px;

height:44px;

font-weight:600;

}

/* Cards */

.block-container{

padding-top:2rem;

padding-left:2rem;

padding-right:2rem;

}

/* Title */

.main-title{

font-size:42px;

font-weight:700;

color:#1f2937;

}

.subtitle{

font-size:18px;

color:#6b7280;

}

</style>
        """,
        unsafe_allow_html=True,
    )