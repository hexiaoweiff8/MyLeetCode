
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # 输入：employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
        ret = 0
        id_map = {}
        for employee in employees:
            id_map[employee.id] = employee
        stack = [id]
        while stack:
            id = stack.pop()
            ret += id_map[id].importance
            for sub in id_map[id].subordinates:
                stack.append(sub)

        return ret


obj = Solution()
print(obj.getImportance(employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1))
