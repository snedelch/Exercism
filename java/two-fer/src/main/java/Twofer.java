public class Twofer {

    /**
     * Two-fer or 2-fer is short for two for one. One for you and one for me.
     * 
     * Method that will take change string by using replace() method
     * 
     * @param name thr name of the person to be replaced in "One for {you}, one for
     *             me"
     * @return a string representation "One for {name}, one for me"
     */
    public String twofer(String name) {
        String two_fer = "One for you, one for me.";
        if (name != null) {
            String two_fer_with_name = two_fer.replace("you", name);
            return two_fer_with_name;
        } else {
            return two_fer;
        }
        // return String.format("One for %s, one for me.", name == null ? "you" : name);
        // shorter vertion credit to badsys's solution
        // added if statement at the end

    }
}
