import git

# ’A’ for added paths
# ’D’ for deleted paths
# ’R’ for renamed paths
# ’M’ for paths with modified data
# ’T’ for changed in the type paths


class Gitlog:
    def __init__(self, repo, ref="master"):
        self.repo = repo
        self.ref = ref

    def check_status(self):
        repo = git.Repo(self.repo, odbt=git.GitDB)
        for item in repo.index.diff(None):
            a_path = item.a_path
            b_path = item.b_path
            print(a_path + "->" + b_path)
        # commits = reversed(list(repo.iter_commits(ref)))
        # for commit in commits:
        #     affected_files = list(commit.stats.files)
        #     print(affected_files)
