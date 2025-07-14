#pragma once
#include <string>
#include <memory>

/**
 * @brief Repräsentiert ein Handelsgut auf dem Markt
 * 
 * Diese Klasse modelliert ein handelbares Gut mit eindeutiger ID, Namen, 
 * variablem Preis und verfügbarer Menge. Der Preis wird durch Marktmechanismen 
 * (Random Walk) aktualisiert. Die Menge bestimmt, wie viele Einheiten verfügbar sind.
 */
class Good {
public:
    using Ptr = std::shared_ptr<Good>; ///< Shared Pointer Typ für geteilten Zugriff
    
    /**
     * @brief Konstruiert ein neues Handelsgut
     * @param id Eindeutige numerische ID des Guts
     * @param name Anzeigename des Guts 
     * @param initial_price Startpreis in POOSE-Coins
     * @param initial_quantity Verfügbare Startmenge
     */
    Good(int id, const std::string& name, double initial_price, int initial_quantity);
    
    // Getter
    
    /**
     * @brief Gibt die eindeutige ID des Guts zurück
     * @return Numerische ID
     */
    int getId() const;
    
    /**
     * @brief Gibt den Anzeigenamen des Guts zurück
     * @return Human-readable Name
     */
    std::string getName() const;
    
    /**
     * @brief Gibt den aktuellen Marktpreis zurück
     * @return Preis in POOSE-Coins
     */
    double getCurrentPrice() const;
    
    /**
     * @brief Gibt die verfügbare Menge zurück
     * @return Anzahl verfügbarer Einheiten
     */
    int getQuantity() const;
    
    // Preis-Update
    
    /**
     * @brief Setzt einen neuen Preis für das Gut
     * @param new_price Neuer Preis in POOSE-Coins
     * 
     * Wird typischerweise vom Preisgenerator aufgerufen.
     * Stellt sicher: new_price > 0
     */
    void updatePrice(double new_price);
    
    // Mengen-Management
    
    /**
     * @brief Prüft ob genügend Menge verfügbar ist
     * @param requested_quantity Gewünschte Menge
     * @return true wenn genügend verfügbar, sonst false
     */
    bool hasEnoughQuantity(int requested_quantity) const;
    
    /**
     * @brief Reduziert die verfügbare Menge (beim Kauf)
     * @param quantity Zu reduzierende Menge
     * @return true bei Erfolg, false wenn nicht genügend verfügbar
     */
    bool reduceQuantity(int quantity);
    
    /**
     * @brief Erhöht die verfügbare Menge (beim Verkauf)
     * @param quantity Zu erhöhende Menge
     */
    void increaseQuantity(int quantity);

private:
    int id; ///< Eindeutige numerische ID
    std::string name; ///<Name des Guts
    double current_price; ///< Aktueller Preis in POOSE-Coins
    int quantity; ///< Verfügbare Menge
};