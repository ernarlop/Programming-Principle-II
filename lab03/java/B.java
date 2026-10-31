import java.io.*;
import java.util.*;

public class B {
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

    // сколько элементов в отрезке [l, r]
    static int cnt(int[] a, int l, int r) {
        if (l > r) return 0;
        return lower(a, r + 1) - lower(a, l);
    }

    public static void main(String[] args) throws IOException {
        int n = next(), q = next();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = next();
        Arrays.sort(a);
        StringBuilder out = new StringBuilder();
        while (q-- > 0) {
            int l1 = next(), r1 = next(), l2 = next(), r2 = next();
            // |A ∪ B| = |A| + |B| - |A ∩ B|
            out.append(cnt(a, l1, r1) + cnt(a, l2, r2) - cnt(a, Math.max(l1, l2), Math.min(r1, r2))).append('\n');
        }
        System.out.print(out);
    }
}
