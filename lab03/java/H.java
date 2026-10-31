import java.io.*;
import java.util.*;

public class H {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next(), k = next();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = next();
        // два указателя: окно [l, r], все числа неотрицательные
        long sum = 0;
        int ans = n, l = 0;
        for (int r = 0; r < n; r++) {
            sum += a[r];
            while (l <= r && sum >= k) {
                ans = Math.min(ans, r - l + 1);
                sum -= a[l++];
            }
        }
        System.out.println(ans);
    }
}
