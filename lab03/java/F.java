import java.io.*;
import java.util.*;

public class F {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next(), h = next();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = next();
        long lo = 1, hi = 1_000_000_000; // ищем минимальное K
        while (lo < hi) {
            long k = (lo + hi) / 2, hours = 0;
            for (int v : a) hours += (v + k - 1) / k; // деление с округлением вверх
            if (hours <= h) hi = k;
            else lo = k + 1;
        }
        System.out.println(lo);
    }
}
