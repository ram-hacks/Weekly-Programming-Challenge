import java.util.*;
import java.io.*;

public class dict {

    /**
     * A list of valid words
     */
    static ArrayDeque<String> dictionary = new ArrayDeque<String>();

    /**
     * Pass two words as command-line arguments
     */
    public static void main(String[] args) {
        String a = args[0];
        String b = args[1];
        
        System.out.println(a + " -> " + b);

        // Load the dictionary
        try {
            loadWords();
        } catch (Exception e) { 
            System.out.println("Failure loading dictionary");
            return;
        }

        ArrayDeque<String> path = transform(a, b);
        if (path == null)
            System.out.println("No path");
        else 
            for (String p : path) 
                System.out.println(p);
    }

    /**
     * Returns a list of all words that are one character away from the given string
     */
    public static ArrayDeque<String> getNeighbors(String w) {
        ArrayDeque<String> n = new ArrayDeque<String>();
        for (int i = 0; i < w.length(); i++) {
            for (int c = 'a'; c <= 'z'; c++) {
                String x = w.substring(0,i) + (char)c + w.substring(i+1, w.length());
                if (isWord(x) && !x.equals(w)) 
                    n.add(x);
            }
        }
        return n;
    }

    /**
     * Gives an optimal path between two given strings using only single letter changes
     */
    public static ArrayDeque<String> transform(String w1, String w2) {
        // If lengths of words do not match, there is no path
        if (w1.length() != w2.length()) 
            return null;

        // If either word isn't in the dictionary, we don't know how to handle it
        if (!isWord(w1) || !isWord(w2)) 
            return null;

        // We will have a set of paths
        ArrayDeque<ArrayDeque<String>> paths = new ArrayDeque<ArrayDeque<String>>();
        
        // And a list of words already seen (to avoid circuits)
        ArrayDeque<String> visited = new ArrayDeque<String>();
        
        // Add the first word to a path, and add that path to our set
        ArrayDeque<String> p1 = new ArrayDeque<String>();
        p1.add(w1);
        paths.add(p1);
     
        // Breadth-first search
        while (!paths.isEmpty()) {
            ArrayDeque<String> curr_path = paths.removeFirst();
            String curr_word = curr_path.peekLast();

            // If we've found the word, this is an optimal path. Return it.
            if (curr_word.equals(w2))
                return curr_path;
            
            // Record the word
            visited.add(curr_word);

            // Go through every possible next node
            for (String n : getNeighbors(curr_word)) {
                // If we've already seen this word, ignore it
                if (visited.contains(n))
                    continue;
                else {
                    // Add this new path
                    ArrayDeque<String> new_path = curr_path.clone();
                    new_path.add(n);
                    paths.add(new_path);
                }
            }
        }
        return null;
    }
    
    /**
     * Returns true if the given word is in the dictionary
     */
    public static boolean isWord(String w) {
        return dictionary.contains(w);
    }

    /**
     * Load a dictionary of valid words
     */
    public static void loadWords() throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("dictionary.txt"));
        try {
            String line = br.readLine();
            while (line != null) {
                dictionary.add(line);
                line = br.readLine();
            }
        } finally {
            br.close();
        }
    }
}
