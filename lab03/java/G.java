import java.io.*;
import java.util.*;

public class G {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next(), k = next();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = next();
        double lo = 0, hi = 1e9; // ищем максимальную длину
        for (int it = 0; it < 100; it++) {
            double x = (lo + hi) / 2;
            long pieces = 0;
            for (int v : a) pieces += (long) (v / x);
            if (pieces >= k) lo = x;
            else hi = x;
        }
        System.out.printf(Locale.US, "%.9f%n", lo);
    }
}
