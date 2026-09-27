import java.io.*;
import java.util.*;

public class K {
    static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        int t = next();
        int[] q = new int[t];
        for (int i = 0; i < t; i++) q[i] = next();
        int n = next(), m = next();
        HashMap<Integer, String> pos = new HashMap<>(); // значение -> "строка столбец"
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) pos.put(next(), i + " " + j);
        StringBuilder out = new StringBuilder();
        for (int v : q) out.append(pos.getOrDefault(v, "-1")).append('\n');
        System.out.print(out);
    }
}
