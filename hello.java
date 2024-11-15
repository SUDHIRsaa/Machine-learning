public class hello{
    public static void main(String[] args) {
        int x=-123;
        String s=String.valueOf(x);
       char c[]=s.toCharArray();
       int start=0;
       int end=c.length-1;
       int[] intArray = new int[c.length];
       for (int i = 0; i < c.length; i++) {
        // Convert each character to integer
        intArray[i] = Character.getNumericValue(c[i]);
    }
       while(start<end){
        
        int  temp = intArray[start];
        intArray[start] = intArray[end];
        intArray[end] = temp;

        // Move pointers
        start++;
        end--;
       }
       for (int i = 0; i < intArray.length; i++) {
        System.out.println(intArray[i]);
       }
    }
}