# Simple Debt Management Calculator

Welcome to my extrmely simple Debt Management Calculator!

This is my **_first_** public release as I continue building programming career.

I started out with this as a Python Tkinter Project, but found it easier to do as HTML, CSS, and JavaScript.


## The calculation
### How this program calculates when your debt will be paid off:
* Start with a current balance due
* Enter the interest rate (if any)
* Finally, add your monthly contribution you are willing to pay off on this debt

The calculation subtracts your monthly contribution from your balance. Each month the balance isn't paid off interest is added to the remainder.

The results are then added in the results tab.

It not only lets you know how many months it will take to payoff, but shows your balance for each month.

Here's how the formula is written:

'''js
while (balanceNum > 0) {
        balanceNum -= contributionNum; // Balance - Monthly Contribution
        const accruedInterest = balanceNum + ((rateNum / 12) * balanceNum); // Interest amount is added to whatever is NOT paid off
        months++; //This happens each month until the balance becomes 0
}
'''

If you would like to mess around with my python funtion, I have included the source code.
Just be sure to create a new branch

Future Features:

1. An option to save your results
2. More functionality to gather results and data.

About Me:

My Name is Isaiah, and at the time of this publishing I've been coding for 3 months.

I started learning coding so that I could advance in a career that pays me for solving problems.

As well as help find solutions to making the world a better and more efficient place!

[My LinkedIn Profile](https://linkedin.com/in/isaiah-vickers) |
[My Github](https://linkedin.com/in/isaiah-vickers) |
[My Email](mailto:isaiah.vickers@outlook.com)
