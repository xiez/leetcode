class Solution {
    
    class Tuple {
        int idx;
        char c;
        public Tuple(int idx, char c) {
            this.idx = idx;
            this.c = c;
        }
    }
    
    public String predictPartyVictory(String senate) {
        LinkedList<Tuple> r_lst = new LinkedList<>();
        LinkedList<Tuple> d_lst = new LinkedList<>();
        int n = senate.length();
        
        for (int i = 0; i < senate.length(); i++) {
            if (senate.charAt(i) == 'R') {
                r_lst.addLast(new Tuple(i, 'R'));
            } else {
                d_lst.addLast(new Tuple(i, 'D'));
            }
        }

        while (r_lst.size() > 0 && d_lst.size() > 0) {
            Tuple r = r_lst.get(0);
            Tuple d = d_lst.get(0);
            if (r.idx < d.idx) {
                r.idx += n;
                r_lst.addLast(r);
            } else {
                d.idx += n;
                d_lst.addLast(d);
            }
            r_lst.removeFirst();
            d_lst.removeFirst();
        }
        
        if (r_lst.size() > 0) {
            return "Radiant";
        }
        return "Dire";
    }
}
