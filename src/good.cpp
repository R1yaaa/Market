#include "../include/good.hpp"
#include <algorithm>

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
}

int Good::getId() const {
    return id;
}

std::string Good::getName() const {
    return name;
}

double Good::getCurrentPrice() const {
    return current_price;
}

int Good::getQuantity() const {
    return quantity;
}

void Good::updatePrice(double new_price) {
    if (new_price > 0) {
        current_price = new_price;
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