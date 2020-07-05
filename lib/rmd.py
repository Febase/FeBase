import re


class Rmd:
    def __init__(self, readme):
        self.readme = readme
        self.toc_reg = re.compile(
            r"<!\-\- toc starts \-\->.*<!\-\- toc ends \-\->", re.DOTALL)
        self.toc = ["<!-- toc starts -->"]

    def update_toc(self, header, url):
        print(header)
        # row = "* [{title}]({url}) - {date}".format()
        # self.toc.append(row)

    def rewrite(self):
        readme_contents = self.readme.open().read()
        self.toc.append("<!-- toc ends -->")
        toc_converted = "\n".join(self.toc).strip()
        self.readme.open('w').write(self.toc_reg.sub(
            toc_converted, readme_contents))
