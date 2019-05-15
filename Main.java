import java.util.*;
class Main {
  
}
class Password {
    private ArrayList<char[]> char_set = new ArrayList<char[]>();

    private String lower = "abcdefghijklmnopqrstuvwxyz";
    private String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private String nums  = "0123456789";
    private String special="!@#$%^&*()-=_+;':\"[]{},./<>?\\";

    private String password = "";

    Password(boolean u, boolean n, boolean s, int len) {
        char_set.add(lower.toCharArray());
        if(u) char_set.add(upper.toCharArray());
        if(n) char_set.add(nums.toCharArray());
        if(s) char_set.add(special.toCharArray());
        generate_V2(len);

    }
    private int random_num(int range) {
        return (int) (Math.random() * range);
    }

    public String toString() {
        return password;
    }
    
    private void generate(int len) {
        int i = 0;
        while( i++ < len ) {
          int cat = random_num(char_set.size());
          this.password += "" + this.char_set.get(cat)[random_num(this.char_set.get(cat).length)];
        }
    }
    private void generate_v2(int len) {
        int size = char_set.size();
        double [] weights = new double[size];
        int i = 0;
        for( ; i < weights.length; i++) weights[i] = (double)(1/(double)char_set.size());
        i = 0;
        double selected;
        int sc;
        while( i < len ) {
          sc = 0;
          selected = Math.random();
          double temp = 0;
          for(double d : weights) {
            temp+=d;
            if(!(selected <= temp)) {
              sc++;
              continue;
            }
            this.password += "" + this.char_set.get(sc)[random_num(this.char_set.get(sc).length)];
            for(int j = 0; j < weights.length; j++) {
              double val = (double) ( 1 / (double) (len-this.password.length()));
              if(j == sc) weights[j] -= val;
              else weights[j] += val/(double) 3;
            }
            break;
          }
          i++;
        }
        System.out.println();
      }
}