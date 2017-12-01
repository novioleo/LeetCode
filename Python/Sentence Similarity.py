# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.
#
# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        else:
            my_pairs = dict()
            for m_pairs in pairs:
                if m_pairs[0] not in my_pairs:
                    my_pairs[m_pairs[0]] = set()
                my_pairs[m_pairs[0]].add(m_pairs[1])
            for i in range(len(words1)):
                word1 = words1[i]
                word2 = words2[i]
                if word1 != word2:
                    if not ((word1 in my_pairs and word2 in my_pairs[word1]) or
                                 (word2 in my_pairs and word1 in my_pairs[word2])):
                        return False
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.areSentencesSimilar(["great","acting","skills"],["fine","drama","talent"],[["great","fine"],["drama","acting"],["skills","talent"]]))