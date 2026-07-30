def calculate_risk(results):

    risk_score = 0
    findings = []

    cipher = results.get("cipher", "")
    key_bits = results.get("key_bits", 0)

    if "RSA" in cipher:
        risk_score += 40
        findings.append("RSA encryption detected — vulnerable to future quantum attacks.")

    if key_bits < 256:
        risk_score += 20
        findings.append("Weak key length detected.")

    if "TLSv1.2" in results.get("tls_version", ""):
        risk_score += 10
        findings.append("Older TLS version detected.")

    if risk_score == 0:
        findings.append("No major immediate quantum-related risks detected.")

    return {
        "risk_score": risk_score,
        "findings": findings
    }