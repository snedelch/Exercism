public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven() {
        return 40;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int min) {
        int min_left = expectedMinutesInOven() - min;
        return min_left;
    }

    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layers) {
        int min_to_cook = layers * 2;
        return min_to_cook;
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layers, int min_cooked) {
        int total_time_cooked = preparationTimeInMinutes(layers) + min_cooked;
        return total_time_cooked;
    }
}
