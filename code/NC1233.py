class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folderDic = {}
        ret = []
        folder.sort()
        for item in folder:
            if not self.checkAndSaveFolder(item, folderDic):
                ret.append(item)

        return ret

    def checkAndSaveFolder(self, folder, folderDic):
        """
        :param folder:
        :param folderDic:
        :return:
        """
        dic = folderDic
        folderArray = folder.split("/")
        lenArray = len(folderArray)
        isSub = False
        isPreLeaf = False
        for index in range(lenArray):
            oneFolder = folderArray[index]
            nextDic = dic.get(oneFolder, None)
            if nextDic:
                dic = nextDic
                if not isPreLeaf:
                    isPreLeaf = nextDic.get("isLeaf", False)
            else:
                isSub = True
                nextDic = {}
                dic[oneFolder] = nextDic
                dic = nextDic

            if lenArray - 1 == index:
                nextDic["isLeaf"] = True
        return isSub and isPreLeaf


obj = Solution()
print(obj.removeSubfolders(["/ah/al/am","/ah/al"]))
