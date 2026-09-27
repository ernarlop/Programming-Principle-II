import java.io.*;
import java.util.*;

public class J {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next(), k = next();
        int[] need = new int[n]; // сторона квадрата, нужная для i-й овцы
        for (int i = 0; i < n; i++) {
            int x1 = next(), y1 = next(), x2 = next(), y2 = next();
            need[i] = Math.max(x2, y2);
        }
        Arrays.sort(need);
        System.out.println(need[k - 1]); // k-я по величине — минимальная сторона для k овец
    }
}
