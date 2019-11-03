
from collections import deque, defaultdict

# O(K * N^2) time complexity where N = len(A) and K = len(A[0])
# This should be good enough in real interview but stupid leetcode somehow TLE

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0

        A = list(set(A))
        wordToSimilars = defaultdict(set)
        for i in xrange(len(A)):
            word1 = A[i]
            for j in xrange(len(A)):
                if i == j:
                    continue
                word2 = A[j]
                if self.isSimilar(word1, word2):
                    wordToSimilars[word1].add(word2)
                    wordToSimilars[word2].add(word1)
            # we need it because later if word not in wordToSimilars we don't do BFS
            if word1 not in wordToSimilars:
                wordToSimilars[word1] = set()

        ans = 0
        # BFS
        for word in A:
            # this word has been BFS'ed to
            if word not in wordToSimilars:
                continue
            self.bfs(word, wordToSimilars)
            ans += 1

        return ans

    def bfs(self, startWord, wordToSimilars):
        queue = deque()
        queue.append(startWord)
        while queue:
            word = queue.popleft()
            if word not in wordToSimilars:
                continue
            for similarWord in wordToSimilars[word]:
                queue.append(similarWord)
                wordToSimilars[similarWord].discard(word)
                if not wordToSimilars[similarWord]:
                    del wordToSimilars[similarWord]
            del wordToSimilars[word]

    def isSimilar(self, word1, word2):
        diffCount = 0
        for i in xrange(len(word1)):
            if word1[i] != word2[i]:
                diffCount += 1
        return diffCount == 2



print Solution().numSimilarGroups(["tars", "rats", "arts", "star"])



'''
import java.util.*;

class Solution {
    public int numSimilarGroups(String[] A) {
        if (A == null || A.length == 0) {
            return 0;
        }
        
        Set<String> aSet = new HashSet<>();
        for (String a : A) {
            aSet.add(a);
        }
        String[] array = new String[aSet.size()];
        int index = 0;
        for (String a : aSet) 
            array[index++] = a;
        
        Map<String, Set<String>> wordToSimilars = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            String word1 = array[i];
            wordToSimilars.put(word1, new HashSet<>());
            for (int j = 0; j < array.length; j++) {
                if (i == j) {
                    continue;
                }
                String word2 = array[j];
                if (!wordToSimilars.containsKey(word2)) {
                    wordToSimilars.put(word2, new HashSet<>());
                }
                if (isSimilar(word1, word2)) {
                    wordToSimilars.get(word1).add(word2);
                    wordToSimilars.get(word2).add(word1);
                }
            }
        }
        
        int ans = 0;
        for (String word : array) {
            if (!wordToSimilars.containsKey(word)) {
                continue;
            }
            bfs(word, wordToSimilars);
            ans++;
        }
        
        return ans;
    }
    
    public void bfs(String startWord, Map<String, Set<String>> wordToSimilars) {
        Queue<String> queue = new LinkedList<>();
        queue.add(startWord);
        while (queue.size() > 0) {
            String word = queue.poll();
            if (!wordToSimilars.containsKey(word)) {
                continue;
            }
            for (String similarWord : wordToSimilars.get(word)) {
                queue.add(similarWord);
                wordToSimilars.get(similarWord).remove(word);
                if (wordToSimilars.get(similarWord).size() == 0) {
                    wordToSimilars.remove(similarWord);
                }
                wordToSimilars.remove(word);
            }
        }
    }
    
    public boolean isSimilar(String word1, String word2) {
        int diffCount = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                diffCount++;   
            }
        }
        return diffCount == 2;
    }    
}
'''
