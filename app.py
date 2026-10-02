import streamlit as st
import time
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind · AI Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)