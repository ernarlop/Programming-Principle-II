import java.io.*;
import java.util.*;

public class C {
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
        int n = next(), m = next();
        int[] p = new int[n]; // p[i] — строка, на которой заканчивается блок i
        for (int i = 0; i < n; i++) p[i] = next() + (i > 0 ? p[i - 1] : 0);
        StringBuilder out = new StringBuilder();
        while (m-- > 0) {
            // первый блок, который заканчивается не раньше строки b
            out.append(lower(p, next()) + 1).append('\n');
        }
        System.out.print(out);
    }
}
