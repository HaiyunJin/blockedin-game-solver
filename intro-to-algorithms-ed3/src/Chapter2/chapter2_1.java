package Chapter2;

//import java.util.Arrays;

public class chapter2_1 {

		public static void main (String[] args) {
			System.out.println((int)(Math.random()*100));
			
//			Myarray myarray = new Myarray();
			int[] array = new int[]{77, 32, 2, 26, 22, 21, 87, 45, 91, 30, 92, 42};
			Myarray myarray = new Myarray(array);

			myarray.insertionSort();
			myarray.printOld();
			myarray.printSorted();
			
	/*				
		System.out.println(System.currentTim`eMillis());
		java.util.Date date = new java.util.Date();
		System.out.println("The elapsed time since Jan 1, 1970 is " +
				date.getTime() + " millseconds.");
		System.out.println(date.toString());
	*/	
		}
}

