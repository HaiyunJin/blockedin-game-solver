package Chapter2;

public class chapter2_3 {
	
	private boolean x;
	
	public static void main (String[] args) {
	chapter2_3 foo = new chapter2_3();
	System.out.println(foo.x);
	
	System.out.println(System.currentTimeMillis());
	
	java.util.Date date = new java.util.Date();
	System.out.println("The elapsed time since Jan 1, 1970 is " +
			date.getTime() + " millseconds.");
	System.out.println(date.toString());
	
}
}