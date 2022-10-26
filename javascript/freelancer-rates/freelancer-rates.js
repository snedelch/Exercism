// @ts-check
//
// ☝🏽 The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion on the web
// and supported IDEs when implementing this exercise. You don't need to
// understand types, JSDoc, or TypeScript in order to complete this JavaScript
// exercise, and can completely ignore this comment block and directive.

// 👋🏽 Hi again!
//
// A quick reminder about exercise stubs:
//
// 💡 You're allowed to completely clear any stub before you get started. Often
// we recommend using the stub, because they are already set-up correctly to
// work with the tests, which you can find in ./freelancer-rates.spec.js.
//
// 💡 You don't need to write JSDoc comment blocks yourself; it is not expected
// in idiomatic JavaScript, but some companies and style-guides do enforce them.
//
// Get those rates calculated!
export const WORK_HOURS_PER_DAY = 8
/**
 * The day rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per day
 */
export function dayRate(ratePerHour) {
  return (ratePerHour * WORK_HOURS_PER_DAY);
}

/**
 * Calculates the number of days in a budget, rounded down
 *
 * @param {number} budget: the total budget
 * @param {number} ratePerHour: the rate per hours
 * @returns {number} the number of days
 */
export function daysInBudget(budget, ratePerHour) {
  var total_hours_paid_by_budget = budget / ratePerHour;
  var day_to_complete_project = Math.floor(total_hours_paid_by_budget / WORK_HOURS_PER_DAY);
  return day_to_complete_project;
}

/**
 * Calculates the discounted rate for large projects, rounded up
 *
 * @param {number} ratePerHour
 * @param {number} numDays: number of days the project spans
 * @param {number} discount: for example 20% written as 0.2
 * @returns {number} the rounded up discounted rate
 */
export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  var months_project_spans = Math.floor(numDays / 22);
  var days_left_project_spans = numDays - months_project_spans * 22;
  var days_billed_by_rate = days_left_project_spans * dayRate(ratePerHour);
  var months_billed_without_discount_rate = months_project_spans * 22 * dayRate(ratePerHour);
  var months_billed_with_discount_rate = months_billed_without_discount_rate - 
                                          months_billed_without_discount_rate * discount;
  var total_amount = Math.ceil(months_billed_with_discount_rate + days_billed_by_rate);

  return total_amount;
}


