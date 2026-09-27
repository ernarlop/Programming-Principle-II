import java.io.*;
import java.util.*;

public class I {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next(), k = next();
        int[] a = new int[n];
        long lo = 0, hi = 0;
        for (int i = 0; i < n; i++) {
            a[i] = next();
            lo = Math.max(lo, a[i]); // ответ не меньше самого большого дома
            hi += a[i];              // и не больше суммы всех
        }
        while (lo < hi) {
            long x = (lo + hi) / 2, cur = 0;
            int blocks = 1;
            for (int v : a) { // жадно набиваем блоки, пока сумма <= x
                if (cur + v > x) { blocks++; cur = 0; }
                cur += v;
            }
            if (blocks <= k) hi = x;
            else lo = x + 1;
        }
        System.out.println(lo);
    }
}
