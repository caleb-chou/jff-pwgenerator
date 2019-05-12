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
        generate(len);

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
}