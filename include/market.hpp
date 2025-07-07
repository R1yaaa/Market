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
 * - Direkter Kauf und Verkauf zum Marktpreis
 * 
 * Vereinfachte Version ohne Handelsangebote - nur sofortiger Handel.
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
    
    // Direkter Handel (ohne Angebote)
    
    /**
     * @brief Kauft ein Gut direkt zum aktuellen Marktpreis
     * @param goodId ID des zu kaufenden Guts
     * @param quantity Gewünschte Menge
     * @return true bei Erfolg, false bei unzureichendem Guthaben oder ungültigen Parametern
     * 
     * Sofortiger Kauf zum aktuellen Marktpreis.
     * Geld wird sofort vom Konto abgezogen, Ware sofort ins Inventar gelegt.
     */
    bool buyGood(int goodId, int quantity);
    
    /**
     * @brief Verkauft ein Gut direkt zum aktuellen Marktpreis
     * @param goodId ID des zu verkaufenden Guts
     * @param quantity Zu verkaufende Menge
     * @return true bei Erfolg, false bei unzureichendem Inventar
     * 
     * Sofortiger Verkauf zum aktuellen Marktpreis.
     * Ware wird sofort aus Inventar entfernt, Geld sofort gutgeschrieben.
     */
    bool sellGood(int goodId, int quantity);
    
    // Preise
    
    /**
     * @brief Aktualisiert alle Güterpreise
     * 
     * Wendet den Random-Walk-Algorithmus auf alle Güter an.
     * Sollte regelmäßig aufgerufen werden (z.B. alle paar Sekunden).
     */
    void updatePrices();

private:
    // Benutzerverwaltung
    std::unordered_map<std::string, std::shared_ptr<User>> users; ///< Alle registrierten User
    std::shared_ptr<User> current_user; ///< Aktuell eingeloggter User

    // Marktdaten
    std::vector<std::shared_ptr<Good>> goods; ///< Alle verfügbaren Handelsgüter
    PriceGenerator price_generator; ///< Preisgenerator für Random-Walk
    
    /**
     * @brief Initialisiert die Handelsgüter des Marktes
     * 
     * Erzeugt mindestens 10 seltene Güter mit Startpreisen.
     */
    void initializeGoods();
};