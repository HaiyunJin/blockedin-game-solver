package Chapter2;

import java.util.Arrays;


public class Myarray{
	// Length of the array
	int length;
	public int[] myarray;
	public int[] sortarray;
	
	// if no array are given, randomly generate one.
	Myarray() {
		int n = (int)(Math.random()* 100);
		length =n;
		System.out.println("length "+length);
        myarray = new int[n];	
		for ( int i =0 ; i < n ; i++ ){
			myarray[i] = (int)(Math.random()*100);
		}
		System.out.println(Arrays.toString(myarray));
		System.out.println("Construct: "+myarray.length);
	}
	// or, use the user's array
	Myarray(int[] newarray){
		myarray = Arrays.copyOf(newarray, newarray.length);
		System.out.println(Arrays.toString(myarray));
	}

	void printOld(){
		System.out.println("Old Array: "+Arrays.toString(myarray));
	}
	
	void printSorted(){
		System.out.println("Sort Array:"+Arrays.toString(sortarray));
	}

//	int[] insertionSort(){
	void insertionSort(){
		System.out.println("lenght of array: "+myarray.length);
		if  (myarray.length > 1){
			int key;
			int j;
			sortarray = Arrays.copyOf(myarray, myarray.length);
			for (int i = 1; i < sortarray.length; i++) {
				key = sortarray[i];
				j = i - 1;
				while (j>=0 && sortarray[j] > key ){
					sortarray[j+1] = sortarray[j];
					j = j - 1;
				}
				sortarray[j+1] = key;
			}	
		}
	}
	
	
	
}
