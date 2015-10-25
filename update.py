with open('header.md') as f:
    readme = f.read()
with open('AUTHORS.md') as f:
    readme += f.read()
with open('footer.md') as f:
    readme += f.read()


with open('README.md', 'w') as f:
    f.write(readme)
