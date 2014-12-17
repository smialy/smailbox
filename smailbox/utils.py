import email.header

def decode_header(header):
    def decode_part(value, encoding):
        if isinstance(value, str):
            return value
        if isinstance(value, bytes):
            if encoding == 'unknown-8bit':
                return value.decode('utf-8', 'replace')
            try:
                if encoding is None:
                    return value.decode()                   
                return value.decode(encoding)
            except LookupError:
                return value.decode()
        return str(value)
   
    return ''.join([decode_part(value, encoding) for value, encoding in email.header.decode_header(header)])
