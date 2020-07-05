import re
import os.path
from datetime import datetime


class Rmd:
    def __init__(self, readme):
        self.readme = readme
        self.toc_reg = re.compile(
            r"<!\-\- toc starts \-\->.*<!\-\- toc ends \-\->", re.DOTALL)
        self.toc = ["<!-- toc starts -->"]

    def set_default_value(self, header, path):
        new_header = header.copy()
        if header['title'] == '':
            new_header['title'] = path
        if header['date'] == '':
            new_header['date'] = datetime.today().strftime('%Y-%m-%d')

        return new_header.copy()

    def get_toc_row(self, toc):
        header_raw = toc['header']
        header = self.set_default_value(header_raw, toc['path'])
        date_matched = re.search(
            r"([0-9]{4}\-[0-9]{2}\-[0-9]{2})", header['date'])
        date = date_matched.group() if date_matched else ""
        row = "* [{title}]({url}) - {date}".format(
            title=header['title'],
            url=toc['url'],
            date=date)
        return row

    def update_toc(self, toc_data):
        for category in toc_data.keys():
            self.toc.append("### {}\n".format(category))
            toc_list = sorted(toc_data[category],
                              key=lambda toc: toc['header']['date'], reverse=True)
            for toc in toc_list:
                row = self.get_toc_row(toc)
                self.toc.append(row)

    def rewrite(self):
        readme_contents = self.readme.open().read()
        self.toc.append("<!-- toc ends -->")
        toc_converted = "\n".join(self.toc).strip()
        self.readme.open('w').write(self.toc_reg.sub(
            toc_converted, readme_contents))
