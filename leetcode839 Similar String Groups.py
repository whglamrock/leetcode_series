
from collections import deque, defaultdict

# O(K * N^2) time complexity where N = len(A) and K = len(A[0])
# This should be good enough in real interview but stupid leetcode somehow TLE
# P.S., it's essential to remember to model this as an undirected graph

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
            w1 = A[i]
            for j in xrange(len(A)):
                if i == j:
                    continue
                w2 = A[j]
                if self.isSimilar(w1, w2):
                    wordToSimilars[w1].add(w2)
                    wordToSimilars[w2].add(w1)

        group = 0
        visited = set()
        for word in A:
            if word not in visited:
                group += 1
                self.bfs(word, wordToSimilars, visited)

        return group

    def bfs(self, startWord, wordToSimilars, visited):
        q = deque()
        q.append(startWord)

        while q:
            word = q.popleft()
            if word in visited:
                continue
            visited.add(word)
            for similar in wordToSimilars[word]:
                if similar not in visited:
                    q.append(similar)

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
        Set<String> visited = new HashSet<>();
        for (String word : array) {
            if (!visited.contains(word)) {
                bfs(word, wordToSimilars, visited);
                ans++;
            }
        }
        
        return ans;
    }
    
    public void bfs(String startWord, Map<String, Set<String>> wordToSimilars, Set<String> visited) {
        Queue<String> queue = new LinkedList<>();
        queue.add(startWord);
        
        while (queue.size() > 0) {
            String word = queue.poll();
            if (visited.contains(word)) {
                continue;
            }
            visited.add(word);
            for (String similarWord : wordToSimilars.get(word)) {
                if (!visited.contains(similarWord)) {
                    queue.add(similarWord);
                }
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
