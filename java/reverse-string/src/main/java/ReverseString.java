class ReverseString {
    /**
     * The reverse string
     * 
     * Reversing a string using StringBuilder class
     * 
     * @param inputString string to reverse
     * @return reverse string
     */
    String reverse(String inputString) {
        StringBuilder reversed_string = new StringBuilder(inputString);
        reversed_string.reverse();
        return reversed_string.toString();
        // return new StringBuilder(inputString).reverse().toString();
        // one line solution
    }

}
