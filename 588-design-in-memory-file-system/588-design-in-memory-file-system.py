class PathNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        
        
class FileNode:
    def __init__(self, name, content):
        self.name = name
        self.content = content

        

class FileSystem:

    def __init__(self):
        self.root = PathNode(name='root')
        
    def ls(self, path: str) -> List[str]:
        pathNodes = path.split('/')[1:]
        currentNode = self.root
        
        for node in pathNodes:
            if node == '':
                continue
            currentNode = currentNode.children[node]
        

        if type(currentNode) is PathNode:
            return sorted(currentNode.children.keys())
        
        else:
            # Path is a file
            return [currentNode.name]

    def mkdir(self, path: str) -> None:
        pathNodes = path.split('/')[1:]
        currentNode = self.root
        
        for path in pathNodes:
            if path not in currentNode.children:
                currentNode.children[path] = PathNode(path)
            currentNode = currentNode.children[path]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        directoryNodes = filePath.split('/')[1:]
        filename = directoryNodes[-1]
        currentNode = self.root
        
        for node in directoryNodes[:-1]:
            currentNode = currentNode.children[node]
            
        if filename in currentNode.children:
            currentNode.children[filename].content += content
        
        else:
            currentNode.children[filename] = FileNode(filename, content)
                    

    def readContentFromFile(self, filePath: str) -> str:
        nodes = filePath.split('/')[1:]
        currentNode = self.root
        
        for node in nodes:
            currentNode = currentNode.children[node]
            
        return currentNode.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)