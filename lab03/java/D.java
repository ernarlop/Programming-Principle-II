import java.io.*;
import java.util.*;

public class D {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    // первый индекс i, где a[i] >= x (как lower_bound в C++)
    static int lower(int[] a, int x) {
        int l = 0, r = a.length;
        while (l < r) {
            int m = (l + r) / 2;
            if (a[m] < x) l = m + 1;
            else r = m;
        }
        return l;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = next();
        Arrays.sort(a);
        long[] s = new long[n + 1]; // s[i] — сумма первых i сил
        for (int i = 0; i < n; i++) s[i + 1] = s[i] + a[i];
        int q = next();
        StringBuilder out = new StringBuilder();
        while (q-- > 0) {
            int k = lower(a, next() + 1); // сколько сил <= p
            out.append(k).append(' ').append(s[k]).append('\n');
        }
        System.out.print(out);
    }
}
