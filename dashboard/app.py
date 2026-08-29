import streamlit as st
import pandas as pd
import os
import re
import io

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Data Modernization",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    /* ===== Smart Data Modernization - Minimal Enterprise UI ===== */
    .stApp {
        background: #07111d;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #08111f 0%, #0b1424 100%);
    }

    [data-testid="stHeader"] {
        background: rgba(8, 17, 31, 0.82);
        backdrop-filter: blur(8px);
        border-bottom: 1px solid rgba(148, 163, 184, 0.18);
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    [data-testid="stAppViewContainer"] > .main {
        border-top: 1px solid rgba(96, 165, 250, 0.12);
    }

    main .block-container {
        padding-top: 1.0rem;
        padding-bottom: 2.5rem;
        max-width: 1500px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1728 0%, #09111f 100%);
        border-right: 1px solid rgba(148, 163, 184, 0.18);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.1rem;
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }

    section[data-testid="stSidebar"] * {
        color: #e6edf7;
    }

    section[data-testid="stSidebar"] .stRadio > label,
    section[data-testid="stSidebar"] .stMultiSelect > label {
        color: #8fa3bd !important;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    section[data-testid="stSidebar"] [data-testid="stRadio"] > label {
        margin-bottom: 0.55rem;
        color: #cbd8e8 !important;
        font-size: 0.86rem;
        letter-spacing: 0;
        text-transform: none;
    }

    section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] {
        gap: 0.28rem;
    }

    section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radio"] {
        min-height: 2.35rem;
        padding: 0.35rem 0.55rem;
        border: 1px solid transparent;
        border-radius: 10px;
        transition: background 0.18s ease, border-color 0.18s ease;
    }

    section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radio"]:hover {
        background: rgba(96, 165, 250, 0.08);
        border-color: rgba(96, 165, 250, 0.18);
    }

    section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radio"][aria-checked="true"] {
        background: linear-gradient(90deg, rgba(96, 165, 250, 0.18), rgba(34, 197, 94, 0.06));
        border-color: rgba(96, 165, 250, 0.35);
        box-shadow: inset 3px 0 0 #60a5fa;
    }

    section[data-testid="stSidebar"] [data-testid="stMultiSelect"] {
        margin-bottom: 0.65rem;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        min-height: 2.55rem;
        border-color: rgba(148, 163, 184, 0.2);
        border-radius: 9px;
        background: rgba(15, 27, 45, 0.82);
    }

    div[data-testid="stSidebarNav"] {
        padding-top: 0.35rem;
    }

    div[data-testid="stSidebarNav"] a {
        border-radius: 10px;
        margin: 3px 0;
        padding: 0.6rem 0.75rem;
        transition: background 0.18s ease, border-color 0.18s ease;
    }

    div[data-testid="stSidebarNav"] a:hover {
        background: rgba(148, 163, 184, 0.08);
        border: 1px solid rgba(148, 163, 184, 0.16);
    }

    .brand {
        padding: 10px 8px 18px 8px;
        border-bottom: 1px solid rgba(148, 163, 184, 0.18);
        margin-bottom: 18px;
    }

    .brand-name {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.6px;
        color: #f8fafc;
    }

    .brand-sub {
        color: #8fa3bd;
        font-size: 12px;
        margin-top: 4px;
        line-height: 1.5;
    }

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 18px;
        min-width: 0;
        min-height: 88px;
        padding: 18px 22px;
        margin: 0 0 24px 0;
        background: linear-gradient(135deg, #101d32 0%, #0d1728 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        box-shadow: 0 12px 28px rgba(2, 6, 23, 0.22);
    }

    .topbar-right {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 5px;
    }

    .top-title {
        font-size: 27px;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.7px;
    }

    .top-sub {
        font-size: 13px;
        color: #9bb0c9;
        margin-top: 4px;
    }

    .top-status-wrap {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 5px;
    }

    .top-status {
        padding: 7px 12px;
        border: 1px solid rgba(34, 197, 94, 0.35);
        border-radius: 999px;
        background: rgba(16, 185, 129, 0.08);
        color: #96f0be;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        white-space: nowrap;
    }

    .top-status-detail {
        color: #8aa2bf;
        font-size: 10px;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        white-space: nowrap;
    }

    .top-page {
        color: #dbeafe;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    }

    .main-title {
        font-size: 2.15rem;
        font-weight: 800;
        line-height: 1.2;
        letter-spacing: -0.06em;
        color: #f8fafc;
        margin: 0.2rem 0 0.15rem 0;
    }

    .sub-title {
        font-size: 0.98rem;
        color: #9bb0c9;
        margin-bottom: 0.5rem;
        letter-spacing: 0.01em;
    }

    .premium-page-header {
        position: relative;
        padding: 1.15rem 1.2rem 0.9rem 1.2rem;
        margin: 0.2rem 0 1.4rem 0;
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(15, 27, 45, 0.95), rgba(10, 18, 31, 0.9));
        box-shadow: 0 10px 24px rgba(2, 6, 23, 0.12);
        overflow: hidden;
    }

    .premium-page-header:before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(180deg, #60a5fa, #22c55e);
    }

    .premium-page-title-row {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 0.4rem;
    }

    .premium-page-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 2.5rem;
        height: 2.5rem;
        border-radius: 12px;
        background: rgba(96, 165, 250, 0.1);
        border: 1px solid rgba(96, 165, 250, 0.18);
        font-size: 1.3rem;
    }

    .premium-page-title {
        font-size: clamp(1.7rem, 2vw, 2.6rem);
        color: #f8fafc;
        font-weight: 800;
        letter-spacing: -0.07em;
        line-height: 1.2;
    }

    .premium-page-subtitle {
        color: #9bb0c9;
        font-size: 0.98rem;
        letter-spacing: 0.01em;
        margin-left: 3.3rem;
    }

    .page-head {
        margin: 0.2rem 0 1.25rem 0;
    }

    .page-title {
        font-size: 34px;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.8px;
    }

    .page-desc {
        color: #91a4bd;
        font-size: 14px;
        margin-top: 5px;
    }

    .section-card {
        background: rgba(15, 27, 45, 0.92);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 16px;
        padding: 18px 20px;
        margin: 10px 0 18px 0;
        box-shadow: 0 8px 24px rgba(2, 6, 23, 0.12);
    }

    h1, h2, h3, h4, h5, h6 {
        letter-spacing: -0.04em;
        color: #f8fafc;
    }

    .stSubheader {
        padding: 0.68rem 0.9rem;
        margin: 0.9rem 0 0.8rem 0;
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-left: 4px solid #60a5fa;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(15, 27, 45, 0.98), rgba(10, 18, 31, 0.88));
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
        color: #edf4ff !important;
        font-weight: 700;
        letter-spacing: -0.03em;
        line-height: 1.35;
    }

    .stSubheader > div {
        color: #edf4ff !important;
    }

    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    .stMarkdown h5,
    .stMarkdown h6 {
        margin: 0.9rem 0 0.8rem 0;
        padding: 0.7rem 0.9rem;
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-left: 4px solid #60a5fa;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(15, 27, 45, 0.98), rgba(10, 18, 31, 0.88));
        color: #edf4ff !important;
        font-weight: 700;
        letter-spacing: -0.03em;
        line-height: 1.35;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #111f34 0%, #0d192b 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 14px;
        padding: 16px 17px;
        box-shadow: 0 8px 22px rgba(2, 6, 23, 0.18);
    }

    div[data-testid="stMetric"] label {
        color: #9bb0c9;
        font-size: 12px;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc;
        font-weight: 800;
        letter-spacing: -0.03em;
    }

    .stButton > button {
        min-height: 2.35rem;
        padding: 0.42rem 0.65rem;
        border-radius: 999px;
        border: 1px solid #30415c;
        background: #132139;
        color: #dbeafe;
        font-size: 0.76rem;
        white-space: nowrap;
    }

    .stButton > button:hover {
        border-color: #6b7f9e;
        transform: translateY(-1px);
        box-shadow: 0 8px 16px rgba(15, 23, 42, 0.12);
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-radius: 12px;
        overflow: hidden;
        background: rgba(10, 18, 31, 0.65);
    }

    div[data-testid="stDataFrame"] > div {
        border-radius: 12px;
    }

    .stAlert {
        border-radius: 12px;
        border: 1px solid rgba(148, 163, 184, 0.18);
    }

    div[data-testid="stChatMessage"] {
        box-sizing: border-box;
        max-width: 84%;
        margin: 0.25rem 0 0.55rem 0;
        padding: 0.72rem 0.95rem;
        border: 1px solid #263650;
        border-radius: 16px;
        background: #0f1b2d;
        color: #f8fafc !important;
        line-height: 1.6;
    }

    div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"],
    div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] *,
    div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p,
    div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] span,
    div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] strong {
        color: #f8fafc !important;
        font-size: 0.92rem;
        line-height: 1.6;
    }

    div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]),
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]),
    div[data-testid="stChatMessage"][aria-label*="user"] {
        max-width: 75%;
        margin-left: auto;
        border-color: rgba(56, 189, 248, 0.34);
        background: #111f34;
    }

    div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]),
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]),
    div[data-testid="stChatMessage"][aria-label*="assistant"] {
        max-width: 84%;
        margin-right: auto;
        border-color: rgba(148, 163, 184, 0.18);
        background: #0f1b2d;
    }

    div[data-testid="stChatInput"] {
        border: 1px solid #30415c !important;
        border-radius: 15px;
        background: #0f1b2d !important;
        box-shadow: 0 10px 28px rgba(2, 6, 23, 0.2);
    }

    div[data-testid="stChatInput"] > div,
    div[data-testid="stChatInput"] textarea,
    div[data-testid="stChatInput"] input {
        background: #0f1b2d !important;
        border-color: #30415c !important;
        color: #f8fafc !important;
        caret-color: #7dd3fc;
        font-size: 0.94rem;
    }

    div[data-testid="stChatInput"] textarea::placeholder,
    div[data-testid="stChatInput"] input::placeholder {
        color: #7f91a8 !important;
        opacity: 1;
    }

    div[data-testid="stChatInput"]:focus-within {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.1), 0 12px 30px rgba(2, 6, 23, 0.24);
    }

    .ai-page-shell {
        width: 100%;
        max-width: 1040px;
        margin: 0 auto;
    }

    .ai-page-header {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.5rem;
        padding: 1.35rem 1.5rem;
        margin: 0.15rem 0 1rem 0;
        overflow: hidden;
        border: 1px solid rgba(96, 165, 250, 0.22);
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(17, 31, 52, 0.98), rgba(10, 20, 36, 0.96));
        box-shadow: 0 14px 32px rgba(2, 6, 23, 0.2);
    }

    .ai-page-header:before {
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 3px;
        background: linear-gradient(180deg, #60a5fa, #2dd4bf);
    }

    .ai-header-main {
        min-width: 0;
    }

    .ai-header-title {
        color: #f8fafc;
        font-size: clamp(1.35rem, 2vw, 1.9rem);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.2;
    }

    .ai-header-subtitle {
        margin-top: 0.42rem;
        color: #a7b7ca;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .ai-status {
        flex: 0 0 auto;
        padding: 0.5rem 0.72rem;
        border: 1px solid rgba(45, 212, 191, 0.32);
        border-radius: 999px;
        background: rgba(45, 212, 191, 0.08);
        color: #99f6e4;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        white-space: nowrap;
    }

    .ai-context-card {
        padding: 0.8rem 1rem;
        margin-bottom: 1.2rem;
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-radius: 12px;
        background: rgba(15, 27, 45, 0.74);
    }

    .ai-context-label {
        color: #7f93ad;
        font-size: 0.66rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .ai-context-value {
        margin-top: 0.35rem;
        color: #dbeafe;
        font-size: 0.84rem;
        line-height: 1.5;
    }

    .ai-context-count {
        color: #99f6e4;
        font-weight: 800;
    }

    .ai-welcome-card {
        padding: 1.65rem 1.5rem;
        margin: 0.5rem 0 1.2rem 0;
        text-align: center;
        border: 1px solid rgba(96, 165, 250, 0.18);
        border-radius: 16px;
        background: linear-gradient(145deg, rgba(15, 27, 45, 0.88), rgba(10, 18, 31, 0.72));
    }

    .ai-welcome-icon {
        font-size: 2rem;
    }

    .ai-welcome-title {
        margin-top: 0.45rem;
        color: #f8fafc;
        font-size: 1.2rem;
        font-weight: 800;
    }

    .ai-welcome-copy {
        max-width: 560px;
        margin: 0.5rem auto 0;
        color: #a7b7ca;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .ai-section-label {
        margin: 0.8rem 0 0.55rem;
        color: #a7b7ca;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    .ai-suggestion-grid .stButton > button {
        min-height: 2.35rem;
        padding: 0.42rem 0.65rem;
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 999px;
        background: rgba(17, 31, 52, 0.88);
        color: #dbeafe;
        font-size: 0.76rem;
        white-space: nowrap;
    }

    .ai-suggestion-grid .stButton > button:hover {
        border-color: rgba(96, 165, 250, 0.62);
        background: rgba(96, 165, 250, 0.12);
        color: #f8fafc;
        transform: translateY(-1px);
    }

    .ai-chat-area {
        padding: 0.2rem 0;
    }

    .ai-chat-area div[data-testid="stChatMessage"] {
        max-width: 88%;
        padding: 0.72rem 0.9rem;
        border-radius: 14px;
        background: #0f1b2d;
    }

    .ai-chat-area div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        color: #f8fafc !important;
        font-size: 0.92rem;
        line-height: 1.62;
    }

    .ai-chat-area div[data-testid="stChatMessage"] p {
        color: #f8fafc !important;
    }

    .upload-intro {
        padding: 1.15rem 1.25rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 15px;
        background: linear-gradient(135deg, rgba(17, 31, 52, 0.95), rgba(10, 20, 36, 0.9));
    }

    .upload-intro-title {
        color: #f8fafc;
        font-size: 1rem;
        font-weight: 800;
    }

    .upload-intro-copy {
        margin-top: 0.35rem;
        color: #a7b7ca;
        font-size: 0.88rem;
        line-height: 1.55;
    }

    .upload-context-card {
        padding: 0.9rem 1rem;
        margin: 0.6rem 0 1rem;
        border: 1px solid rgba(52, 211, 153, 0.22);
        border-radius: 12px;
        background: rgba(16, 185, 129, 0.06);
    }

    .upload-context-label {
        color: #6ee7b7;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    .upload-context-value {
        margin-top: 0.35rem;
        color: #d1fae5;
        font-size: 0.86rem;
    }

    .upload-section-title {
        margin: 1.25rem 0 0.7rem;
        padding: 0.62rem 0.8rem;
        border-left: 4px solid #38bdf8;
        border-radius: 9px;
        background: rgba(15, 27, 45, 0.85);
        color: #f8fafc;
        font-size: 0.98rem;
        font-weight: 800;
    }

    .validation-banner {
        display: flex;
        flex-direction: column;
        gap: 0.35rem;
        padding: 1rem 1.2rem;
        margin: 1rem 0 1.25rem;
        border: 1px solid rgba(16, 185, 129, 0.38);
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(11, 52, 42, 0.95), rgba(10, 23, 34, 0.92));
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
    }

    .validation-banner-title {
        color: #d1fae5;
        font-size: 1.02rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }

    .validation-banner-subtitle {
        color: #ecfdf5;
        font-size: 0.92rem;
        font-weight: 600;
    }

    .dataset-overview-card {
        padding: 1.15rem 1.15rem 1rem;
        margin: 1.2rem 0 1.1rem;
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 18px;
        background: linear-gradient(180deg, rgba(16, 28, 42, 0.96), rgba(11, 20, 31, 0.9));
        box-shadow: 0 12px 30px rgba(2, 6, 23, 0.18);
    }

    .dataset-overview-header {
        margin: 0 0 1rem;
        color: #f8fafc;
        font-size: 1.05rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }

    .dataset-metric-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.9rem;
    }

    .dataset-metric-card {
        min-height: 122px;
        padding: 1rem 1rem 0.9rem;
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 14px;
        background: linear-gradient(180deg, rgba(15, 27, 45, 0.95), rgba(12, 19, 29, 0.92));
        transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
    }

    .dataset-metric-card:hover {
        transform: translateY(-1px);
        border-color: rgba(96, 165, 250, 0.42);
        box-shadow: 0 8px 18px rgba(59, 130, 246, 0.12);
    }

    .dataset-metric-card.warning {
        border-color: rgba(251, 191, 36, 0.38);
        background: linear-gradient(180deg, rgba(55, 36, 11, 0.88), rgba(19, 21, 30, 0.9));
    }

    .dataset-metric-card.healthy {
        border-color: rgba(16, 185, 129, 0.34);
        background: linear-gradient(180deg, rgba(8, 42, 34, 0.9), rgba(12, 19, 29, 0.92));
    }

    .dataset-metric-label {
        color: #cfe1f5;
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .dataset-metric-value {
        margin-top: 0.8rem;
        color: #f8fafc;
        font-size: clamp(1.3rem, 1.6vw, 2rem);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.2;
        word-break: break-word;
    }

    .dataset-metric-footnote {
        margin-top: 0.55rem;
        color: #8db2d5;
        font-size: 0.73rem;
        font-weight: 600;
    }

    .dataset-columns-card {
        padding: 1.1rem 1.1rem 1rem;
        margin-top: 0.2rem;
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 16px;
        background: linear-gradient(180deg, rgba(12, 22, 35, 0.95), rgba(11, 18, 29, 0.9));
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.02);
    }

    .dataset-columns-header {
        margin: 0 0 0.8rem;
        color: #f8fafc;
        font-size: 1rem;
        font-weight: 800;
    }

    .dataset-column-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
    }

    .dataset-column-pill {
        display: inline-flex;
        align-items: center;
        max-width: 100%;
        padding: 0.52rem 0.7rem;
        border: 1px solid rgba(96, 165, 250, 0.22);
        border-radius: 999px;
        background: rgba(23, 38, 57, 0.92);
        color: #e2f0ff;
        font-size: 0.82rem;
        font-weight: 600;
        line-height: 1.3;
        white-space: normal;
        word-break: break-word;
    }

    .muted-caption {
        margin-top: 0.8rem;
        color: #9bb0c9;
        font-size: 0.82rem;
        line-height: 1.55;
    }

    @media (max-width: 900px) {
        .dataset-metric-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media (max-width: 560px) {
        .dataset-metric-grid {
            grid-template-columns: 1fr;
        }

        .dataset-column-pill {
            font-size: 0.76rem;
        }

        .validation-banner {
            padding: 0.9rem 1rem;
        }
    }

    @media (max-width: 800px) {
        .upload-section-title {
            margin-top: 1rem;
        }
    }

    @media (max-width: 800px) {
        .ai-page-header {
            align-items: flex-start;
            flex-direction: column;
            gap: 0.8rem;
            padding: 1.1rem 1.15rem;
        }

        .ai-status {
            font-size: 0.62rem;
        }

            div[data-testid="stChatMessage"],
            div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]),
            div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]),
            div[data-testid="stChatMessage"][aria-label*="user"],
            div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]),
            div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]),
            div[data-testid="stChatMessage"][aria-label*="assistant"] {
                max-width: 100%;
        }
    }

    .footer {
        margin-top: 58px;
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #0f1c30 0%, #0a1424 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        box-shadow: 0 -8px 30px rgba(2, 6, 23, 0.15);
    }

    .footer-grid {
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr 1fr;
        gap: 28px;
    }

    .footer-brand {
        font-size: 21px;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.04em;
    }

    .footer-heading {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #a7b7ca;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .footer-text {
        color: #8195ae;
        font-size: 13px;
        line-height: 1.7;
    }

    .footer-list {
        margin: 0;
        padding: 0;
        list-style: none;
        color: #8195ae;
        font-size: 13px;
        line-height: 1.9;
    }

    .footer-pill {
        display: inline-block;
        padding: 6px 10px;
        margin: 3px;
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 999px;
        color: #c7d2e4;
        font-size: 11px;
        background: rgba(148, 163, 184, 0.04);
    }

    .footer-bottom {
        margin-top: 24px;
        padding-top: 17px;
        border-top: 1px solid rgba(148, 163, 184, 0.2);
        color: #7e90a8;
        font-size: 11px;
        display: flex;
        justify-content: space-between;
        gap: 10px;
        flex-wrap: wrap;
    }

    @media (max-width: 1100px) {
        .footer-grid {
            grid-template-columns: 1.2fr 1fr 1fr;
        }
    }

    @media (max-width: 800px) {
        .footer-grid {
            grid-template-columns: 1fr;
        }

        .topbar {
            padding: 16px 18px;
            align-items: flex-start;
            flex-direction: column;
        }

        .topbar-right {
            align-items: flex-start;
        }

        .top-status-wrap {
            align-items: flex-start;
        }

        .top-status {
            display: none;
        }

        .top-title {
            font-size: 22px;
        }

        .premium-page-title {
            font-size: 1.8rem;
        }

        .premium-page-subtitle {
            margin-left: 0;
        }

        .premium-page-title-row {
            align-items: flex-start;
        }

        .main-title {
            font-size: 1.75rem;
        }

        .page-title {
            font-size: 28px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD MAIN DATA
# ============================================================

@st.cache_data
def load_data():

    file_path = "data/cleaned_superstore.csv"

    if not os.path.exists(file_path):
        return None

    data = pd.read_csv(file_path)

    data["order_date"] = pd.to_datetime(
        data["order_date"],
        errors="coerce"
    )

    data["ship_date"] = pd.to_datetime(
        data["ship_date"],
        errors="coerce"
    )

    # Make sure numeric columns are numeric
    for col in [
        "sales",
        "profit",
        "quantity",
        "discount",
        "shipping_cost",
        "shipping_days"
    ]:

        if col in data.columns:
            data[col] = pd.to_numeric(
                data[col],
                errors="coerce"
            )

    return data


df = load_data()


# ============================================================
# DATA FILE CHECK
# ============================================================

if df is None:

    st.error(
        "cleaned_superstore.csv not found inside the data folder."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div class="brand">
        <div class="brand-name">📊 Smart Data</div>
        <div class="brand-sub">Modernization & Intelligence Platform</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()

st.sidebar.subheader("🧭 Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "📊 Executive Dashboard",
        "📈 Sales Analytics",
        "👥 Customer Intelligence",
        "🤖 ML Analytics",
        "🚨 Anomaly Detection",
        "💡 Business Insights",
        "⚙️ Data Quality",
        "🤖 AI Business Assistant",
        "📂 Upload Business Data"
    ]
)

st.sidebar.divider()


# ============================================================
# GLOBAL FILTERS
# ============================================================

st.sidebar.subheader("🔎 Global Filters")

years = sorted(
    df["year"].dropna().unique().tolist()
)

selected_years = st.sidebar.multiselect(
    "Year",
    years,
    default=years
)


categories = sorted(
    df["category"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)


regions = sorted(
    df["region"].dropna().unique().tolist()
)

selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    df["year"].isin(selected_years)
    &
    df["category"].isin(selected_categories)
    &
    df["region"].isin(selected_regions)
].copy()

# ============================================================
# APPLICATION TOP BAR
# ============================================================

filtered_record_count = len(filtered_df)
filtered_order_count = filtered_df["order_id"].nunique()
selected_filter_summary = (
    f"{filtered_record_count:,} Records • {filtered_order_count:,} Orders"
)

st.markdown(
    f"""
    <div class="topbar">
        <div class="topbar-left">
            <div class="top-title">Smart Data Modernization</div>
            <div class="top-sub">Analytics &amp; Intelligence Platform</div>
        </div>
        <div class="topbar-right">
            <div class="top-page">{page}</div>
            <div class="top-status">● SYSTEM ONLINE</div>
            <div class="top-status-detail">{selected_filter_summary}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTION
# ============================================================

def render_page_header(icon, title, subtitle):
    st.markdown(
        f"""
        <div class="premium-page-header">
            <div class="premium-page-title-row">
                <span class="premium-page-icon">{icon}</span>
                <span class="premium-page-title">{title}</span>
            </div>
            <div class="premium-page-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_kpis(data):

    total_sales = data["sales"].sum()

    total_profit = data["profit"].sum()

    total_quantity = data["quantity"].sum()

    total_orders = data["order_id"].nunique()

    if total_sales != 0:
        profit_margin = (
            total_profit / total_sales
        ) * 100
    else:
        profit_margin = 0

    if "shipping_days" in data.columns:
        avg_shipping_days = (
            data["shipping_days"].mean()
        )
    else:
        avg_shipping_days = 0

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "💰 Total Sales",
        f"${total_sales:,.0f}"
    )

    col2.metric(
        "📈 Total Profit",
        f"${total_profit:,.0f}"
    )

    col3.metric(
        "📦 Quantity",
        f"{total_quantity:,.0f}"
    )

    col4.metric(
        "🛒 Orders",
        f"{total_orders:,}"
    )

    col5.metric(
        "📊 Profit Margin",
        f"{profit_margin:.2f}%"
    )


def answer_business_question(question, data):

    normalized_question = question.strip().lower()

    unsupported_response = (
        "I can currently answer questions about sales, profit, orders, customers, "
        "categories, regions, shipping, discounts and business performance.\n\n"
        "Try: What is total sales?\n"
        "Which region has the highest profit?\n"
        "Who are the top 5 customers by profit?"
    )

    if data.empty:
        return "There is no data available for the current filter selection."

    def has_columns(*columns):
        return all(column in data.columns for column in columns)

    if "profit margin" in normalized_question:
        if not has_columns("sales", "profit"):
            return unsupported_response
        total_sales = data["sales"].sum()
        total_profit = data["profit"].sum()
        profit_margin = (
            (total_profit / total_sales) * 100
            if total_sales != 0
            else 0
        )
        return f"The profit margin for the current filtered data is **{profit_margin:.2f}%**."

    ranking_requests = [
        ("category", "profit", "category", "highest profit", "highest-profit category"),
        ("category", "sales", "category", "highest sales", "highest-sales category"),
        ("region", "profit", "region", "highest profit", "highest-profit region"),
        ("region", "sales", "region", "highest sales", "highest-sales region"),
        ("ship_mode", "sales", "shipping mode", "highest sales", "highest-sales shipping mode")
    ]

    for group_column, value_column, label, phrase, result_label in ranking_requests:
        if (
            (phrase in normalized_question or phrase.replace("highest", "most") in normalized_question)
            and label in normalized_question
        ):
            if not has_columns(group_column, value_column):
                return unsupported_response
            ranking = data.groupby(group_column)[value_column].sum().sort_values(ascending=False)
            if ranking.empty:
                return unsupported_response
            winner = ranking.index[0]
            return (
                f"🏆 **{winner}** is the {result_label}.\n\n"
                f"Total {value_column.replace('_', ' ').title()}: **${ranking.iloc[0]:,.2f}**"
            )

    if "top customer" in normalized_question or "top customers" in normalized_question:
        if not has_columns("customer_name", "profit"):
            return unsupported_response
        match = re.search(r"top\s+(\d+)", normalized_question)
        top_count = int(match.group(1)) if match else 5
        top_count = max(1, min(top_count, 10))
        ranking = (
            data.groupby("customer_name")["profit"]
            .sum()
            .sort_values(ascending=False)
            .head(top_count)
        )
        if ranking.empty:
            return unsupported_response
        lines = [f"👥 **Top {len(ranking)} Customers by Profit**", ""]
        lines.extend(
            f"{index}. {customer} — **${profit:,.2f}**"
            for index, (customer, profit) in enumerate(ranking.items(), start=1)
        )
        return "\n".join(lines)

    if "loss-making" in normalized_question or "loss making" in normalized_question:
        if not has_columns("sub_category", "profit"):
            return unsupported_response
        losses = data.groupby("sub_category")["profit"].sum()
        losses = losses[losses < 0].sort_values()
        if losses.empty:
            return "No loss-making sub-categories were found in the current filtered data."
        lines = ["⚠️ **Loss-Making Sub-Categories**", ""]
        lines.extend(
            f"- {subcategory} — **${profit:,.2f}**"
            for subcategory, profit in losses.items()
        )
        return "\n".join(lines)

    if "average discount" in normalized_question or "avg discount" in normalized_question:
        if not has_columns("discount"):
            return unsupported_response
        return f"The average discount is **{data['discount'].mean():.2%}** for the current filtered data."

    if "how many orders" in normalized_question or "number of orders" in normalized_question or "order count" in normalized_question:
        if not has_columns("order_id"):
            return unsupported_response
        return f"There are **{data['order_id'].nunique():,} unique orders** in the current filtered data."

    if "total quantity" in normalized_question or "quantity sold" in normalized_question or "how much quantity" in normalized_question:
        if not has_columns("quantity"):
            return unsupported_response
        return f"The total quantity sold is **{data['quantity'].sum():,.0f} units**."

    if "total sales" in normalized_question or "sales" in normalized_question or "revenue" in normalized_question:
        if not has_columns("sales"):
            return unsupported_response
        return f"Total sales for the current filtered data are **${data['sales'].sum():,.2f}**."

    if "total profit" in normalized_question or "profit" in normalized_question or "earnings" in normalized_question:
        if not has_columns("profit"):
            return unsupported_response
        return f"Total profit for the current filtered data is **${data['profit'].sum():,.2f}**."

    return unsupported_response


STANDARD_FIELD_ORDER = [
    "date",
    "revenue",
    "quantity",
    "profit",
    "product",
    "category",
    "customer",
    "location",
    "order",
    "status",
    "channel",
    "discount",
    "cost"
]

BUSINESS_SEMANTIC_ALIASES = {
    "date": {
        "date",
        "order date",
        "order_date",
        "transaction date",
        "transaction_date",
        "purchase date",
        "purchase_date",
        "sale date",
        "sale_date",
        "created at",
        "created_at",
        "timestamp",
        "time"
    },
    "revenue": {
        "revenue",
        "sales",
        "sale",
        "amount",
        "total amount",
        "total_amount",
        "income",
        "turnover",
        "gmv",
        "total sales",
        "total_sales",
        "gross sales",
        "gross_sales",
        "net sales",
        "net_sales"
    },
    "quantity": {
        "quantity",
        "qty",
        "units",
        "units sold",
        "units_sold",
        "items",
        "item count",
        "item_count",
        "count"
    },
    "profit": {
        "profit",
        "net profit",
        "net_profit",
        "gross profit",
        "gross_profit",
        "earnings",
        "margin",
        "net earnings",
        "net_earnings"
    },
    "product": {
        "product",
        "product name",
        "product_name",
        "item",
        "item name",
        "item_name",
        "sku",
        "product title",
        "product_title"
    },
    "category": {
        "category",
        "product category",
        "product_category",
        "type",
        "segment",
        "department"
    },
    "customer": {
        "customer",
        "customer name",
        "customer_name",
        "buyer",
        "client",
        "user",
        "account",
        "shopper"
    },
    "location": {
        "location",
        "city",
        "state",
        "country",
        "region",
        "area",
        "store",
        "market",
        "territory"
    },
    "order": {
        "order id",
        "order_id",
        "transaction id",
        "transaction_id",
        "invoice",
        "invoice id",
        "invoice_id",
        "order number",
        "order_number",
        "order no",
        "orderno"
    },
    "status": {
        "status",
        "order status",
        "order_status",
        "payment status",
        "payment_status",
        "delivery status",
        "delivery_status",
        "fulfilment",
        "fulfillment"
    },
    "channel": {
        "channel",
        "sales channel",
        "sales_channel",
        "platform",
        "source",
        "marketplace",
        "store channel"
    },
    "discount": {
        "discount",
        "discount rate",
        "discount_rate",
        "discount percentage",
        "discount_percentage",
        "promotion",
        "promo"
    },
    "cost": {
        "cost",
        "shipping cost",
        "shipping_cost",
        "delivery cost",
        "delivery_cost",
        "freight",
        "shipping",
        "logistics cost",
        "logistics_cost"
    }
}

DATASET_CLASSIFIERS = [
    ("Retail", {"product", "category", "revenue"}),
    ("E-commerce", {"channel", "product", "revenue"}),
    ("Sales", {"revenue", "customer"}),
    ("Customer Transactions", {"customer", "order", "date"}),
    ("Inventory", {"product", "quantity", "category"}),
    ("Marketing", {"channel", "revenue", "customer"}),
    ("Finance", {"revenue", "profit", "cost"}),
    ("Operations", {"status", "location", "date"})
]


def normalize_business_column_name(value):
    if value is None:
        return ""
    text = str(value).strip().lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def column_matches_semantics(column_name, alias_set):
    normalized = normalize_business_column_name(column_name)
    if not normalized:
        return False

    normalized_aliases = {
        normalize_business_column_name(alias)
        for alias in alias_set
    }

    if normalized in normalized_aliases:
        return True

    tokens = set(normalized.split())
    for alias in normalized_aliases:
        alias_tokens = set(alias.split())
        if alias_tokens and (
            alias_tokens.issubset(tokens)
            or tokens.issubset(alias_tokens)
            or alias_tokens & tokens
        ):
            return True

    return False


def detect_business_column_semantics(column_name):
    for semantic_name, alias_set in BUSINESS_SEMANTIC_ALIASES.items():
        if column_matches_semantics(column_name, alias_set):
            return semantic_name
    return None


def safe_numeric_conversion(series):
    cleaned = series.copy()
    cleaned = cleaned.map(
        lambda value: value.strip() if isinstance(value, str) else value
    )
    cleaned = cleaned.replace({"": pd.NA, "N/A": pd.NA, "NA": pd.NA, "null": pd.NA, "None": pd.NA})
    cleaned = cleaned.map(lambda value: value.replace("$", "").replace(",", "").replace("%", "") if isinstance(value, str) else value)
    cleaned = pd.to_numeric(cleaned, errors="coerce")
    return cleaned


def classify_business_dataset(semantic_columns):
    matched_semantics = set(semantic_columns.keys())
    if not matched_semantics:
        return "General Business Data", 0.0

    best_label = "General Business Data"
    best_score = 0.0

    for label, required_semantics in DATASET_CLASSIFIERS:
        score = sum(1 for item in required_semantics if item in matched_semantics)
        if score > best_score:
            best_label = label
            best_score = score

    max_possible = max(len(required) for _, required in DATASET_CLASSIFIERS)
    confidence = min(0.99, (best_score / max(1, max_possible)) * 1.1)
    if best_score == 0:
        confidence = 0.15
    return best_label, round(confidence, 2)


def detect_uploaded_business_structure(frame):
    mapping = {}
    semantic_columns = {}

    for column in frame.columns:
        semantic = detect_business_column_semantics(column)
        if semantic:
            mapping[column] = semantic
            semantic_columns.setdefault(semantic, []).append(column)

    dataset_type, confidence = classify_business_dataset(semantic_columns)

    if not mapping:
        return {
            "mapping": {},
            "semantic_columns": {},
            "dataset_type": "General Business Data",
            "confidence": 0.0,
            "is_business_like": False,
            "column_quality": []
        }

    column_quality = []
    for column in frame.columns:
        values = frame[column]
        missing = int(values.isna().sum())
        unique_count = int(values.nunique(dropna=True))
        numeric_like = pd.to_numeric(values, errors="coerce").notna().sum()
        is_date_like = False
        try:
            pd.to_datetime(values, errors="raise")
            is_date_like = True
        except Exception:
            is_date_like = False

        semantic = mapping.get(column)
        column_quality.append({
            "Column": column,
            "Detected Meaning": semantic or "Unclassified",
            "Missing Values": missing,
            "Unique Values": unique_count,
            "Numeric-Like Values": numeric_like,
            "Date-Like": is_date_like,
            "Sample Values": values.dropna().head(3).tolist()
        })

    return {
        "mapping": mapping,
        "semantic_columns": semantic_columns,
        "dataset_type": dataset_type,
        "confidence": confidence,
        "is_business_like": len(mapping) >= 2 or confidence >= 0.2,
        "column_quality": column_quality
    }


def measure_data_quality(frame):
    numeric_columns = []
    categorical_columns = []
    date_columns = []
    issues = []

    for column in frame.columns:
        series = frame[column]
        non_null = series.dropna()
        if non_null.empty:
            categorical_columns.append(column)
            continue

        numeric_values = pd.to_numeric(series, errors="coerce")
        numeric_ratio = numeric_values.notna().mean()

        try:
            pd.to_datetime(series, errors="raise")
            date_columns.append(column)
        except Exception:
            pass

        if numeric_ratio > 0.7 and series.nunique(dropna=True) > 1:
            numeric_columns.append(column)
        else:
            categorical_columns.append(column)

        if numeric_ratio > 0.7 and series.isna().sum() > len(series) * 0.3:
            issues.append(f"Column '{column}' has a large number of missing values.")

    duplicate_rows = int(frame.duplicated().sum())
    missing_values = int(frame.isna().sum().sum())

    if duplicate_rows:
        issues.append(f"{duplicate_rows} duplicate rows were detected.")

    return {
        "rows": len(frame),
        "columns": len(frame.columns),
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "date_columns": date_columns,
        "issues": issues
    }


def resolve_metric_column(data, aliases):
    for alias in aliases:
        for column in data.columns:
            if normalize_business_column_name(column) == normalize_business_column_name(alias):
                return column
    for alias in aliases:
        alias_norm = normalize_business_column_name(alias)
        for column in data.columns:
            if normalize_business_column_name(column).startswith(alias_norm) or alias_norm.startswith(normalize_business_column_name(column)):
                return column
    for alias in aliases:
        alias_norm = normalize_business_column_name(alias)
        for column in data.columns:
            if alias_norm in normalize_business_column_name(column).split():
                return column
    return None


def generate_dynamic_kpis(data, semantic_info):
    if data is None or data.empty:
        return []

    kpis = []
    revenue_column = resolve_metric_column(data, ["revenue", "sales", "amount", "total sales", "total_amount", "turnover", "income", "gmv"])
    profit_column = resolve_metric_column(data, ["profit", "net profit", "gross profit", "earnings", "margin"])
    quantity_column = resolve_metric_column(data, ["quantity", "qty", "units", "units sold", "count", "items"])
    order_column = resolve_metric_column(data, ["order id", "order_id", "transaction id", "invoice", "order number", "orders"])
    customer_column = resolve_metric_column(data, ["customer", "customer name", "buyer", "client", "user"])
    product_column = resolve_metric_column(data, ["product", "product name", "item", "sku"])
    date_column = resolve_metric_column(data, ["date", "order date", "purchase date", "transaction date", "created at", "timestamp"])

    revenue_series = safe_numeric_conversion(data[revenue_column]) if revenue_column else pd.Series(dtype=float)
    profit_series = safe_numeric_conversion(data[profit_column]) if profit_column else pd.Series(dtype=float)
    quantity_series = safe_numeric_conversion(data[quantity_column]) if quantity_column else pd.Series(dtype=float)

    if not revenue_series.empty:
        kpis.append({"label": "TOTAL REVENUE", "value": f"${revenue_series.sum():,.0f}"})
    elif "sales" in data.columns:
        series = safe_numeric_conversion(data["sales"])
        kpis.append({"label": "TOTAL SALES", "value": f"${series.sum():,.0f}"})

    if not profit_series.empty:
        kpis.append({"label": "TOTAL PROFIT", "value": f"${profit_series.sum():,.0f}"})

    if not quantity_series.empty:
        kpis.append({"label": "TOTAL UNITS", "value": f"{quantity_series.sum():,.0f}"})

    if order_column:
        order_count = data[order_column].nunique() if data[order_column].dtype == object else len(data)
        kpis.append({"label": "TOTAL ORDERS", "value": f"{order_count:,}"})

    if customer_column:
        kpis.append({"label": "UNIQUE CUSTOMERS", "value": f"{data[customer_column].nunique():,}"})

    if product_column:
        kpis.append({"label": "UNIQUE PRODUCTS", "value": f"{data[product_column].nunique():,}"})

    if date_column:
        parsed_dates = pd.to_datetime(data[date_column], errors="coerce")
        valid_dates = parsed_dates.dropna()
        if not valid_dates.empty:
            kpis.append({"label": "DATE RANGE", "value": f"{valid_dates.min().date()} → {valid_dates.max().date()}"})

    if revenue_column and order_column:
        order_count = data[order_column].nunique() if data[order_column].dtype == object else len(data)
        if order_count:
            avg_order = revenue_series.sum() / order_count
            kpis.append({"label": "AVERAGE ORDER VALUE", "value": f"${avg_order:,.0f}"})

    if revenue_column and profit_column:
        total_revenue = revenue_series.sum()
        total_profit = profit_series.sum()
        if total_revenue:
            margin = (total_profit / total_revenue) * 100
            kpis.append({"label": "PROFIT MARGIN", "value": f"{margin:.2f}%"})

    return kpis


def build_dynamic_charts(data, semantic_info):
    if data is None or data.empty:
        return []

    charts = []
    categories = [
        ("date", "revenue"),
        ("date", "sales"),
        ("date", "amount"),
        ("category", "revenue"),
        ("category", "sales"),
        ("category", "profit"),
        ("product", "revenue"),
        ("product", "sales"),
        ("location", "revenue"),
        ("location", "sales"),
        ("channel", "revenue"),
        ("channel", "sales"),
        ("status", None)
    ]

    for dim, metric in categories:
        if dim == "status":
            status_column = resolve_metric_column(data, ["status", "order status", "delivery status", "payment status", "fulfilment"])
            if status_column is not None:
                counts = data[status_column].dropna().value_counts().head(10)
                if not counts.empty:
                    charts.append({"title": "Orders by Status", "type": "bar", "data": counts})
            continue

        dim_column = resolve_metric_column(data, [
            dim,
            dim.replace("_", " "),
            "customer",
            "region",
            "location",
            "category",
            "product",
            "item",
            "market",
            "type",
            "channel",
            "sales channel",
            "state",
            "country",
            "city"
        ])
        metric_column = resolve_metric_column(data, [
            metric or "revenue",
            "sales",
            "amount",
            "total amount",
            "income",
            "profit",
            "quantity",
            "units",
            "qty"
        ]) if metric else None

        if dim_column is None:
            continue

        if metric and metric_column is None:
            continue

        if dim == "date":
            actual_date_col = resolve_metric_column(data, ["date", "order date", "purchase date", "transaction date", "created at", "timestamp"])
            if actual_date_col is not None and metric_column is not None:
                series = data[[actual_date_col, metric_column]].copy()
                series[actual_date_col] = pd.to_datetime(series[actual_date_col], errors="coerce")
                series = series.dropna()
                if not series.empty:
                    grouped = series.groupby(series[actual_date_col].dt.to_period("M").astype(str))[metric_column].sum()
                    charts.append({"title": f"{metric.replace('_',' ').title()} Trend Over Time", "type": "line", "data": grouped})
            continue

        if metric and dim_column is not None and metric_column is not None:
            metric_series = safe_numeric_conversion(data[metric_column])
            grouped = data.assign(__metric=metric_series).groupby(data[dim_column].fillna("Unknown"))["__metric"].sum().sort_values(ascending=False).head(10)
            if not grouped.empty:
                title = f"Top {len(grouped)} {dim.replace('_',' ').title()} by {metric.replace('_',' ').title()}"
                if dim == "location":
                    title = f"{metric.replace('_',' ').title()} by Location"
                elif dim == "channel":
                    title = f"{metric.replace('_',' ').title()} by Channel"
                elif dim == "product":
                    title = f"Top 10 Products by {metric.replace('_',' ').title()}"
                elif dim == "category":
                    title = f"{metric.replace('_',' ').title()} by Category"
                charts.append({"title": title, "type": "bar", "data": grouped})

    numeric_columns = []
    for column in data.columns:
        if pd.to_numeric(data[column], errors="coerce").notna().sum() > max(1, len(data) * 0.5):
            numeric_columns.append(column)

    if len(numeric_columns) >= 2:
        x_col = numeric_columns[0]
        y_col = numeric_columns[1]
        scatter_df = data[[x_col, y_col]].dropna()
        if not scatter_df.empty:
            charts.append({"title": f"{x_col} vs {y_col}", "type": "scatter", "data": scatter_df})

    if not charts:
        categorical_cols = [col for col in data.columns if col not in numeric_columns][:3]
        for col in categorical_cols:
            counts = data[col].dropna().value_counts().head(10)
            if not counts.empty:
                charts.append({"title": f"{col} Distribution", "type": "bar", "data": counts})

    return charts


def generate_business_insights(data, semantic_info):
    insights = []
    if data is None or data.empty:
        return insights

    category_column = resolve_metric_column(data, ["category", "product category", "type", "segment"])
    product_column = resolve_metric_column(data, ["product", "product name", "item", "sku"])
    location_column = resolve_metric_column(data, ["location", "city", "state", "country", "region", "area", "store"])
    channel_column = resolve_metric_column(data, ["channel", "sales channel", "platform", "source"])
    status_column = resolve_metric_column(data, ["status", "order status", "delivery status", "payment status", "fulfilment"])
    revenue_column = resolve_metric_column(data, ["revenue", "sales", "amount", "total sales", "total_amount", "turnover", "income", "gmv"])
    profit_column = resolve_metric_column(data, ["profit", "net profit", "gross profit", "earnings", "margin"])

    if category_column and revenue_column:
        cat_revenue = data[[category_column, revenue_column]].copy()
        cat_revenue[revenue_column] = safe_numeric_conversion(cat_revenue[revenue_column])
        top_category = cat_revenue.groupby(category_column)[revenue_column].sum().sort_values(ascending=False)
        if not top_category.empty:
            insights.append(f"{top_category.index[0]} generated the highest revenue.")

    if product_column and revenue_column:
        prod_revenue = data[[product_column, revenue_column]].copy()
        prod_revenue[revenue_column] = safe_numeric_conversion(prod_revenue[revenue_column])
        top_product = prod_revenue.groupby(product_column)[revenue_column].sum().sort_values(ascending=False)
        if not top_product.empty:
            insights.append(f"{top_product.index[0]} is the most frequently purchased product.")

    if channel_column and revenue_column:
        channel_revenue = data[[channel_column, revenue_column]].copy()
        channel_revenue[revenue_column] = safe_numeric_conversion(channel_revenue[revenue_column])
        top_channel = channel_revenue.groupby(channel_column)[revenue_column].sum().sort_values(ascending=False)
        if not top_channel.empty:
            insights.append(f"{top_channel.index[0]} contributes the largest share of revenue.")

    if status_column:
        status_counts = data[status_column].dropna().value_counts()
        if not status_counts.empty:
            insights.append(f"{status_counts.index[0]} is the most common order status.")

    if location_column and revenue_column:
        loc_revenue = data[[location_column, revenue_column]].copy()
        loc_revenue[revenue_column] = safe_numeric_conversion(loc_revenue[revenue_column])
        top_location = loc_revenue.groupby(location_column)[revenue_column].sum().sort_values(ascending=False)
        if not top_location.empty:
            insights.append(f"{top_location.index[0]} generated the strongest performance by location.")

    if profit_column and revenue_column:
        revenue_total = safe_numeric_conversion(data[revenue_column]).sum()
        profit_total = safe_numeric_conversion(data[profit_column]).sum()
        if revenue_total:
            margin = (profit_total / revenue_total) * 100
            insights.append(f"The current profit margin is {margin:.2f}%.")

    if not insights:
        insights.append("The uploaded dataset contains useful business information, but the available columns do not support a deeper automated insight yet.")

    return insights[:5]


def answer_business_question(question, data):
    normalized_question = question.strip().lower()
    if data is None or data.empty:
        return "There is no data available for the current selection."

    def get_column_aliases(*alias_groups):
        for group in alias_groups:
            for alias in group:
                found = resolve_metric_column(data, [alias])
                if found is not None:
                    return found
        return None

    total_sales_col = get_column_aliases(["sales", "revenue", "amount", "total sales", "turnover", "income", "gmv"])
    total_profit_col = get_column_aliases(["profit", "net profit", "gross profit", "earnings", "margin"])
    total_quantity_col = get_column_aliases(["quantity", "qty", "units", "units sold", "items", "count"])
    order_col = get_column_aliases(["order id", "order_id", "transaction id", "invoice", "order number", "orders"])
    category_col = get_column_aliases(["category", "product category", "type", "segment"])
    product_col = get_column_aliases(["product", "product name", "item", "sku"])
    customer_col = get_column_aliases(["customer", "customer name", "buyer", "client", "user"])
    location_col = get_column_aliases(["location", "city", "state", "country", "region", "area", "store"])
    channel_col = get_column_aliases(["channel", "sales channel", "platform", "source"])
    status_col = get_column_aliases(["status", "order status", "fulfilment", "delivery status", "payment status"])

    if "total revenue" in normalized_question or "total sales" in normalized_question or "revenue" in normalized_question and "what is" in normalized_question:
        if total_sales_col is None:
            return "I can't calculate total revenue because the uploaded dataset does not contain a revenue or sales-related column."
        total = safe_numeric_conversion(data[total_sales_col]).sum()
        return f"Total revenue for the uploaded dataset is **${total:,.2f}**."

    if "total profit" in normalized_question or "profit" in normalized_question and "what is" in normalized_question:
        if total_profit_col is None:
            return "I can't calculate profit because the uploaded dataset does not contain a profit-related column."
        total = safe_numeric_conversion(data[total_profit_col]).sum()
        return f"Total profit for the uploaded dataset is **${total:,.2f}**."

    if "total quantity" in normalized_question or "units sold" in normalized_question or "quantity sold" in normalized_question:
        if total_quantity_col is None:
            return "I can't calculate quantity because the uploaded dataset does not contain a quantity-related column."
        total = safe_numeric_conversion(data[total_quantity_col]).sum()
        return f"Total quantity for the uploaded dataset is **{total:,.0f}**."

    if "how many orders" in normalized_question or "order count" in normalized_question or "total orders" in normalized_question:
        if order_col is None:
            return "I can't answer that because the uploaded dataset does not contain an order or transaction identifier."
        count = data[order_col].nunique() if data[order_col].dtype == object else len(data)
        return f"There are **{count:,} orders** in the uploaded dataset."

    if "category" in normalized_question and "highest" in normalized_question:
        if category_col is None or total_sales_col is None:
            return "I can't determine the best category because the uploaded dataset does not contain a category and revenue/sales column."
        grouped = data[[category_col, total_sales_col]].copy()
        grouped[total_sales_col] = safe_numeric_conversion(grouped[total_sales_col])
        winner = grouped.groupby(category_col)[total_sales_col].sum().sort_values(ascending=False).idxmax()
        value = grouped.groupby(category_col)[total_sales_col].sum().sort_values(ascending=False).max()
        return f"{winner} has the highest sales with **${value:,.2f}**."

    if "product" in normalized_question and "highest" in normalized_question:
        if product_col is None or total_sales_col is None:
            return "I can't identify the top product because the uploaded dataset does not contain a product and revenue/sales column."
        grouped = data[[product_col, total_sales_col]].copy()
        grouped[total_sales_col] = safe_numeric_conversion(grouped[total_sales_col])
        winner = grouped.groupby(product_col)[total_sales_col].sum().sort_values(ascending=False).idxmax()
        value = grouped.groupby(product_col)[total_sales_col].sum().sort_values(ascending=False).max()
        return f"{winner} generated the highest sales with **${value:,.2f}**."

    if "which customer" in normalized_question and "highest" in normalized_question:
        if customer_col is None or total_sales_col is None:
            return "I can't determine the top customer because the uploaded dataset does not contain a customer and sales/revenue column."
        grouped = data[[customer_col, total_sales_col]].copy()
        grouped[total_sales_col] = safe_numeric_conversion(grouped[total_sales_col])
        winner = grouped.groupby(customer_col)[total_sales_col].sum().sort_values(ascending=False).idxmax()
        value = grouped.groupby(customer_col)[total_sales_col].sum().sort_values(ascending=False).max()
        return f"{winner} generated the highest sales with **${value:,.2f}**."

    if "average order value" in normalized_question or "aov" in normalized_question:
        if total_sales_col is None or order_col is None:
            return "I can't calculate average order value because the uploaded dataset does not contain both revenue/sales and order identifiers."
        sales_total = safe_numeric_conversion(data[total_sales_col]).sum()
        count = data[order_col].nunique() if data[order_col].dtype == object else len(data)
        if count == 0:
            return "I can't calculate average order value because there are no valid order identifiers in the uploaded dataset."
        aov = sales_total / count
        return f"The average order value is **${aov:,.2f}**."

    if "status" in normalized_question:
        if status_col is None:
            return "I can't answer that because the uploaded dataset does not contain a status column."
        status_counts = data[status_col].dropna().value_counts()
        if status_counts.empty:
            return "No order status data is available in the uploaded dataset."
        top_status = status_counts.idxmax()
        top_value = status_counts.max()
        return f"The most common status is **{top_status}** with **{top_value:,} records**."

    if "what is the total sales" in normalized_question or "what is the sales" in normalized_question:
        if total_sales_col is None:
            return "I can't calculate total sales because the uploaded dataset does not contain a sales or revenue-related column."
        total = safe_numeric_conversion(data[total_sales_col]).sum()
        return f"Total sales for the uploaded dataset are **${total:,.2f}**."

    return "I can answer questions about the metrics and dimensions available in the uploaded dataset, such as revenue, profit, quantity, orders, categories, products, customers, location, and status."


def prepare_uploaded_data(uploaded_file, manual_mapping=None):
    if uploaded_file is None:
        return None, [], {}, 0, 0, "Please upload a CSV file."

    try:
        file_bytes = uploaded_file.getvalue() if hasattr(uploaded_file, "getvalue") else uploaded_file
        uploaded_data = pd.read_csv(
            io.BytesIO(file_bytes),
            dtype=str,
            keep_default_na=True,
            na_values=["", " ", "NA", "N/A", "NULL", "null", "NaN", "nan"]
        )
    except Exception as error:
        return None, [], {}, 0, 0, f"Could not read the uploaded CSV: {error}"

    if uploaded_data.empty:
        return None, [], {}, 0, 0, "The uploaded CSV is empty."

    structure = detect_uploaded_business_structure(uploaded_data)
    mapping = structure["mapping"]
    preview = []
    for column in uploaded_data.columns:
        semantic = mapping.get(column, "Unclassified")
        if semantic == "Unclassified":
            status = "✕ Not detected"
        else:
            status = "✓ Automatically detected"
        preview.append({
            "Uploaded Column": column,
            "Detected Meaning": semantic,
            "Status": status
        })

    if not structure["is_business_like"]:
        summary = {
            "rows": len(uploaded_data),
            "columns": len(uploaded_data.columns),
            "detected_columns": [],
            "missing_values": int(uploaded_data.isnull().sum().sum()),
            "duplicate_rows": int(uploaded_data.duplicated().sum()),
            "column_names": list(uploaded_data.columns),
            "dataset_type": structure["dataset_type"],
            "confidence": structure["confidence"]
        }
        return (
            None,
            preview,
            summary,
            0,
            0,
            "This dataset does not appear to contain common business information. Please upload a business, sales, retail, transaction, customer, marketing, inventory or financial dataset."
        )

    cleaned_data = uploaded_data.copy()

    semantic_columns = structure["semantic_columns"]
    canonical_names = {
        "date": "date",
        "revenue": "revenue",
        "quantity": "quantity",
        "profit": "profit",
        "product": "product",
        "category": "category",
        "customer": "customer",
        "location": "location",
        "order": "order_id",
        "status": "status",
        "channel": "channel",
        "discount": "discount",
        "cost": "cost"
    }

    for semantic, columns in semantic_columns.items():
        if not columns:
            continue
        preferred = columns[0]
        if preferred in cleaned_data.columns:
            cleaned_data = cleaned_data.rename(columns={preferred: canonical_names.get(semantic, semantic)})

    for column in list(cleaned_data.columns):
        if column == "date":
            cleaned_data[column] = pd.to_datetime(cleaned_data[column], errors="coerce")
        if column in {"revenue", "profit", "quantity", "discount", "cost"}:
            cleaned_data[column] = safe_numeric_conversion(cleaned_data[column])

    cleaned_data = cleaned_data.drop_duplicates().copy()
    invalid_rows = int(cleaned_data.isna().all(axis=1).sum())
    cleaned_data = cleaned_data.loc[~cleaned_data.isna().all(axis=1)].copy()

    summary = {
        "rows": len(uploaded_data),
        "columns": len(uploaded_data.columns),
        "detected_columns": sorted(mapping.keys()),
        "missing_values": int(cleaned_data.isna().sum().sum()),
        "duplicate_rows": int(uploaded_data.duplicated().sum()),
        "column_names": list(uploaded_data.columns),
        "dataset_type": structure["dataset_type"],
        "confidence": structure["confidence"],
        "quality": measure_data_quality(cleaned_data)
    }

    return (
        cleaned_data,
        preview,
        summary,
        invalid_rows,
        int(uploaded_data.duplicated().sum()),
        None
    )


# ============================================================
# EMPTY FILTER CHECK
# ============================================================

if len(filtered_df) == 0 and page != "📂 Upload Business Data":

    st.warning(
        "No records found for the selected filters."
    )

    st.stop()


# ============================================================
# PAGE 1
# EXECUTIVE DASHBOARD
# ============================================================

if page == "📊 Executive Dashboard":

    render_page_header(
        "📊",
        "Executive Dashboard",
        "Interactive executive business analytics"
    )

    show_kpis(filtered_df)

    st.divider()

    # --------------------------------------------------------
    # YEARLY SALES
    # --------------------------------------------------------

    st.subheader(
        "📈 Yearly Sales Performance"
    )

    yearly_sales = (
        filtered_df
        .groupby("year")["sales"]
        .sum()
    )

    st.line_chart(
        yearly_sales
    )

    st.divider()

    col1, col2 = st.columns(2)

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    with col1:

        st.subheader(
            "📦 Category Sales & Profit"
        )

        category_data = (
            filtered_df
            .groupby("category")[
                ["sales", "profit"]
            ]
            .sum()
        )

        st.bar_chart(
            category_data
        )

    # --------------------------------------------------------
    # REGION
    # --------------------------------------------------------

    with col2:

        st.subheader(
            "🌍 Regional Profit"
        )

        region_profit = (
            filtered_df
            .groupby("region")["profit"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        st.bar_chart(
            region_profit
        )

    st.divider()

    # --------------------------------------------------------
    # TOP CUSTOMERS
    # --------------------------------------------------------

    st.subheader(
        "🏆 Top 10 Customers by Profit"
    )

    top_customers = (
        filtered_df
        .groupby("customer_name")["profit"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    st.bar_chart(
        top_customers
    )


# ============================================================
# PAGE 2
# SALES ANALYTICS
# ============================================================

elif page == "📈 Sales Analytics":

    render_page_header(
        "📈",
        "Sales Analytics",
        "Detailed sales, product and shipping analysis"
    )

    show_kpis(filtered_df)

    st.divider()

    # --------------------------------------------------------
    # MONTHLY SALES
    # --------------------------------------------------------

    st.subheader(
        "📅 Monthly Sales Trend"
    )

    monthly_sales = (
        filtered_df
        .groupby(
            filtered_df[
                "order_date"
            ].dt.to_period("M")
        )["sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["order_date"] = (
        monthly_sales["order_date"]
        .dt.to_timestamp()
    )

    monthly_sales[
        "3_Month_Moving_Average"
    ] = (
        monthly_sales["sales"]
        .rolling(
            window=3
        )
        .mean()
    )

    monthly_chart = (
        monthly_sales
        .set_index("order_date")[
            [
                "sales",
                "3_Month_Moving_Average"
            ]
        ]
    )

    st.line_chart(
        monthly_chart
    )

    st.divider()

    # --------------------------------------------------------
    # CATEGORY ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "📦 Category Analysis"
    )

    category_analysis = (
        filtered_df
        .groupby("category")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Total_Quantity=(
                "quantity",
                "sum"
            ),
            Total_Orders=(
                "order_id",
                "nunique"
            )
        )
    )

    category_analysis[
        "Profit_Margin_%"
    ] = (
        category_analysis[
            "Total_Profit"
        ]
        /
        category_analysis[
            "Total_Sales"
        ]
        * 100
    )

    category_analysis = (
        category_analysis
        .round(2)
        .sort_values(
            "Total_Sales",
            ascending=False
        )
    )

    st.dataframe(
        category_analysis,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # REGION ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "🌍 Region Analysis"
    )

    region_analysis = (
        filtered_df
        .groupby("region")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Total_Quantity=(
                "quantity",
                "sum"
            ),
            Total_Orders=(
                "order_id",
                "nunique"
            )
        )
    )

    region_analysis[
        "Profit_Margin_%"
    ] = (
        region_analysis[
            "Total_Profit"
        ]
        /
        region_analysis[
            "Total_Sales"
        ]
        * 100
    )

    st.dataframe(
        region_analysis
        .round(2)
        .sort_values(
            "Total_Profit",
            ascending=False
        ),
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # SHIPPING
    # --------------------------------------------------------

    st.subheader(
        "🚚 Shipping Mode Performance"
    )

    shipping_data = (
        filtered_df
        .groupby("ship_mode")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Average_Shipping_Days=(
                "shipping_days",
                "mean"
            ),
            Total_Orders=(
                "order_id",
                "nunique"
            )
        )
        .sort_values(
            "Total_Sales",
            ascending=False
        )
        .round(2)
    )

    st.dataframe(
        shipping_data,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # LOSS MAKING SUB-CATEGORIES
    # --------------------------------------------------------

    st.subheader(
        "⚠️ Loss-Making Sub-Categories"
    )

    subcategory_profit = (
        filtered_df
        .groupby("sub_category")[
            "profit"
        ]
        .sum()
        .sort_values()
    )

    loss_making = (
        subcategory_profit[
            subcategory_profit < 0
        ]
    )

    if len(loss_making) > 0:

        st.warning(
            f"{len(loss_making)} "
            "sub-category(s) are loss-making."
        )

        st.dataframe(
            loss_making.to_frame(
                "Total Profit"
            ),
            use_container_width=True
        )

    else:

        st.success(
            "No loss-making sub-category "
            "found for the selected filters."
        )


# ============================================================
# PAGE 3
# CUSTOMER INTELLIGENCE
# ============================================================

elif page == "👥 Customer Intelligence":

    render_page_header(
        "👥",
        "Customer Intelligence",
        "RFM segmentation, customer risk and clustering"
    )

    # ========================================================
    # RFM
    # ========================================================

    rfm_file = (
        "data/rfm_customer_segments.csv"
    )

    if os.path.exists(rfm_file):

        rfm_df = pd.read_csv(
            rfm_file
        )

        st.subheader(
            "🎯 RFM Customer Segmentation"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Customers",
            f"{len(rfm_df):,}"
        )

        champions = (
            rfm_df[
                rfm_df[
                    "Customer_Segment"
                ]
                == "Champions"
            ]
        )

        at_risk = (
            rfm_df[
                rfm_df[
                    "Customer_Segment"
                ]
                == "At Risk"
            ]
        )

        col2.metric(
            "🏆 Champions",
            f"{len(champions):,}"
        )

        col3.metric(
            "⚠️ At Risk",
            f"{len(at_risk):,}"
        )

        st.write(
            "### Customer Segment Distribution"
        )

        segment_counts = (
            rfm_df[
                "Customer_Segment"
            ]
            .value_counts()
        )

        st.bar_chart(
            segment_counts
        )

        selected_segment = st.selectbox(
            "Select Customer Segment",
            ["All"]
            +
            sorted(
                rfm_df[
                    "Customer_Segment"
                ].dropna().unique()
            )
        )

        if selected_segment == "All":

            rfm_display = rfm_df

        else:

            rfm_display = rfm_df[
                rfm_df[
                    "Customer_Segment"
                ]
                == selected_segment
            ]

        st.write(
            "### Customer Details"
        )

        rfm_columns = [
            "customer_name",
            "Recency",
            "Frequency",
            "Monetary",
            "RFM_Score",
            "Customer_Segment"
        ]

        available_rfm_columns = [
            col
            for col in rfm_columns
            if col in rfm_display.columns
        ]

        st.dataframe(
            rfm_display[
                available_rfm_columns
            ]
            .sort_values(
                "Monetary",
                ascending=False
            ),
            use_container_width=True
        )

    else:

        st.info(
            "RFM data not found."
        )

    st.divider()

    # ========================================================
    # CUSTOMER RISK
    # ========================================================

    risk_file = (
        "data/customer_risk_predictions.csv"
    )

    if os.path.exists(risk_file):

        risk_df = pd.read_csv(
            risk_file
        )

        st.subheader(
            "⚠️ Customer Risk Prediction"
        )

        high_risk = (
            risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == "High Risk"
            ].shape[0]
        )

        medium_risk = (
            risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == "Medium Risk"
            ].shape[0]
        )

        low_risk = (
            risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == "Low Risk"
            ].shape[0]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🔴 High Risk",
            f"{high_risk:,}"
        )

        col2.metric(
            "🟡 Medium Risk",
            f"{medium_risk:,}"
        )

        col3.metric(
            "🟢 Low Risk",
            f"{low_risk:,}"
        )

        risk_counts = (
            risk_df[
                "Predicted_Risk"
            ]
            .value_counts()
        )

        st.bar_chart(
            risk_counts
        )

        selected_risk = st.selectbox(
            "Filter Risk Level",
            [
                "All",
                "High Risk",
                "Medium Risk",
                "Low Risk"
            ]
        )

        if selected_risk == "All":

            risk_display = risk_df

        else:

            risk_display = risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == selected_risk
            ]

        risk_columns = [
            "customer_name",
            "Recency",
            "Frequency",
            "Monetary",
            "Customer_Segment",
            "Predicted_Risk"
        ]

        available_risk_columns = [
            col
            for col in risk_columns
            if col in risk_display.columns
        ]

        st.dataframe(
            risk_display[
                available_risk_columns
            ]
            .sort_values(
                "Monetary",
                ascending=False
            ),
            use_container_width=True
        )

    else:

        st.info(
            "Customer risk predictions not found."
        )

    st.divider()

    # ========================================================
    # CUSTOMER CLUSTERING
    # ========================================================

    cluster_file = (
        "data/customer_clusters.csv"
    )

    if os.path.exists(cluster_file):

        cluster_df = pd.read_csv(
            cluster_file
        )

        st.subheader(
            "🧠 Customer Clustering"
        )

        cluster_counts = (
            cluster_df[
                "Customer_Cluster"
            ]
            .value_counts()
            .sort_index()
        )

        st.bar_chart(
            cluster_counts
        )

        cluster_summary = (
            cluster_df
            .groupby(
                "Customer_Cluster"
            )
            .agg(
                Customers=(
                    "customer_name",
                    "count"
                ),
                Avg_Recency=(
                    "Recency",
                    "mean"
                ),
                Avg_Frequency=(
                    "Frequency",
                    "mean"
                ),
                Avg_Monetary=(
                    "Monetary",
                    "mean"
                )
            )
            .round(2)
        )

        st.write(
            "### Cluster Summary"
        )

        st.dataframe(
            cluster_summary,
            use_container_width=True
        )

        selected_cluster = st.selectbox(
            "Select Customer Cluster",
            [
                "All",
                0,
                1,
                2
            ]
        )

        if selected_cluster == "All":

            cluster_display = cluster_df

        else:

            cluster_display = cluster_df[
                cluster_df[
                    "Customer_Cluster"
                ]
                == selected_cluster
            ]

        cluster_columns = [
            "customer_name",
            "Recency",
            "Frequency",
            "Monetary",
            "Customer_Segment",
            "Customer_Cluster"
        ]

        available_cluster_columns = [
            col
            for col in cluster_columns
            if col in cluster_display.columns
        ]

        st.dataframe(
            cluster_display[
                available_cluster_columns
            ],
            use_container_width=True
        )

    else:

        st.info(
            "Customer clustering data not found."
        )


# ============================================================
# PAGE 4
# MACHINE LEARNING
# ============================================================

elif page == "🤖 ML Analytics":

    render_page_header(
        "🤖",
        "Machine Learning Analytics",
        "Predictive modelling and forecasting"
    )

    # ========================================================
    # SALES PREDICTION
    # ========================================================

    prediction_file = (
        "data/sales_predictions.csv"
    )

    st.subheader(
        "📈 Sales Prediction"
    )

    if os.path.exists(prediction_file):

        prediction_df = pd.read_csv(
            prediction_file
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "MAE",
            "85.38"
        )

        col2.metric(
            "RMSE",
            "251.88"
        )

        col3.metric(
            "R² Score",
            "0.7219"
        )

        st.info(
            "Model: Random Forest Regressor | "
            "Training: 2011–2013 | "
            "Testing: 2014"
        )

        st.write(
            "### Actual vs Predicted Sales"
        )

        if (
            "Actual_Sales" in prediction_df.columns
            and
            "Predicted_Sales" in prediction_df.columns
        ):

            st.scatter_chart(
                prediction_df,
                x="Actual_Sales",
                y="Predicted_Sales"
            )

        st.write(
            "### Prediction Sample"
        )

        st.dataframe(
            prediction_df.head(20),
            use_container_width=True
        )

    else:

        st.warning(
            "Sales prediction file not found."
        )

    st.divider()

    # ========================================================
    # SALES FORECAST
    # ========================================================

    forecast_file = (
        "data/sales_forecast.csv"
    )

    st.subheader(
        "🔮 Future Sales Forecast"
    )

    if os.path.exists(forecast_file):

        forecast_df = pd.read_csv(
            forecast_file
        )

        if "order_date" in forecast_df.columns:

            forecast_df[
                "order_date"
            ] = pd.to_datetime(
                forecast_df[
                    "order_date"
                ],
                errors="coerce"
            )

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        if (
            "order_date" in forecast_df.columns
            and
            "Forecasted_Sales" in forecast_df.columns
        ):

            st.line_chart(
                forecast_df.set_index(
                    "order_date"
                )[
                    "Forecasted_Sales"
                ]
            )

        st.caption(
            "Forecast generated by the sales forecasting module."
        )

    else:

        st.info(
            "Sales forecast file not found. "
            "Run sales_forecasting.py first."
        )


# ============================================================
# PAGE 5
# ANOMALY DETECTION
# ============================================================

elif page == "🚨 Anomaly Detection":

    render_page_header(
        "🚨",
        "Business Anomaly Detection",
        "Identify unusual discounts, shipping costs and transactions"
    )

    anomaly_file = (
        "data/anomalies.csv"
    )

    if os.path.exists(anomaly_file):

        anomaly_df = pd.read_csv(
            anomaly_file
        )

        total_anomalies = len(
            anomaly_df
        )

        discount_anomalies = 0

        shipping_anomalies = 0

        if "discount_anomaly" in anomaly_df.columns:

            discount_anomalies = int(
                anomaly_df[
                    "discount_anomaly"
                ].sum()
            )

        if "shipping_anomaly" in anomaly_df.columns:

            shipping_anomalies = int(
                anomaly_df[
                    "shipping_anomaly"
                ].sum()
            )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🚨 Anomalous Records",
            f"{total_anomalies:,}"
        )

        col2.metric(
            "🏷️ Discount Anomalies",
            f"{discount_anomalies:,}"
        )

        col3.metric(
            "🚚 Shipping Anomalies",
            f"{shipping_anomalies:,}"
        )

        st.divider()

        st.subheader(
            "🔎 Detected Anomalies"
        )

        available_columns = [
            col
            for col in [
                "order_id",
                "customer_name",
                "category",
                "sub_category",
                "sales",
                "discount",
                "profit",
                "shipping_cost",
                "anomaly_score"
            ]
            if col in anomaly_df.columns
        ]

        if "anomaly_score" in anomaly_df.columns:

            anomaly_display = (
                anomaly_df
                .sort_values(
                    "anomaly_score",
                    ascending=False
                )
            )

        else:

            anomaly_display = anomaly_df

        st.dataframe(
            anomaly_display[
                available_columns
            ],
            use_container_width=True
        )

        if "anomaly_score" in anomaly_df.columns:

            st.subheader(
                "🔥 Highest Priority Anomalies"
            )

            high_risk = anomaly_df[
                anomaly_df[
                    "anomaly_score"
                ] >= 2
            ]

            st.dataframe(
                high_risk[
                    [
                        col
                        for col in [
                            "order_id",
                            "category",
                            "sub_category",
                            "sales",
                            "discount",
                            "profit",
                            "shipping_cost",
                            "anomaly_score"
                        ]
                        if col in high_risk.columns
                    ]
                ].head(20),
                use_container_width=True
            )

    else:

        st.warning(
            "Anomaly data not found."
        )


# ============================================================
# PAGE 6
# BUSINESS INSIGHTS
# ============================================================

elif page == "💡 Business Insights":

    render_page_header(
        "💡",
        "Business Intelligence",
        "Data-driven business insights from the selected filters"
    )

    # --------------------------------------------------------
    # BEST CATEGORY
    # --------------------------------------------------------

    category_profit = (
        filtered_df
        .groupby("category")[
            "profit"
        ]
        .sum()
    )

    best_category = (
        category_profit
        .idxmax()
    )

    best_category_profit = (
        category_profit
        .max()
    )

    # --------------------------------------------------------
    # BEST REGION
    # --------------------------------------------------------

    region_profit = (
        filtered_df
        .groupby("region")[
            "profit"
        ]
        .sum()
    )

    best_region = (
        region_profit
        .idxmax()
    )

    best_region_profit = (
        region_profit
        .max()
    )

    # --------------------------------------------------------
    # BEST SHIPPING
    # --------------------------------------------------------

    shipping_sales = (
        filtered_df
        .groupby("ship_mode")[
            "sales"
        ]
        .sum()
    )

    best_shipping = (
        shipping_sales
        .idxmax()
    )

    # --------------------------------------------------------
    # LOSS MAKING
    # --------------------------------------------------------

    subcategory_profit = (
        filtered_df
        .groupby("sub_category")[
            "profit"
        ]
        .sum()
    )

    loss_making = (
        subcategory_profit[
            subcategory_profit < 0
        ]
        .sort_values()
    )

    # --------------------------------------------------------
    # INSIGHT CARDS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"🏆 Highest-profit category: "
            f"**{best_category}**"
        )

        st.write(
            f"Profit generated: "
            f"**${best_category_profit:,.2f}**"
        )

    with col2:

        st.info(
            f"🌍 Highest-profit region: "
            f"**{best_region}**"
        )

        st.write(
            f"Profit generated: "
            f"**${best_region_profit:,.2f}**"
        )

    st.divider()

    st.info(
        f"🚚 Highest-sales shipping mode: "
        f"**{best_shipping}**"
    )

    st.divider()

    # --------------------------------------------------------
    # LOSS MAKING PRODUCTS
    # --------------------------------------------------------

    st.subheader(
        "⚠️ Loss-Making Sub-Categories"
    )

    if len(loss_making) > 0:

        st.warning(
            f"{len(loss_making)} "
            "sub-category(s) are generating negative profit."
        )

        st.dataframe(
            loss_making.to_frame(
                "Total Profit"
            ),
            use_container_width=True
        )

    else:

        st.success(
            "No loss-making sub-category "
            "found for the selected filters."
        )

    st.divider()

    # --------------------------------------------------------
    # DISCOUNT ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "🏷️ Discount vs Profit"
    )

    discount_analysis = (
        filtered_df
        .groupby("discount")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Total_Quantity=(
                "quantity",
                "sum"
            )
        )
        .sort_index()
    )

    st.dataframe(
        discount_analysis.round(2),
        use_container_width=True
    )

    st.line_chart(
        discount_analysis[
            [
                "Total_Profit"
            ]
        ]
    )


# ============================================================
# PAGE 7
# DATA QUALITY
# ============================================================

elif page == "⚙️ Data Quality":

    render_page_header(
        "⚙️",
        "Data Quality & Validation",
        "Monitor dataset health before analytics and ML"
    )

    total_rows = len(df)

    total_columns = len(
        df.columns
    )

    missing_values = int(
        df.isnull()
        .sum()
        .sum()
    )

    duplicate_rows = int(
        df.duplicated()
        .sum()
    )

    total_cells = (
        total_rows
        *
        total_columns
    )

    if total_cells > 0:

        completeness = (
            1
            -
            (
                missing_values
                /
                total_cells
            )
        ) * 100

    else:

        completeness = 100

    if total_rows > 0:

        duplicate_percentage = (
            duplicate_rows
            /
            total_rows
        ) * 100

    else:

        duplicate_percentage = 0

    quality_score = max(
        0,
        completeness
        -
        duplicate_percentage
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📄 Records",
        f"{total_rows:,}"
    )

    col2.metric(
        "📋 Columns",
        f"{total_columns:,}"
    )

    col3.metric(
        "❌ Missing Values",
        f"{missing_values:,}"
    )

    col4.metric(
        "⭐ Quality Score",
        f"{quality_score:.2f}%"
    )

    st.divider()

    # --------------------------------------------------------
    # DUPLICATES
    # --------------------------------------------------------

    if duplicate_rows == 0:

        st.success(
            "✅ No duplicate rows detected."
        )

    else:

        st.warning(
            f"⚠️ {duplicate_rows:,} duplicate "
            "rows detected."
        )

    # --------------------------------------------------------
    # COLUMN QUALITY
    # --------------------------------------------------------

    st.subheader(
        "📋 Column-Level Data Quality"
    )

    quality_data = []

    for column in df.columns:

        quality_data.append(
            {
                "Column": column,
                "Data Type": str(
                    df[column].dtype
                ),
                "Missing Values": int(
                    df[column].isnull().sum()
                ),
                "Unique Values": int(
                    df[column].nunique()
                )
            }
        )

    quality_df = pd.DataFrame(
        quality_data
    )

    st.dataframe(
        quality_df,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # DATA PREVIEW
    # --------------------------------------------------------

    st.subheader(
        "👀 Dataset Preview"
    )

    rows_to_show = st.slider(
        "Rows to display",
        min_value=10,
        max_value=100,
        value=25
    )

    st.dataframe(
        df.head(rows_to_show),
        use_container_width=True
    )


# ============================================================
# PAGE 8
# AI BUSINESS ASSISTANT
# ============================================================

elif page == "🤖 AI Business Assistant":

    assistant_data = st.session_state.get(
        "uploaded_assistant_data",
        filtered_df
    )

    if assistant_data is None:
        assistant_data = filtered_df

    years_context = (
        "All Years"
        if len(selected_years) == len(years)
        else ", ".join(str(year) for year in selected_years)
    )
    categories_context = (
        "All Categories"
        if len(selected_categories) == len(categories)
        else ", ".join(selected_categories)
    )
    regions_context = (
        "All Regions"
        if len(selected_regions) == len(regions)
        else ", ".join(selected_regions)
    )

    if assistant_data is None or assistant_data.empty:
        assistant_order_count = 0
    else:
        assistant_order_count = assistant_data["order_id"].nunique() if "order_id" in assistant_data.columns else len(assistant_data)

    assistant_column, _ = st.columns([8, 1])

    with assistant_column:
        st.markdown(
            """
            <div class="ai-page-shell">
                <div class="ai-page-header">
                    <div class="ai-header-main">
                        <div class="ai-header-title">🤖 AI Business Assistant</div>
                        <div class="ai-header-subtitle">
                            Your intelligent assistant for business analytics and data-driven decisions.
                        </div>
                    </div>
                    <div class="ai-status">● AI ASSISTANT ONLINE</div>
                </div>
                <div class="ai-context-card">
                    <div class="ai-context-label">Current Data Context</div>
                    <div class="ai-context-value">
                        FILTERS: {years_context} &nbsp;•&nbsp; {categories_context} &nbsp;•&nbsp; {regions_context}
                        <br>
                        <span class="ai-context-count">{record_count:,} Records</span>
                        &nbsp;•&nbsp; {order_count:,} Orders
                    </div>
                </div>
            </div>
            """.format(
                years_context=years_context,
                categories_context=categories_context,
                regions_context=regions_context,
                record_count=len(assistant_data) if assistant_data is not None else 0,
                order_count=assistant_order_count
            ),
            unsafe_allow_html=True
        )

    if "business_assistant_messages" not in st.session_state:
        st.session_state.business_assistant_messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello. Ask me about sales, profit, orders, quantity, "
                    "profit margin, or category performance."
                )
            }
        ]

    with assistant_column:
        if len(st.session_state.business_assistant_messages) == 1:
            st.markdown(
                """
                <div class="ai-welcome-card">
                    <div class="ai-welcome-icon">🤖</div>
                    <div class="ai-welcome-title">AI Business Assistant</div>
                    <div class="ai-welcome-copy">
                        Ask questions about your sales, customers, profitability,
                        regions and business performance.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            '<div class="ai-section-label">Suggested Questions</div>',
            unsafe_allow_html=True
        )

        suggestions = [
            ("💰 Total Sales", "What is the total sales?"),
            ("📈 Total Profit", "What is the total profit?"),
            ("📦 Quantity Sold", "What is the total quantity sold?"),
            ("🛒 Order Count", "How many orders are there?"),
            ("📊 Profit Margin", "What is the profit margin?"),
            ("🏆 Best Category", "Which category has the highest profit?"),
            ("📦 Best Sales Category", "Which category has the highest sales?"),
            ("🌍 Best Profit Region", "Which region has the highest profit?"),
            ("🌍 Best Sales Region", "Which region has the highest sales?"),
            ("👥 Top Customers", "Who are the top 5 customers by profit?"),
            ("⚠️ Loss Categories", "Which sub-categories are loss-making?"),
            ("🚚 Best Shipping", "Which shipping mode has the highest sales?"),
            ("🏷️ Average Discount", "What is the average discount?")
        ]

        suggestion_columns = st.columns(4)
        selected_suggestion = None

        for index, (label, prompt) in enumerate(suggestions):
            with suggestion_columns[index % 4]:
                if st.button(label, key=f"assistant_suggestion_{index}", use_container_width=True):
                    selected_suggestion = prompt

        for message in st.session_state.business_assistant_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input(
            "Ask anything about your business data..."
        )

        question = question or selected_suggestion

    if question:
        answer = answer_business_question(
            question,
            assistant_data
        )

        st.session_state.business_assistant_messages.extend(
            [
                {
                    "role": "user",
                    "content": question
                },
                {
                    "role": "assistant",
                    "content": answer
                }
            ]
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            st.markdown(answer)


# ============================================================
# PAGE 9
# UPLOAD BUSINESS DATA
# ============================================================

elif page == "📂 Upload Business Data":

    render_page_header(
        "📂",
        "Upload Business Data",
        "Analyze your own sales data with the Smart Data Modernization platform"
    )

    st.markdown(
        """
        <div class="upload-intro">
            <div class="upload-intro-title">Bring your business data into the platform</div>
            <div class="upload-intro-copy">
                Upload a CSV containing your business sales data to analyze it using the
                Smart Data Modernization platform. The original uploaded file is never modified.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload your business CSV file",
        type=["csv"],
        key="business_data_uploader"
    )

    manual_mapping = st.session_state.get("uploaded_business_manual_mapping", {})

    if uploaded_file is not None:
        (
            prepared_data,
            mapping_preview,
            file_summary,
            invalid_row_count,
            duplicate_row_count,
            upload_error
        ) = prepare_uploaded_data(uploaded_file, manual_mapping=manual_mapping)

        st.session_state.uploaded_business_data = prepared_data
        st.session_state.uploaded_business_data_mapping = mapping_preview
        st.session_state.uploaded_business_data_summary = file_summary
        st.session_state.uploaded_business_data_error = upload_error
        st.session_state.uploaded_business_data_quality = (
            invalid_row_count,
            duplicate_row_count
        )
        if prepared_data is None:
            st.session_state.uploaded_assistant_data = None

    uploaded_data = st.session_state.get("uploaded_business_data")
    mapping_preview = st.session_state.get("uploaded_business_data_mapping", [])
    file_summary = st.session_state.get("uploaded_business_data_summary", {})
    upload_error = st.session_state.get("uploaded_business_data_error")
    invalid_row_count, duplicate_row_count = st.session_state.get(
        "uploaded_business_data_quality",
        (0, 0)
    )

    if uploaded_file is not None:
        validation_status = "Ready to analyze" if uploaded_data is not None and not uploaded_data.empty else "Waiting for valid dataset"
        st.markdown(
            f"<div class='upload-intro'><div class='upload-intro-title'>Validation status</div><div class='upload-intro-copy'>{validation_status}</div></div>",
            unsafe_allow_html=True
        )

    if upload_error:
        st.error(upload_error)
        st.markdown("### Supported business dataset examples")
        supported_examples = [
            "Date, Product, Category, Revenue, Profit",
            "Order ID, Date, Customer, Product, Quantity, Sales",
            "Region, Category, Sales, Discount, Profit"
        ]
        for example in supported_examples:
            st.write(f"• {example}")

    if uploaded_data is None:
        st.info(
            "No uploaded dataset is active. Your existing Superstore dashboard remains unchanged."
        )
    elif uploaded_data.empty:
        st.warning("No valid rows remain after cleaning the uploaded CSV.")
    else:
        total_rows = int(file_summary.get("rows", len(uploaded_data)))
        total_columns = int(file_summary.get("columns", len(uploaded_data.columns)))
        missing_values = int(file_summary.get("missing_values", uploaded_data.isnull().sum().sum()))
        duplicate_rows = int(file_summary.get("duplicate_rows", duplicate_row_count))
        detected_columns = list(file_summary.get("detected_columns", []))
        missing_attention = missing_values > max(25, total_rows * 0.05)

        st.markdown(
            """
            <div class="validation-banner">
                <div class="validation-banner-title">✓ Dataset validated successfully</div>
                <div class="validation-banner-subtitle">{rows:,} usable records</div>
            </div>
            """.format(rows=total_rows),
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="dataset-overview-card">
                <div class="dataset-overview-header">Dataset Overview</div>
                <div class="dataset-metric-grid">
                    <div class="dataset-metric-card healthy">
                        <div class="dataset-metric-label">Rows</div>
                        <div class="dataset-metric-value">{rows}</div>
                    </div>
                    <div class="dataset-metric-card healthy">
                        <div class="dataset-metric-label">Columns</div>
                        <div class="dataset-metric-value">{columns}</div>
                    </div>
                    <div class="dataset-metric-card {missing_class}">
                        <div class="dataset-metric-label">Missing Values</div>
                        <div class="dataset-metric-value">{missing}</div>
                        <div class="dataset-metric-footnote">{missing_note}</div>
                    </div>
                    <div class="dataset-metric-card {duplicate_class}">
                        <div class="dataset-metric-label">Duplicate Rows</div>
                        <div class="dataset-metric-value">{duplicates}</div>
                        <div class="dataset-metric-footnote">{duplicate_note}</div>
                    </div>
                </div>
            </div>
            """.format(
                rows=f"{total_rows:,}",
                columns=f"{total_columns:,}",
                missing=f"{missing_values:,}",
                duplicates=f"{duplicate_rows:,}",
                missing_class="warning" if missing_attention else "healthy",
                duplicate_class="healthy" if duplicate_rows == 0 else "warning",
                missing_note="Review recommended" if missing_attention else "Healthy range",
                duplicate_note="No duplicate rows" if duplicate_rows == 0 else "Needs review"
            ),
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="dataset-columns-card">
                <div class="dataset-columns-header">Detected Columns</div>
                <div class="dataset-column-pills">
                    {badges}
                </div>
            </div>
            """.format(
                badges="".join(
                    f"<span class='dataset-column-pill'>{value}</span>"
                    for value in (detected_columns or ["No detected columns"])
                )
            ),
            unsafe_allow_html=True
        )

        if invalid_row_count or duplicate_row_count:
            st.caption(
                f"Cleaning summary: {invalid_row_count:,} invalid rows handled, "
                f"{duplicate_row_count:,} duplicate rows removed."
            )

        if mapping_preview:
            mapping_df = pd.DataFrame(mapping_preview)
            st.markdown(
                "<div class='muted-caption'>Detailed mapping preview below for validation and manual review.</div>",
                unsafe_allow_html=True
            )
            st.dataframe(mapping_df, use_container_width=True)

            unresolved_columns = [
                row["Uploaded Column"]
                for row in mapping_preview
                if row["Status"] != "✓ Automatically detected"
            ]

            if unresolved_columns:
                st.markdown("### Manual Mapping Review")
                for column_name in unresolved_columns:
                    options = ["Not used"] + sorted(STANDARD_FIELD_ORDER)
                    current_index = options.index(
                        next(
                            (
                                row["Standard Field"]
                                for row in mapping_preview
                                if row["Uploaded Column"] == column_name
                            ),
                            "Not used"
                        )
                    ) if next(
                        (
                            row["Standard Field"]
                            for row in mapping_preview
                            if row["Uploaded Column"] == column_name
                        ),
                        ""
                    ) in options else 0
                    selected_field = st.selectbox(
                        f"Map '{column_name}' to a standard field",
                        options,
                        index=current_index,
                        key=f"manual_map_{column_name}"
                    )
                    if selected_field != "Not used":
                        manual_mapping[column_name] = selected_field
                st.session_state.uploaded_business_manual_mapping = manual_mapping

                if st.button("Apply Manual Mapping"):
                    if uploaded_file is not None:
                        (
                            prepared_data,
                            mapping_preview,
                            file_summary,
                            invalid_row_count,
                            duplicate_row_count,
                            upload_error
                        ) = prepare_uploaded_data(uploaded_file, manual_mapping=manual_mapping)

                        st.session_state.uploaded_business_data = prepared_data
                        st.session_state.uploaded_business_data_mapping = mapping_preview
                        st.session_state.uploaded_business_data_summary = file_summary
                        st.session_state.uploaded_business_data_error = upload_error
                        st.session_state.uploaded_business_data_quality = (
                            invalid_row_count,
                            duplicate_row_count
                        )
                        if prepared_data is None:
                            st.session_state.uploaded_assistant_data = None

        st.markdown("### Upload Analysis")
        if st.button("Analyze Uploaded Data"):
            st.success("Analysis started for the uploaded dataset.")

        if "sales" in uploaded_data.columns and "profit" in uploaded_data.columns:
            upload_total_sales = uploaded_data["sales"].sum()
            upload_total_profit = uploaded_data["profit"].sum()
        else:
            upload_total_sales = uploaded_data["sales"].sum() if "sales" in uploaded_data.columns else 0
            upload_total_profit = uploaded_data["profit"].sum() if "profit" in uploaded_data.columns else 0

        upload_total_orders = uploaded_data["order_id"].nunique() if "order_id" in uploaded_data.columns else len(uploaded_data)
        upload_total_quantity = uploaded_data["quantity"].sum() if "quantity" in uploaded_data.columns else 0
        upload_total_customers = uploaded_data["customer_name"].nunique() if "customer_name" in uploaded_data.columns else 0
        upload_profit_margin = (
            (upload_total_profit / upload_total_sales) * 100
            if upload_total_sales != 0
            else 0
        )

        st.markdown(
            '<div class="upload-section-title">📊 Uploaded Business Data Overview</div>',
            unsafe_allow_html=True
        )

        kpi_columns = st.columns(6)
        kpi_columns[0].metric("💰 Total Sales", f"${upload_total_sales:,.0f}")
        kpi_columns[1].metric("📈 Total Profit", f"${upload_total_profit:,.0f}")
        kpi_columns[2].metric("🛒 Orders", f"{upload_total_orders:,}")
        kpi_columns[3].metric("📦 Quantity", f"{upload_total_quantity:,.0f}")
        kpi_columns[4].metric("📊 Profit Margin", f"{upload_profit_margin:.2f}%")
        kpi_columns[5].metric("👥 Customers", f"{upload_total_customers:,}")

        st.markdown(
            '<div class="upload-section-title">📈 Dynamic Insights</div>',
            unsafe_allow_html=True
        )

        insight_blocks = []
        if "order_date" in uploaded_data.columns:
            trend_data = uploaded_data.assign(month=uploaded_data["order_date"].dt.to_period("M").astype(str)).groupby("month").agg(sales=("sales", "sum"))
            if not trend_data.empty:
                st.subheader("📅 Sales Trend Over Time")
                st.line_chart(trend_data)
        if "category" in uploaded_data.columns and "sales" in uploaded_data.columns:
            category_sales = uploaded_data.groupby("category")["sales"].sum().sort_values(ascending=False)
            if not category_sales.empty:
                st.subheader("📦 Sales by Category")
                st.bar_chart(category_sales)
        if "category" in uploaded_data.columns and "profit" in uploaded_data.columns:
            category_profit = uploaded_data.groupby("category")["profit"].sum().sort_values(ascending=False)
            if not category_profit.empty:
                st.subheader("📈 Profit by Category")
                st.bar_chart(category_profit)
        if "product_name" in uploaded_data.columns and "sales" in uploaded_data.columns:
            top_products = uploaded_data.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)
            if not top_products.empty:
                st.subheader("🏆 Top Products by Sales")
                st.bar_chart(top_products)
        if "customer_name" in uploaded_data.columns and "sales" in uploaded_data.columns:
            top_customers = uploaded_data.groupby("customer_name")["sales"].sum().sort_values(ascending=False).head(10)
            if not top_customers.empty:
                st.subheader("👥 Top Customers by Sales")
                st.bar_chart(top_customers)
        if "discount" in uploaded_data.columns and "profit" in uploaded_data.columns:
            discount_profit = uploaded_data[["discount", "profit"]].dropna()
            if not discount_profit.empty:
                st.subheader("💸 Discount vs Profit")
                st.scatter_chart(discount_profit)
        if "region" in uploaded_data.columns and "sales" in uploaded_data.columns:
            region_sales = uploaded_data.groupby("region")["sales"].sum().sort_values(ascending=False)
            if not region_sales.empty:
                st.subheader("🌍 Regional Sales")
                st.bar_chart(region_sales)

        if "category" in uploaded_data.columns and "profit" in uploaded_data.columns:
            best_category = uploaded_data.groupby("category")["profit"].sum().idxmax()
            st.caption(f"Best category by profit: {best_category}")

        uploaded_filtered_data = uploaded_data.copy()
        if "year" in uploaded_filtered_data.columns:
            uploaded_filtered_data = uploaded_filtered_data[uploaded_filtered_data["year"].notna()].copy()
        st.session_state.uploaded_assistant_data = uploaded_filtered_data


# ============================================================
# PREMIUM PRODUCT FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <div class="footer-grid">
            <div>
                <div class="footer-brand">📊 Smart Data Modernization</div>
                <div class="footer-text" style="margin-top:10px;">
                    An end-to-end analytics platform that converts business data into measurable insights,
                    customer intelligence, and predictive decisions.
                </div>
            </div>
            <div>
                <div class="footer-heading">Platform</div>
                <ul class="footer-list">
                    <li>Executive Analytics</li>
                    <li>Sales Intelligence</li>
                    <li>Customer Intelligence</li>
                    <li>ML & Forecasting</li>
                    <li>Anomaly Monitoring</li>
                    <li>Data Quality</li>
                </ul>
            </div>
            <div>
                <div class="footer-heading">Analytics</div>
                <ul class="footer-list">
                    <li>Revenue Analysis</li>
                    <li>Profit Analysis</li>
                    <li>Customer Segmentation</li>
                    <li>Risk Prediction</li>
                    <li>Sales Forecasting</li>
                    <li>Business Insights</li>
                </ul>
            </div>
            <div>
                <div class="footer-heading">Technology</div>
                <div>
                    <span class="footer-pill">Python</span>
                    <span class="footer-pill">Pandas</span>
                    <span class="footer-pill">Scikit-Learn</span>
                    <span class="footer-pill">Streamlit</span>
                    <span class="footer-pill">Machine Learning</span>
                    <span class="footer-pill">Data Analytics</span>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <span>© 2026 Smart Data Modernization</span>
            <span>Data → Insights → Intelligence → Decisions</span>
            <span>Enterprise Analytics Platform</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
