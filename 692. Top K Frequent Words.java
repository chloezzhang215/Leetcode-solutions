class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> mapping = new HashMap<>();
        for (String word: words){
            if ( !mapping.containsKey(word)){
                mapping.put(word,0);
            }
            int count = mapping.get(word) + 1;
            mapping.put(word,count);
        }
        PriorityQueue<String> pq = new PriorityQueue<>(
            (w1,w2) -> mapping.get(w1).equals(mapping.get(w2)) ? w2.compareTo(w1): mapping.get(w1) -mapping.get(w2)
        );

        for(String word: mapping.keySet()){
            pq.add(word);
            if(pq.size()>k){
                pq.poll();
            }
        }

        List<String> res = new ArrayList<>();
        while (! pq.isEmpty()){
            res.add(pq.poll());
        }

        Collections.reverse(res);
        return res;

    }
}
