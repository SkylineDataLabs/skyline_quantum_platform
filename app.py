import streamlit as st
from core.tls_scanner import scan_tls
from core.risk_engine import calculate_risk
from reports.pdf_generator import create_pdf_report



st.set_page_config(
    page_title="Skyline Quantum Platform",
    page_icon="🛡️",
    layout="wide"
)

st.title("Skyline Quantum Platform")
st.subheader("Post-Quantum Cryptography Readiness Scanner")

st.write("Platform initialized successfully.")

domain = st.text_input("Enter a domain to scan")

if st.button("Run Scan"):

    if domain:

        try:
            results = scan_tls(domain)

            st.success(f"Scan completed for {domain}")

            risk_data = calculate_risk(results)

            score = risk_data["risk_score"]

            if score >= 70:
                risk_label = "High Risk"
            elif score >= 30:
                risk_label = "Moderate Risk"
            else:
                risk_label = "Low Risk"

            st.metric("Quantum Risk Score", f"{score}/100", risk_label)
            st.subheader("Findings")

            for finding in risk_data["findings"]:
                st.warning(finding)

            st.subheader("Raw TLS Data")

            st.json(results)
            pdf_file = create_pdf_report(
                domain=domain,
                risk_score=score,
                findings=risk_data["findings"],
                tls_results=results
            )

            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="Download PDF Report",
                    data=file,
                    file_name=pdf_file,
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"Scan failed: {e}")