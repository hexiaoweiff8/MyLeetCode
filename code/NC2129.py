class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        return ' '.join([word.capitalize() if len(word) > 2 else word.lower() for word in title.split(' ')])
