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
        ArrayList<Tuple> r_lst = new ArrayList<>();
        ArrayList<Tuple> d_lst = new ArrayList<>();
        int n = senate.length();
        
        for (int i = 0; i < senate.length(); i++) {
            if (senate.charAt(i) == 'R') {
                r_lst.add(new Tuple(i, 'R'));
            } else {
                d_lst.add(new Tuple(i, 'D'));
            }
        }

        while (r_lst.size() > 0 && d_lst.size() > 0) {
            Tuple r = r_lst.get(0);
            Tuple d = d_lst.get(0);
            if (r.idx < d.idx) {
                r.idx += n;
                r_lst.add(r);
            } else {
                d.idx += n;
                d_lst.add(d);
            }
            r_lst.remove(0);
            d_lst.remove(0);
        }
        
        if (r_lst.size() > 0) {
            return "Radiant";
        }
        return "Dire";
    }
}
