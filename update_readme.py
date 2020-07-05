import pathlib
from lib.header import Header
from lib.rmd import Rmd
from lib.logger import Logger
from lib.gitlog import Gitlog

root_path = pathlib.Path(__file__).parent.resolve()


def start_update(logger):
    md_paths = root_path.glob('*/*.md')
    gitlog = Gitlog(root_path)
    for file_path in md_paths:
        fp = file_path.open()
        header = Header(fp)
        header.set_header(['title', 'author', 'date', 'category'])
        header_data = header.get_header()
        path = str(file_path.relative_to(root_path))
        url = "https://github.com/Febase/FeBase/blob/mater/{}".format(path)
        logger.update(header_data, url, path)
        gitlog.check_status()
    logger.save(log_path)


def rewrite_readme(logger):
    readme = root_path / 'README.md'
    rmd = Rmd(readme)
    # rmd.update_toc()
    rmd.rewrite()


if __name__ == "__main__":
    log_path = root_path / '.log/readme_log.json'
    logger = Logger()
    logger.load(log_path)
    start_update(logger)
    rewrite_readme(logger)
