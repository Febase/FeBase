class Header:
    def __init__(self, fp):
        self.fp = fp
        self.header = {
            'count': 0,
            'data': {}
        }

    def update_data(self, key, value):
        header_data = self.header['data']
        header_data[key] = value
        self.header['count'] -= 1

    def read_line(self, read_state):
        line = self.fp.readline().strip()
        if ('---' in line):
            return 'ended' if self.header['count'] == 0 else 'reading'
        if (':' in line) and (read_state == 'reading'):
            key, value = line.split(':', 1)
            parsed_key = key.strip()
            parsed_value = value.strip()
            if parsed_key not in self.header['data']:
                return 'reading'
            self.update_data(parsed_key, parsed_value)
            return 'reading'
        return 'pending'

    def set_header(self, header_list):
        self.header['data'] = dict.fromkeys(header_list, '')
        self.header['count'] = len(header_list)
        read_count = 3
        read_state = 'pending'
        while read_state != 'ended':
            read_state = self.read_line(read_state)
            if read_state == "pending":
                read_count -= 1
            if read_count == 0:
                return

    def get_header(self):
        return self.header['data'].copy()
