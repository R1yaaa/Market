#pragma once
#include <random>

class PriceGenerator {
public:
    PriceGenerator();
    
    // Random Walk Algorithmus
    double generateNextPrice(
        double current_price, 
        double tendency = 0.05, 
        double volatility = 0.8, 
        double dt = 0.001
    );

private:
    std::mt19937 generator;
};