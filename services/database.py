import streamlit as st
from supabase import create_client

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

def save_report(
    company_name,
    status,
    risk_score=None,
    report_filename=None,
    error_message=None,
    processing_seconds=None,
):
    report_data = {
        "company_name": company_name,
        "status": status,
        "risk_score": risk_score,
        "report_filename": report_filename,
        "error_message": error_message,
        "processing_seconds": processing_seconds,
    }

    response = supabase.table("reports").insert(report_data).execute()
    return response