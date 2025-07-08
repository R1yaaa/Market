#pragma once
#include <random>

/**
 * @brief Generiert Preise mit Random Walk Algorithmus
 * 
 * Implementiert den Random Walk aus der Aufgabenstellung:
 * S(t+1) = S(t) + μ * dt * S(t) + σ * sqrt(dt) * Y(t) * S(t)
 * 
 * wobei Y(t) eine Zufallsvariable zwischen -1 und 1 ist.
 */
class PriceGenerator {
public:
    /**
     * @brief Konstruiert einen neuen Preisgenerator
     */
    PriceGenerator();
    
    /**
     * @brief Generiert den nächsten Preis mit Random Walk
     * @param current_price Aktueller Preis
     * @param tendency Tendenz (μ) - wie stark soll der Kurs langfristig steigen
     * @param volatility Volatilität (σ) - Standardabweichung/Streuung
     * @param dt Zeitschritt (Standard: 0.001)
     * @return Neuer Preis
     */
    double generateNextPrice(
        double current_price, 
        double tendency = 0.05, 
        double volatility = 0.8, 
        double dt = 0.001
    );

private:
    std::mt19937 generator; ///< Zufallsgenerator
};