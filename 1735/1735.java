import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a1 = scan.nextInt();
        int a2 = scan.nextInt();
        int b1 = scan.nextInt();
        int b2 = scan.nextInt();
        int gcd = getGcd(a2,b2);

        int denomin = getLcm(gcd,a2,b2);
        int numerator = (a1 * (b2 / gcd)) + (b1 * (a2 / gcd));

        int irredu = getGcd(denomin,numerator);

        if(irredu != 1) {
            denomin /= irredu;
            numerator /= irredu;
        }
        System.out.println(numerator + " " + denomin);
    }
    public static int getGcd(int x, int y) {
        if(x < y) {
            int temp = x;
            x = y;
            y = temp;
        }
        while(y != 0) {
            int n = x % y;
            x = y;
            y = n;
        }
        return x;
    }
    public static int getLcm(int gcd, int x, int y) {
        return gcd * (x /  gcd) * (y / gcd);
    }
}
