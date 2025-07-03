#pragma once
#include <memory>
#include <string>


class User;

/**
 * @brief Repräsentiert ein Handelsangebot auf dem Markt
 * 
 * Enthält alle Informationen über ein Kauf- oder Verkaufsangebot.
 * 
 */
class TradeOffer {
public:
    using Ptr = std::shared_ptr<TradeOffer>; ///< Shared Pointer Typ für TradeOffer
    
    /**
     * @brief Konstruiert ein neues Handelsangebot
     * @param user Anbietender Nutzer
     * @param goodId ID des gehandelten Guts
     * @param quantity Angebotene Menge
     * @param price Angebotspreis pro Einheit
     * @param is_buy_offer true für Kaufangebot, false für Verkaufsangebot
     */
    TradeOffer(std::shared_ptr<User> user, int goodId, int quantity, double price, bool is_buy_offer);
    
    // Getter
    
    /**
     * @brief Gibt den anbietenden Nutzer zurück
     * @return Shared Pointer zum User
     */
    std::shared_ptr<User> getUser() const;
    
    /**
     * @brief Gibt die ID des gehandelten Guts zurück
     * @return Gut-ID
     */
    int getGoodId() const;
    
    /**
     * @brief Gibt die angebotene Menge zurück
     * @return Menge
     */
    int getQuantity() const;
    
    /**
     * @brief Gibt den Angebotspreis pro Einheit zurück
     * @return Preis pro Einheit
     */
    double getPrice() const;
    
    /**
     * @brief Prüft ob es sich um ein Kaufangebot handelt
     * @return true für Kaufangebot, false für Verkaufsangebot
     */
    bool isBuyOffer() const;
    
    // Operationen
    
    /**
     * @brief Reduziert die angebotene Menge
     * @param amount Zu reduzierende Menge
     * @return true bei Erfolg, false wenn nicht genügend Menge vorhanden
     */
    bool reduceQuantity(int amount);
    
    /**
     * @brief Prüft ob das Angebot noch gültig ist
     * @return true wenn quantity > 0, sonst false
     */
    bool isValid() const;

private:
    std::shared_ptr<User> user; ///< Anbietender Nutzer
    int goodId; ///< ID des gehandelten Guts
    int quantity; ///< Angebotene Menge
    double price; ///< Angebotspreis pro Einheit
    bool is_buy_offer; ///< true = Kaufangebot, false = Verkaufsangebot
};