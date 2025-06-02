
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

def foo():
    folder = '/home/pbrian/projects'
    folders = [os.path.join(folder,f) for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
    
    html = '<table>'
     
    for folder in folders:
        _, paths = analyse_repo(folder)
        if paths:
            path = paths[0]
            with open(path) as fo:
                txt = fo.read()
            html += f'<tr><td>{folder}</td><td>{txt[:100]}</td></tr>'
    with open("/home/pbrian/foo.html", 'w') as fo:
        fo.write(html+"</table>")
    import webbrowser
    webbrowser.open('/home/pbrian/foo.html')



if __name__ == '__main__':
    foo()