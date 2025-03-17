class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 预处理好词
        good_word = set(positive_feedback)
        # 预处理坏词
        bad_word = set(negative_feedback)
        ret_array = []
        for index, one_report in enumerate(report):
            report_array = one_report.split(" ")
            score = 0
            for word in report_array:
                if word in good_word:
                    score += 3
                elif word in bad_word:
                    score -= 1
            ret_array.append((score, student_id[index]))
        ret_array.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        return [x[1] for x in ret_array[:k]]


obj = Solution()
print(obj.topStudents(positive_feedback=["smart", "brilliant", "studious"], negative_feedback=["not"],
                      report=["this student is studious", "the student is smart"], student_id=[1, 2], k=2))
