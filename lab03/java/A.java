import java.io.*;
import java.util.*;

public class A {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = next();
        int x = next();
        // Arrays.binarySearch делит отрезок пополам; >= 0 значит «нашёл»
        System.out.println(Arrays.binarySearch(a, x) >= 0 ? "Yes" : "No");
    }
}
