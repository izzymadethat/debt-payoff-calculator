function calculateDebt(balance, rate, contribution) {
    let balanceNum = parseFloat(balance)
    let rateNum = parseFloat(rate) / 100
    let contributionNum = parseFloat(contribution)

    // console.log(balanceNum)
    // console.log(rateNum)
    // console.log(contributionNum)

    // balanceNum -= contributionNum
    // accruedInterest = balanceNum + ((rateNum / 12) * balanceNum)
    // console.log(balanceNum, accruedInterest)

    if (isNaN(balanceNum) || isNaN(rateNum) || isNaN(contributionNum)) {
        console.log('Please enter a valid number')
        return;
    }

    if (contributionNum < 10) {
        console.log('PMust contribute at least $10')
        return;
    }

    let months = 0;

    while (balanceNum > 0) {
        balanceNum -= contributionNum; // Balance - Monthly Contribution
        const accruedInterest = balanceNum + ((rateNum / 12) * balanceNum); // Interest amount is added to whatever is NOT paid off
        months++; //This happens each month until the balance becomes 0


        console.log("Month: " + months + " Balance Paid: $" + balanceNum.toFixed(2) + " New Balance: $" + accruedInterest.toFixed(2))

    }
    console.log("No Balance Owed.");

};

document.getElementById('debtSubmit').addEventListener('click', function () {
    let balanceDue = document.getElementById('balance').value;
    let interestRate = document.getElementById('rate').value;
    let monthlyContribution = document.getElementById('monthlyPayment').value;

    calculateDebt(balanceDue, interestRate, monthlyContribution);
});