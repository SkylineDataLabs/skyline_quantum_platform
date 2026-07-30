from pathlib import Path

import streamlit as st

from core.tls_scanner import scan_tls
from core.risk_engine import calculate_risk
from reports.pdf_generator import create_pdf_report


# Browser-tab and page settings
st.set_page_config(
    page_title="Skyline Quantum Platform",
    page_icon="🛡️",
    layout="wide",
)


# Page heading
st.title("Skyline Quantum Platform")
st.subheader("Cybersecurity Assessment Platform")

st.write(
    "Enter a company domain to generate a professional cybersecurity "
    "assessment and downloadable PDF report."
)

st.caption(
    "TLS configuration • SSL certificates • Risk scoring • Professional PDF reporting"
)


# Domain input
domain = st.text_input(
    "Company or Domain",
    placeholder="e.g. playstation.com",
).strip()


# Generate assessment
if st.button("Generate Report", type="primary"):
    if not domain:
        st.warning("Please enter a company domain before generating a report.")

    else:
        try:
            with st.spinner(f"Analyzing {domain}..."):
                scan_results = scan_tls(domain)
                risk_results = calculate_risk(scan_results)

                pdf_path = create_pdf_report(
                    domain,
                    scan_results,
                    risk_results,
                )

            st.success("Assessment complete. Your PDF report is ready.")

            st.subheader("Assessment Results")

            if isinstance(risk_results, dict):
                st.json(risk_results)
            else:
                st.write(risk_results)

            pdf_file = Path(pdf_path)

            if pdf_file.exists():
                st.download_button(
                    label="Download PDF Report",
                    data=pdf_file.read_bytes(),
                    file_name=pdf_file.name,
                    mime="application/pdf",
                    type="primary",
                )
            else:
                st.error(
                    "The assessment completed, but the generated PDF could not be found."
                )

        except Exception as error:
            st.error(f"The assessment could not be completed: {error}")


# Disclaimer
st.divider()

st.caption(
    "Quantum analyzes publicly available information only. "
    "It does not perform intrusive testing or attempt to exploit vulnerabilities."
)