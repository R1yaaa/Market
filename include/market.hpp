#pragma once
#include <vector>
#include <map>
#include <memory>
#include <unordered_map>
#include <string>
#include "user.hpp"
#include "good.hpp"
#include "price_generator.hpp"
#include "chat.hpp"

struct TradeOffer {
    using Ptr = std::shared_ptr<TradeOffer>;
    
    std::weak_ptr<User> user;
    int goodId;
    int quantity;
    double price;
    bool is_buy_offer;
};

class Market {
public:
    Market();
    
    // Benutzer-Management
    bool registerUser(const std::string& username, const std::string& password);
    bool loginUser(const std::string& username, const std::string& password);
    void logout();
    User* getCurrentUser() const;
    User* getUser(const std::string& username);
    
    // Handelsgüter
    void initializeGoods();
    const std::vector<Good::Ptr>& getGoods() const;
    Good* getGood(int goodId);
    
    // Handel
    bool placeSellOffer(const std::string& username, int goodId, int quantity, double price);
    bool placeBuyOffer(const std::string& username, int goodId, int quantity, double price);
    bool executeTrade(
        const std::string& buyer, 
        const std::string& seller, 
        int goodId, 
        int quantity
    );
    
    // Preise aktualisieren
    void updatePrices();
    
    // Angebote anzeigen
    std::vector<TradeOffer::Ptr> getOffers() const;
    std::vector<TradeOffer::Ptr> getOffersForGood(int goodId) const;
    
    // Chat
    std::shared_ptr<Chat> getChat();

private:
    // Benutzerverwaltung
    std::unordered_map<std::string, std::unique_ptr<User>> users;
    User* current_user = nullptr;
    
    // Marktdaten
    std::vector<Good::Ptr> goods;
    std::vector<TradeOffer::Ptr> offers;
    PriceGenerator price_generator;
    std::shared_ptr<Chat> chat;
    
    // Automatisches Matching
    bool tryExecuteTrade(TradeOffer::Ptr buy_offer, TradeOffer::Ptr sell_offer);
};