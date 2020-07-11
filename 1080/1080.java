import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = 0;
        int n = scan.nextInt();
        int m = scan.nextInt();
        char[][] matA = new char[n][m];
        boolean[][] check = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            matA[i] = scan.next().toCharArray();
        }
        for (int i = 0; i < n; i++) {
            char[] matB = scan.next().toCharArray();
            for(int j = 0; j < m; j++) {
                if(matB[j] != matA[i][j]) {
                    check[i][j] = true;
                    count++;
                }
            }
        }

        if(count == 0)
            System.out.println(count);
        else
            System.out.println(howChange(check));
    }

    static int howChange(boolean mat[][]) {
        int change = 0;
        int n = mat.length;
        int m = mat[0].length;

        if(n < 3 || m < 3)
            return -1;

        for(int i = 0; i <= n - 3; i++) {
            for(int j = 0; j <= m - 3; j++) {
                if(i == n -3 && !(mat[i][j] == mat[i+1][j] && mat[i][j] == mat[i+2][j])) {
                    return -1;
                }
                if(j == m - 3 && !(mat[i][j] == mat[i][j+1] && mat[i][j] == mat[i][j+2])) {
                    return -1;
                }
                if(mat[i][j] == true) {
                    for (int x = i; x < i + 3; x++) {
                        for (int y = j; y < j + 3; y++) {
                            mat[x][y] = !mat[x][y];
                        }
                    }
                    change++;
                }
            }
        }
        
        boolean last = mat[n-3][m-3];
        for(int i = n - 2; i < n ;i++) {
            for(int j = m -2; j < m ;j++) {
                if(last != mat[i][j])
                    return -1;
            }
        }
        return change;
    }
}
