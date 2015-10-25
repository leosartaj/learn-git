from urlparse import urlparse

lines = []
with open('AUTHORS.md') as f:
    for l in f:
        lines.append(l)


def check_url(url, user):
    url = urlparse(url)
    path = '/' + user
    return ((url[0] == 'http' or url[0] == 'https') and
            (url[1] == 'www.github.com' or url[1] == 'github.com') and
            url[2] == path and url[3:] == ('', '', ''))


def test_authors():
    prev = 'a'
    for line in lines:
        l = line.split()
        assert l[0] == '*'
        name = (' '.join(l[1:-1])).lower()
        assert name >= prev
        username, link = l[-1].split(']')
        assert username[0] == '['
        assert link[0] == '('
        assert link[-1] == ')'
        assert check_url(link[1:-1], username[1:])
