import dns.resolver

def check_dkim(domain):
    try:
        dkim_records = dns.resolver.resolve(f'_adsp._domainkey.{domain}', 'TXT')
        for record in dkim_records:
            print(f'DKIM Record: {record}')

    except dns.resolver.NXDOMAIN:
        print(f'DKIM Record not found for {domain}')

    except dns.resolver.NoAnswer:
        print(f'No DKIM Record found for {domain}')

def check_dmarc(domain):
    try:
        dmarc_records = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
        for record in dmarc_records:
            print(f'DMARC Record: {record}')

    except dns.resolver.NXDOMAIN:
        print(f'DMARC Record not found for {domain}')

    except dns.resolver.NoAnswer:
        print(f'No DMARC Record found for {domain}')

if __name__ == "__main__":
    domain_to_check = input("Digite o domínio para verificar DKIM e DMARC: ")
    check_dkim(domain_to_check)
    check_dmarc(domain_to_check)
