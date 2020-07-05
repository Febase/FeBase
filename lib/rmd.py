import re


class Rmd:
    def __init__(self, readme):
        self.readme = readme
        self.toc_reg = re.compile(
            r"<!\-\- toc starts \-\->.*<!\-\- toc ends \-\->", re.DOTALL)
        self.toc = ["<!-- toc starts -->"]

    def get_toc_row(self, toc):
        header = toc['header']
        date = re.search(r"([0-9]{4}\-[0-9]{2}\-[0-9]{2})", header['date'])
        row = "* [{title}]({url}) - {date}".format(
            title=header['title'],
            url=toc['url'],
            date=date.group()
        )
        return row

    def update_toc(self, toc_data):
        for category in toc_data.keys():
            self.toc.append("## {}\n".format(category))
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
