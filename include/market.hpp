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

/**
 * @brief Repräsentiert ein Handelsangebot auf dem Markt
 * 
 * Enthält alle Informationen über ein Kauf- oder Verkaufsangebot.
 * Nutzt Smart Pointer für sicheres Speichermanagement.
 */
struct TradeOffer {
    using Ptr = std::shared_ptr<TradeOffer>; ///< Shared Pointer Typ für TradeOffer
    
    std::weak_ptr<User> user;     ///< Weak-Pointer zum anbietenden User (vermeidet Besitzzyklus)
    int goodId;                   ///< ID des gehandelten Guts
    int quantity;                 ///< Angebotene Menge
    double price;                 ///< Angebotspreis pro Einheit
    bool is_buy_offer;            ///< true = Kaufangebot, false = Verkaufsangebot
};

/**
 * @brief Hauptklasse für den Handelsplatz
 * 
 * Verwaltet alle Marktfunktionen:
 * - Benutzerregistrierung und -anmeldung
 * - Handelsgüter und Preissimulation
 * - Kauf- und Verkaufsangebote
 * - Handelsausführung
 * - Chat-System
 * 
 * Nutzt Smart Pointer für automatisches Speichermanagement.
 */
class Market {
public:
    /**
     * @brief Konstruktor für den Markt
     * 
     * Initialisiert die Handelsgüter und das Chat-System.
     */
    Market();
    
    // Benutzer-Management
    
    /**
     * @brief Registriert einen neuen Benutzer
     * @param username Eindeutiger Benutzername
     * @param password Passwort des Benutzers
     * @return true bei Erfolg, false wenn Benutzername bereits existiert
     */
    bool registerUser(const std::string& username, const std::string& password);
    
    /**
     * @brief Authentifiziert einen Benutzer
     * @param username Benutzername
     * @param password Passwort
     * @return true bei erfolgreicher Anmeldung, sonst false
     */
    bool loginUser(const std::string& username, const std::string& password);
    
    /**
     * @brief Meldet den aktuellen Benutzer ab
     */
    void logout();
    
    /**
     * @brief Gibt den aktuell eingeloggten Benutzer zurück
     * @return Pointer zum User oder nullptr wenn nicht eingeloggt
     */
    User* getCurrentUser() const;
    
    /**
     * @brief Sucht einen Benutzer nach Benutzername
     * @param username Benutzername
     * @return Pointer zum User oder nullptr wenn nicht gefunden
     */
    User* getUser(const std::string& username);
    
    // Handelsgüter
    
    /**
     * @brief Initialisiert die Handelsgüter des Marktes
     * 
     * Erzeugt mindestens 10 seltene Güter mit Startpreisen.
     * Muss vor der ersten Nutzung des Marktes aufgerufen werden.
     */
    void initializeGoods();
    
    /**
     * @brief Gibt alle Handelsgüter zurück
     * @return Vektor mit unique_ptr zu den Gütern
     */
    const std::vector<Good::Ptr>& getGoods() const;
    
    /**
     * @brief Sucht ein Handelsgut nach ID
     * @param goodId ID des gesuchten Guts
     * @return Pointer zum Good oder nullptr wenn nicht gefunden
     */
    Good* getGood(int goodId);
    
    // Handel
    
    /**
     * @brief Erstellt ein Verkaufsangebot
     * @param username Benutzername des Anbieters
     * @param goodId ID des angebotenen Guts
     * @param quantity Angebotene Menge
     * @param price Gewünschter Preis pro Einheit
     * @return true bei Erfolg, false bei ungültigen Parametern
     * 
     * Prüft ob der User genügend Güter besitzt.
     * Führt automatisch Matching mit Kaufangeboten durch.
     */
    bool placeSellOffer(const std::string& username, int goodId, int quantity, double price);
    
    /**
     * @brief Erstellt ein Kaufangebot
     * @param username Benutzername des Käufers
     * @param goodId ID des gewünschten Guts
     * @param quantity Gewünschte Menge
     * @param price Maximalpreis pro Einheit
     * @return true bei Erfolg, false bei ungültigen Parametern
     * 
     * Prüft ob der User genügend Guthaben hat.
     * Führt automatisch Matching mit Verkaufsangeboten durch.
     */
    bool placeBuyOffer(const std::string& username, int goodId, int quantity, double price);
    
    /**
     * @brief Führt einen Handel manuell aus
     * @param buyer Benutzername des Käufers
     * @param seller Benutzername des Verkäufers
     * @param goodId ID des gehandelten Guts
     * @param quantity Gehandelte Menge
     * @return true bei Erfolg, false bei ungültigen Parametern
     * 
     * Wird normalerweise automatisch durch placeBuyOffer/placeSellOffer aufgerufen.
     * Transferiert Guthaben und Güter zwischen den Nutzern.
     */
    bool executeTrade(
        const std::string& buyer, 
        const std::string& seller, 
        int goodId, 
        int quantity
    );
    
    // Preise
    
    /**
     * @brief Aktualisiert alle Güterpreise
     * 
     * Wendet den Random-Walk-Algorithmus auf alle Güter an.
     * Sollte regelmäßig aufgerufen werden (z.B. alle 5-10 Sekunden).
     */
    void updatePrices();
    
    // Angebote
    
    /**
     * @brief Gibt alle aktiven Handelsangebote zurück
     * @return Vektor mit shared_ptr zu TradeOffers
     */
    std::vector<TradeOffer::Ptr> getOffers() const;
    
    /**
     * @brief Gibt Angebote für ein bestimmtes Gut zurück
     * @param goodId ID des gesuchten Guts
     * @return Vektor mit passenden TradeOffers
     */
    std::vector<TradeOffer::Ptr> getOffersForGood(int goodId) const;
    
    // Chat
    
    /**
     * @brief Gibt das Chat-System des Marktes zurück
     * @return shared_ptr zum Chat-Objekt
     */
    std::shared_ptr<Chat> getChat();

private:
    // Benutzerverwaltung
    std::unordered_map<std::string, std::unique_ptr<User>> users; ///< Alle registrierten User (Benutzername -> unique_ptr)
    User* current_user = nullptr; ///< Aktuell eingeloggter User (roher Pointer, kein Besitz)
    
    // Marktdaten
    std::vector<Good::Ptr> goods; ///< Alle verfügbaren Handelsgüter
    std::vector<TradeOffer::Ptr> offers; ///< Aktive Handelsangebote
    PriceGenerator price_generator; ///< Preisgenerator für Random-Walk
    std::shared_ptr<Chat> chat; ///< Chat-System für Nutzerkommunikation
    
    /**
     * @brief Versucht einen Handel zwischen zwei Angeboten auszuführen
     * @param buy_offer Kaufangebot
     * @param sell_offer Verkaufsangebot
     * @return true wenn Handel erfolgreich, sonst false
     * 
     * Prüft Preis- und Mengenkompatibilität.
     * Transferiert Güter und Guthaben.
     * Aktualisiert oder entfernt Angebote nach Handel.
     */
    bool tryExecuteTrade(TradeOffer::Ptr buy_offer, TradeOffer::Ptr sell_offer);
};