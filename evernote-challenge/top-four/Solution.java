import java.util.Scanner;
import java.util.ArrayList;

class Solution {
    static ArrayList<Integer> topFour = new ArrayList<Integer>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int x;
        for (int i = 0; i < n; i++) {
            x = sc.nextInt();
            for (int j = 0; j < 4; j++) {
                if (j < topFour.size()) {
                    if (x >= topFour.get(j)) {
                        topFour.add(j, x);
                        if (topFour.size() > 4) {
                            topFour.remove(4);
                        }
                        break;
                    }
                } else {
                    topFour.add(x);
                    break;
                }
            }
        }
        for (Integer s : topFour) {
            if (s != null) {
                System.out.println(s);
            }
        }
    }
}
