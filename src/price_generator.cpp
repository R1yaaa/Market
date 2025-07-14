#include "../include/price_generator.hpp"
#include <cmath>
#include <chrono>

PriceGenerator::PriceGenerator() {
    // Seed with current time
    auto seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
    generator.seed(static_cast<unsigned int>(seed));
}

double PriceGenerator::generateNextPrice(
    double current_price, 
    double tendency, 
    double volatility, 
    double dt
) {
    // Generate random variable Y(t) between -1 and 1
    std::uniform_real_distribution<double> distribution(-1.0, 1.0);
    double Y = distribution(generator);
    
    // Apply Random Walk formula:
    // S(t+1) = S(t) + μ * dt * S(t) + σ * sqrt(dt) * Y(t) * S(t)
    double drift = tendency * dt * current_price;
    double random_component = volatility * std::sqrt(dt) * Y * current_price;
    
    double new_price = current_price + drift + random_component;
    
    // Ensure price doesn't go below a minimum threshold (e.g., 0.01)
    if (new_price < 0.01) {
        new_price = 0.01;
    }
    
    // Round to 2 decimal places
    return std::round(new_price * 100.0) / 100.0;
}