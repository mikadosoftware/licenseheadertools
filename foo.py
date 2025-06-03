
import os

def walk_tree(fldr, extlist):
    """Given fldr, walk the tree and return all files as abspaths """
    outfiles = []
    for root, dirs, files in os.walk(fldr):
        if ".git" in dirs: dirs.remove(".git")
        fileshere = [os.path.join(root, f) for f in
                     files if os.path.splitext(f)[-1:][0] in extlist]
        outfiles.extend(fileshere)
    return outfiles

def analyse_repo(folder):
    extlist = ['.py', '.rst']
    repofiles = walk_tree(folder, extlist)
    readme = [f for f in repofiles if 'README' in f]
    return (folder, readme)

def extract_tokens(text):
    """ We have oneline comments in files like 
    
    .. onelinedesc: foobar
    .. somethingelse: foobar

    get foobar
    """
    found = {}
    tokens = ['onelinedesc']
    for line in text.split('\n'):
        line = line.strip()
        for token in tokens:
            tokenplus = f'.. {token}:'
            if line.startswith(tokenplus):
                found['token']= line
    return found


def foo():
    folder = '/home/pbrian/projects'
    folders = [os.path.join(folder,f) for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
    folders = [f for f in folders if 'mikado' in f]    
    html = '<table>'
     
    for folder in folders:
        _, paths = analyse_repo(folder)
        if paths:
            path = paths[0]
            with open(path) as fo:
                txt = fo.read()
                results = extract_tokens(txt)

            html += f'<tr><td>{folder}</td><td>{results}</td></tr>'
    with open("/home/pbrian/foo.html", 'w') as fo:
        fo.write(html+"</table>")
    import webbrowser
    webbrowser.open('/home/pbrian/foo.html')



if __name__ == '__main__':
    foo()