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

    // if (isNaN(balanceNum) || isNaN(rateNum) || isNaN(contributionNum)) {
    //     document.querySelector('#result').innerText = "Please enter a valid number"
    //     console.log('Please enter a valid number')
    //     return;
    // }

    if (isNaN(balanceNum) && isNaN(rateNum) && isNaN(contributionNum)) {
        document.querySelector('#result').innerText = "No Results entered!"
        console.log('No Results entered!')
        return;
    }

    if (contributionNum < 10) {
        console.log('PMust contribute at least $10')
        return;
    }

    let months = 0;
    let resultText = "";

    while (balanceNum > 0) {
        balanceNum -= contributionNum; // Balance - Monthly Contribution
        const accruedInterest = balanceNum + ((rateNum / 12) * balanceNum); // Interest amount is added to whatever is NOT paid off
        months++; //This happens each month until the balance becomes 0
        resultText += "Month: " + months + " Balance Paid: $" + balanceNum.toFixed(2) + " New Balance: $" + accruedInterest.toFixed(2) + "\n"


        console.log("Month: " + months + " Balance Paid: $" + balanceNum.toFixed(2) + " New Balance: $" + accruedInterest.toFixed(2));

    }

    if (months < 0) {
        resultText += "No Balance Owed."
    }

    document.querySelector('#result').innerText = resultText;
    console.log("No Balance Owed.");
    addToResults(months);
};

function addToResults(month) {
    document.querySelector('#result').innerText += "\nYour Debt will take " + month + " month(s) to pay off.";
}


// When the Submit Button is Selected..
document.getElementById('debtSubmit').addEventListener('click', function () {
    event.preventDefault();
    let balanceDue = document.getElementById('balance').value;
    let interestRate = document.getElementById('rate').value;
    let monthlyContribution = document.getElementById('monthlyPayment').value;

    calculateDebt(balanceDue, interestRate, monthlyContribution);


});

// When the clear button is selected..
document.getElementById('resetFields').addEventListener('click', function () {
    document.getElementById('debtName').value = ""
    document.getElementById('balance').value = ""
    document.getElementById('rate').value = ""
    document.getElementById('monthlyPayment').value = ""
    document.querySelector('#result').innerText = ""
})