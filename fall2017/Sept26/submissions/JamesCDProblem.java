
package cdsellers;

import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.stream.IntStream;

/**
 * @author James
 * @version 0.1
 */
public class CDSellers {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanThis = new Scanner(System.in);
        String[] info = scanThis.nextLine().split("\\s+");
        int cdsToSell = 0;
        int[] cdInfo = new int[10000];
            for(int counter=0;counter<Integer.parseInt(info[0])+Integer.parseInt(info[1]);counter++){
                int someInt = Integer.parseInt(scanThis.next());
                if(cdInfo!=null&&IntStream.of(cdInfo).anyMatch(num->num==someInt)){
                    cdsToSell++;
                }
                cdInfo[counter]=someInt;
            }
            System.out.println(cdsToSell+"");
    }
    
}
