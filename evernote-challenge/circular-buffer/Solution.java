import java.util.Scanner;

class Solution {
    static String[] buf;
    static int last = -1;
    static int first = 0;
    static int len;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input; int i;
        len = sc.nextInt();
        sc.nextLine();
        buf = new String[len];
        while (true) {
            input = sc.nextLine();
            switch (input.charAt(0)) {
            case 'A':
                i = Integer.parseInt(input.substring(2));
                while (i-- != 0) {
                    last = (last + 1) % len;
                    if (buf[last] != null) {
                        first = (first + 1) % len;
                    }
                    buf[last] = sc.nextLine();
                }
                break;
            case 'R':
                i = Integer.parseInt(input.substring(2));
                while (i-- != 0) {
                    buf[first] = null;
                    first = (first + 1) % len;
                }
                break;
            case 'L':
                i = first;
                while (i != last) {
                    System.out.println(buf[i]);
                    i = (i + 1) % len;
                }
                System.out.println(buf[i]);
                break;
            case 'Q':
                System.exit(0);
                break;
            }
        }
    }
}
