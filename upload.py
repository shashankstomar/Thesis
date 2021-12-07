import base64
from github import Github
from github import InputGitTreeElement
g=Github("shshankstomar","S.040690204@s")
g = Github("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")

file_list = [
    'checkpoint_50000.zip'
]
file_names = [
   'checkpoint_50000.zip'
]
commit_message = 'python commit'
master_ref = repo.get_git_ref('heads/main')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

element_list = list()
for i, entry in enumerate(file_list):
    data = base64.b64encode(open("checkpoint_50000.zip", "rb").read())
    #data = input_file.read()
    # if entry.endswith('.png'): # images must be encoded
    #     data = base64.b64encode(data)
    element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    element_list.append(element)

tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)