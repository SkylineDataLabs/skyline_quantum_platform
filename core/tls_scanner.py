import ssl
import socket


def scan_tls(domain):
    context = ssl.create_default_context()

    with socket.create_connection((domain, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            cert = ssock.getpeercert()

            cipher = ssock.cipher()

            return {
                "domain": domain,
                "cipher": cipher[0],
                "tls_version": cipher[1],
                "key_bits": cipher[2],
                "issuer": dict(x[0] for x in cert['issuer']),
                "subject": dict(x[0] for x in cert['subject']),
            }