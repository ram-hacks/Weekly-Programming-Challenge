package fizzbuzz;

import java.util.stream.IntStream;

/**
 * @author James Clinton
 * @version 0.1
 */
public class FizzBuzz {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        IntStream.range(1,50).mapToObj(num->num%5==0&&num%3==0?"RAMHacks":num%3==0?"RAM":num%5==0?"Hacks":num).forEach(System.out::println);
    }
}
