#pragma once
#include <string>
#include <memory>
#include <unordered_map>
#include "account.hpp"

/**
 * @brief Repräsentiert einen registrierten Nutzer des Handelsplatzes
 * 
 * Verwaltet Nutzerdaten, Authentifizierung, Konto und Inventar.
 * Nutzt Shared Pointer für das Konto, um geteilten Zugriff zu ermöglichen.
 */
class User {
public:
    /**
     * @brief Konstruiert einen neuen Nutzer
     * @param username Eindeutiger Benutzername
     * @param password Klartext-Passwort (wird gehasht gespeichert)
     * 
     * Erstellt automatisch:
     * - Konto mit Startguthaben (Standard: 0 POOSE-Coins)
     * - Leeres Inventar
     */
    User(const std::string& username, const std::string& password);
    
    // Authentifizierung

    /**
     * @brief Prüft die Authentifizierung des Nutzers
     * @param password Eingebenes Passwort (Klartext)
     * @return true wenn Passwort übereinstimmt, sonst false
     * 
     * Vergleicht den Hash des eingegebenen Passworts mit gespeichertem Hash.
     */
    bool authenticate(const std::string& password) const;
    
    // Getter

    /**
     * @brief Gibt den Benutzernamen zurück
     * @return Eindeutiger Nutzername
     */
    std::string getUsername() const;
    
    /**
     * @brief Gibt Zugriff auf das Nutzerkonto
     * @return Shared Pointer zum Account-Objekt
     * 
     * Ermöglicht Kontotransaktionen:
     * @code
     * user->getAccount()->deposit(100.0);
     * @endcode
     */
    std::shared_ptr<Account> getAccount();
    
    /**
     * @brief Gibt das gesamte Inventar zurück
     * @return Konstante Referenz zur Inventory-Map (goodId -> Menge)
     * 
     * Beispiel für Inventardurchlauf:
     * @code
     * for (const auto& [id, qty] : user.getInventory()) {
     *     std::cout << "Gut #" << id << ": " << qty << " Einheiten\n";
     * }
     * @endcode
     */
    const std::unordered_map<int, int>& getInventory() const;
    
    // Inventar-Management

    /**
     * @brief Fügt Güter zum Inventar hinzu
     * @param goodId ID des hinzuzufügenden Guts
     * @param quantity Menge (Standard: 1)
     * 
     * Beispiel für Masseneinzug:
     * @code
     * user.addGood(3, 5); // Fügt 5 Einheiten von Gut #3 hinzu
     * @endcode
     */
    void addGood(int goodId, int quantity = 1);
    
    /**
     * @brief Entfernt Güter aus dem Inventar
     * @param goodId ID des zu entfernenden Guts
     * @param quantity Menge (Standard: 1)
     * @return true bei Erfolg, false wenn nicht genügend Einheiten vorhanden
     * 
     * Wird typischerweise bei Verkauf oder Handel verwendet.
     */
    bool removeGood(int goodId, int quantity = 1);
    
    /**
     * @brief Prüft den Bestand eines bestimmten Guts
     * @param goodId ID des gesuchten Guts
     * @return Anzahl der Einheiten im Inventar (0 wenn nicht vorhanden)
     */
    int getGoodQuantity(int goodId) const;

private:
    std::string username;                   ///< Eindeutiger Benutzername
    std::string password_hash;              ///< Gehashtes Passwort (Sicherheit)
    std::shared_ptr<Account> account;       ///< POOSE-Coin-Konto (Shared Ownership)
    std::unordered_map<int, int> inventory; ///< Inventar: goodId -> Menge
};