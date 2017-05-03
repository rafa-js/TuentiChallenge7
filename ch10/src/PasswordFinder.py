import os
import subprocess


class PasswordFinder:
    REPO_PATH = '/Users/rafa0809/Desktop/repo/'


    def __init__(self, commits_file):
        self.commitsByDate = {}
        inputFile = open(commits_file, mode='r')
        line = inputFile.readline()
        while line:
            date, commit = line.split(':')
            self.commitsByDate[date] = commit
            line = inputFile.readline()
        inputFile.close()


    def find_password_for_user(self, user: str, history: str) -> str:
        password, hash = '', ''
        for date, times in history:
            commit = self.commitsByDate[date]
            secret1, secret2 = self.get_secrets(commit)
            for i in range(times):
                password, hash = self.generate_password(user, hash, secret1, secret2)
        return password


    def generate_password(self, user: str, hash: str, secret1: str, secret2: str):
        pr = subprocess.Popen(f"php fast_script.php {secret1} {secret2} {user} {hash}",
                              cwd=os.path.dirname(self.REPO_PATH),
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = pr.communicate()
        pr.kill()
        if len(error) > 0:
            raise Exception(f'Error performing script.php command: {error}')
        content = out[:-1].decode("utf-8")
        return content.split(' ')


    def get_secrets(self, commit):
        pr = subprocess.Popen(f"/usr/bin/git show {commit}",
                              cwd=os.path.dirname(self.REPO_PATH),
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = pr.communicate()
        if len(error) > 0:
            raise Exception(f'Error performing git command: {error}')
        content = str(out)
        pr.kill()

        # First matching with 'secretX = ' if first commit. Second matching otherwise
        start_index1 = content.find("secret1 = ")
        second_start_index1 = content.find("secret1 = ", start_index1 + 2)
        start_index1 = start_index1 if second_start_index1 == -1 else second_start_index1

        start_index2 = content.find("secret2 = ")
        second_start_index2 = content.find("secret2 = ", start_index2 + 2)
        start_index2 = start_index2 if second_start_index2 == -1 else second_start_index2

        secret1 = content[start_index1 + 10:start_index1 + 17]
        secret2 = content[start_index2 + 10:start_index2 + 17]
        return secret1, secret2
