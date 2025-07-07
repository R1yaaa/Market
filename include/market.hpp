#pragma once
#include <vector>
#include <memory>
#include <unordered_map>
#include <string>
#include "user.hpp"
#include "good.hpp"
#include "price_generator.hpp"

/**
 * @brief Hauptklasse für den Handelsplatz
 * 
 * Verwaltet alle Marktfunktionen:
 * - Benutzerregistrierung und -anmeldung
 * - Handelsgüter und Preissimulation
 * - Kauf- und Verkaufsangebote
 * - Handelsausführung
 * 
 * 
 */
class Market {
public:
    /**
     * @brief Konstruktor für den Markt
     * 
     * Initialisiert die Handelsgüter (mindestens 10 rare Güter).
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
     * @return Shared Pointer zum User (nullptr wenn nicht eingeloggt)
     * 
     *
     */
    std::shared_ptr<User> getCurrentUser() const;
    
    /**
     * @brief Sucht einen Benutzer nach Benutzername
     * @param username Benutzername
     * @return Shared Pointer zum User (nullptr wenn nicht gefunden)
     */
    std::shared_ptr<User> getUser(const std::string& username);
    
    // Handelsgüter
    
    /**
     * @brief Gibt alle Handelsgüter zurück
     * @return Konstante Referenz zum Vektor mit shared_ptr zu den Gütern
     */
    const std::vector<std::shared_ptr<Good>>& getGoods() const;
    
    /**
     * @brief Sucht ein Handelsgut nach ID
     * @param goodId ID des gesuchten Guts
     * @return Shared Pointer zum Good (nullptr wenn nicht gefunden)
     */
    std::shared_ptr<Good> getGood(int goodId);
    
    // Handel
    
    /**
     * @brief Erstellt ein Verkaufsangebot
     * @param goodId ID des angebotenen Guts
     * @param quantity Angebotene Menge
     * @param price Gewünschter Preis pro Einheit
     * @return true bei Erfolg, false bei ungültigen Parametern
     * 
     * Prüft ob der eingeloggte User genügend Güter besitzt.
     * Führt automatisch Matching mit Kaufangeboten durch.
     */
    bool placeSellOffer(int goodId, int quantity, double price);
    
    /**
     * @brief Erstellt ein Kaufangebot
     * @param goodId ID des gewünschten Guts
     * @param quantity Gewünschte Menge
     * @param price Maximalpreis pro Einheit
     * @return true bei Erfolg, false bei ungültigen Parametern
     * 
     * Prüft ob der eingeloggte User genügend Guthaben hat.
     * Führt automatisch Matching mit Verkaufsangeboten durch.
     */
    bool placeBuyOffer(int goodId, int quantity, double price);
    
    /**
     * @brief Kauft ein Gut direkt zum aktuellen Marktpreis
     * @param goodId ID des zu kaufenden Guts
     * @param quantity Gewünschte Menge
     * @return true bei Erfolg, false bei ungültigen Parametern
     * 
     * Kauft zum aktuellen Marktpreis des Guts.
     * Der eingeloggte User muss genügend Guthaben haben.
     */
    bool buyGood(int goodId, int quantity);
    
    // Preise
    
    /**
     * @brief Aktualisiert alle Güterpreise
     * 
     * Wendet den Random-Walk-Algorithmus auf alle Güter an.
     * Sollte regelmäßig aufgerufen werden (z.B. alle paar Sekunden).
     */
    void updatePrices();
    
    // Angebote
    
    /**
     * @brief Gibt alle aktiven Handelsangebote zurück
     * @return Konstante Referenz zum Vektor mit shared_ptr zu TradeOffers
     */
    const std::vector<std::shared_ptr<TradeOffer>>& getOffers() const;
    
    /**
     * @brief Gibt Angebote für ein bestimmtes Gut zurück
     * @param goodId ID des gesuchten Guts
     * @return Vektor mit passenden TradeOffers
     */
    std::vector<std::shared_ptr<TradeOffer>> getOffersForGood(int goodId) const;

private:
    // Benutzerverwaltung
    std::unordered_map<std::string, std::shared_ptr<User>> users; ///< Alle registrierten User
    std::shared_ptr<User> current_user; ///< Aktuell eingeloggter User

    // Marktdaten
    std::vector<std::shared_ptr<Good>> goods; ///< Alle verfügbaren Handelsgüter
    std::vector<std::shared_ptr<TradeOffer>> offers; ///< Aktive Handelsangebote
    PriceGenerator price_generator; ///< Preisgenerator für Random-Walk
    
    /**
     * @brief Initialisiert die Handelsgüter des Marktes
     * 
     * Erzeugt mindestens 10 seltene Güter mit Startpreisen.
     */
    void initializeGoods();
    
    /**
     * @brief Versucht automatisches Matching zwischen Angeboten
     * 
     * Sucht nach kompatiblen Kauf- und Verkaufsangeboten und führt Handel aus.
     */
    void matchOrders();
    
    /**
     * @brief Führt einen Handel zwischen zwei Angeboten aus
     * @param buy_offer Kaufangebot
     * @param sell_offer Verkaufsangebot
     * @return true wenn Handel erfolgreich, sonst false
     */
    bool executeTrade(std::shared_ptr<TradeOffer> buy_offer, std::shared_ptr<TradeOffer> sell_offer);
    
    /**
     * @brief Entfernt ungültige Angebote aus der Liste
     */
    void cleanupOffers();
};