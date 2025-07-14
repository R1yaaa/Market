#include "account.hpp"
#include <algorithm>

Account::Account(double initial_balance) : balance(initial_balance) {
    // keine negative balance
    if (balance < 0) {
        balance = 0;
    }
}

bool Account::withdraw(double amount) {
    if (amount <= 0) {
        return false; // keine negative amount abheben
    }
    
    if (balance >= amount) {
        balance -= amount;
        return true;
    }
    
    return false; // nicht genügend balance
}

void Account::deposit(double amount) {
    if (amount > 0) {
        balance += amount;
    }
    // Ignore negative deposits
}

double Account::getBalance() const { //balance zurückgeben
    return balance;
}

bool Account::hasEnoughBalance(double amount) const {
    return balance >= amount;
}