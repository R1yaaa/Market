#pragma once
#include <memory>

/**
 * @brief Repräsentiert ein Benutzerkonto mit Guthaben in POOSE-Coins
 * 
 * Verwaltet das Guthaben eines Nutzers und bietet Operationen für Einzahlungen,
 * Auszahlungen und Kontostandprüfungen. Nutzt Shared Pointer für sicheres
 * Speichermanagement bei geteiltem Zugriff.
 */
class Account {
public:
    using Ptr = std::shared_ptr<Account>; ///< Shared Pointer Typ für Account-Objekte
    
    /**
     * @brief Konstruiert ein neues Konto
     * @param initial_balance Startguthaben (Standard: 1000.0 POOSE-Coins)
     */
    Account(double initial_balance = 1000.0);
    
    // Kontooperationen
    
    /**
     * @brief Führt eine Geldabhebung durch
     * @param amount Abzuhebender Betrag
     * @return true bei Erfolg, false wenn nicht genügend Guthaben
     *
     */
    bool withdraw(double amount);
    
    /**
     * @brief Zahlt Geld auf das Konto ein
     * @param amount Einzuzahlender Betrag
     *
     * Betrag muss positiv sein. Negative Werte werden ignoriert.
     */
    void deposit(double amount);
    
    /**
     * @brief Gibt den aktuellen Kontostand zurück
     * @return Aktuelles Guthaben in POOSE-Coins
     */
    double getBalance() const;
    
    // Validierung
    
    /**
     * @brief Prüft ob ausreichend Guthaben vorhanden ist
     * @param amount Benötigter Betrag
     * @return true wenn Kontostand >= amount, sonst false
     *
     */
    bool hasEnoughBalance(double amount) const;

private:
    double balance; ///< Aktuelles Guthaben in POOSE-Coins
};