class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        for i in range(len(sandwiches)):
            if sandwiches[i] in students:
                students.remove(sandwiches[i])
            else:
                return len(students)
        return 0