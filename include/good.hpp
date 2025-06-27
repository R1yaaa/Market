#pragma once
#include <string>
#include <memory>

/**
 * @brief Repräsentiert ein Handelsgut auf dem Markt
 * 
 * Diese Klasse modelliert ein handelbares Gut mit eindeutiger ID, Namen und variablem Preis.
 * Der Preis wird durch Marktmechanismen (Random Walk) aktualisiert. Nutzt Unique Pointer
 * für exklusive Besitzverhältnisse im Markt.
 */
class Good {
public:
    using Ptr = std::unique_ptr<Good>; ///< Unique Pointer Typ für exklusiven Besitz
    
    /**
     * @brief Konstruiert ein neues Handelsgut
     * @param id Eindeutige numerische ID des Guts
     * @param name Anzeigename des Guts (z.B. "Klausurzulassung")
     * @param initial_price Startpreis in POOSE-Coins
     */
    Good(int id, const std::string& name, double initial_price);
    
    // Getter

    /**
     * @brief Gibt die eindeutige ID des Guts zurück
     * @return Numerische ID
     * 
     * Wird verwendet für:
     * - Handelstransaktionen
     * - Inventarverwaltung
     * - Preisabfragen
     */
    int getId() const;
    
    /**
     * @brief Gibt den Anzeigenamen des Guts zurück
     * @return Human-readable Name
     * 
     * Beispiel: "Sonnenblumenöl" oder "POOSE-Merch Hoodie"
     */
    std::string getName() const;
    
    /**
     * @brief Gibt den aktuellen Marktpreis zurück
     * @return Preis in POOSE-Coins
     * 
     * Der Preis wird regelmäßig durch Market::updatePrices() aktualisiert.
     */
    double getCurrentPrice() const;
    
    // Preis-Update

    /**
     * @brief Setzt einen neuen Preis für das Gut
     * @param new_price Neuer Preis in POOSE-Coins
     * 
     * Wird typischerweise vom Preisgenerator aufgerufen.
     * Stellt sicher: new_price > 0
     * 
     * @warning Direkter Aufruf nur durch Marktlogik!
     */
    void updatePrice(double new_price);

private:
    int id;                ///< Eindeutige numerische ID
    std::string name;      ///< Human-readable Name des Guts
    double current_price;  ///< Aktueller Preis in POOSE-Coins
};