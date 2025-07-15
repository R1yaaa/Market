/**
 * @file good.cpp
 * @author saja
 * @brief 
 * 
 */

#include "../include/good.hpp"
#include <algorithm>
#include <cmath>

// Hilfsfunktion für Rundung auf 2 Nachkommastellen
double roundToTwoDecimals(double value) {
    return std::round(value * 100.0) / 100.0;
}

Good::Good(int id, const std::string& name, double initial_price, int initial_quantity) 
    : id(id), name(name), current_price(initial_price), quantity(initial_quantity) {
    // Ensure price is positive
    if (current_price <= 0) {
        current_price = 1.0;
    }
    
    // Ensure quantity is not negative
    if (quantity < 0) {
        quantity = 0;
    }
    
    // Round price to 2 decimal places
    current_price = roundToTwoDecimals(current_price);
}

int Good::getId() const {
    return id;
}

std::string Good::getName() const {
    return name;
}

double Good::getCurrentPrice() const {
    // Immer auf 2 Nachkommastellen runden beim Zurückgeben
    return roundToTwoDecimals(current_price);
}

int Good::getQuantity() const {
    return quantity;
}

void Good::updatePrice(double new_price) {
    if (new_price > 0) {
        // Round to 2 decimal places before storing
        current_price = roundToTwoDecimals(new_price);
    }
    // Ignore non-positive prices
}

bool Good::hasEnoughQuantity(int requested_quantity) const {
    return quantity >= requested_quantity;
}

bool Good::reduceQuantity(int quantity_to_reduce) {
    if (quantity_to_reduce <= 0) {
        return false; // Cannot reduce negative or zero quantity
    }
    
    if (quantity >= quantity_to_reduce) {
        quantity -= quantity_to_reduce;
        return true;
    }
    
    return false; // Not enough quantity available
}

void Good::increaseQuantity(int quantity_to_add) {
    if (quantity_to_add > 0) {
        quantity += quantity_to_add;
    }
    // Ignore negative increases
}