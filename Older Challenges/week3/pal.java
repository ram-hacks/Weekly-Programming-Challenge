/**
 * @Tim Leonard
 * 
 * A Palindrome solution in Java
 */

import java.util.ArrayList;
import javax.swing.JOptionPane;


public class Main {
	
	public static void main(String args[]) {
		
		String inputValue = JOptionPane.showInputDialog("Please input some characters");
		
		ArrayList<Character> list = new ArrayList<Character>();
		for(char c : inputValue.toCharArray()) {
		    list.add(c);
		}
		
		Pal pal = new Pal(list);
	
		for(int i =0; i<list.size();i++)
			System.out.print(list.get(i));	
	}
		
}


class Pal {
	
	public Pal(ArrayList<Character> l) {		
		
		System.out.println(palindrome(l,0));

	}

	private boolean palindrome(ArrayList<Character> l, int i) {
		
		int index = i;
		
		if (i<l.size()/2){
				
			if (palindrome(l,++i))
		
				return l.get(l.size()-index-1).equals(l.get(index));
		
			else
			
				return false;
		}
		
		else
			
			return true;
					
	}
	
}
