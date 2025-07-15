/**
 * @file user.cpp
 * @author saja
 * @brief 
 * 
 */

#include "../include/user.hpp"
#include <functional>
#include <algorithm>

// Konstruktor für einen neuen Benutzer
User::User(const std::string& username, const std::string& password) 
    : username(username) {
    
    // Passwort wird mit einfachem Hash gesichert (nicht sicher für reale Anwendungen!)
    std::hash<std::string> hasher;
    password_hash = std::to_string(hasher(password));
    
    // Konto wird mit einem Startguthaben von 1000.0 erstellt
    account = std::make_shared<Account>(1000.0);
    
    // Inventar initialisieren (leere Map)
    inventory.clear();
}

// Authentifiziert einen Benutzer anhand des Passworts
bool User::authenticate(const std::string& password) const {
    std::hash<std::string> hasher;
    std::string provided_hash = std::to_string(hasher(password));
    // Vergleicht den gespeicherten Hash mit dem aus dem Eingabepasswort
    return provided_hash == password_hash;
}

// Gibt den Benutzernamen zurück
std::string User::getUsername() const {
    return username;
}

// Gibt das Benutzerkonto (z.B. für Ein-/Auszahlungen) zurück
std::shared_ptr<Account> User::getAccount() {
    return account;
}

// Gibt das gesamte Inventar (Map von Gut-ID → Anzahl) zurück
const std::unordered_map<int, int>& User::getInventory() const {
    return inventory;
}

// Fügt ein Gut zum Inventar hinzu (oder erhöht die Anzahl, falls schon vorhanden)
void User::addGood(int goodId, int quantity) {
    if (quantity <= 0) {
        return; // Negative oder 0 Menge nicht erlaubt
    }
    
    // Wenn das Gut schon existiert, erhöhe die Anzahl
    auto it = inventory.find(goodId);
    if (it != inventory.end()) {
        it->second += quantity;
    } else {
        // Neues Gut hinzufügen
        inventory[goodId] = quantity;
    }
}

// Entfernt ein Gut aus dem Inventar
bool User::removeGood(int goodId, int quantity) {
    if (quantity <= 0) {
        return false; // Negative oder 0 Menge nicht erlaubt
    }
    
    auto it = inventory.find(goodId);
    if (it == inventory.end()) {
        return false; // Gut existiert nicht im Inventar
    }
    
    if (it->second < quantity) {
        return false; // Zu wenig Menge vorhanden
    }
    
    // Reduziere die Menge
    it->second -= quantity;
    
    // Wenn die Menge auf 0 fällt, entferne das Gut komplett
    if (it->second == 0) {
        inventory.erase(it);
    }
    
    return true;
}

// Gibt die Anzahl eines bestimmten Guts im Inventar zurück
int User::getGoodQuantity(int goodId) const {
    auto it = inventory.find(goodId);
    if (it != inventory.end()) {
        return it->second;
    }
    return 0; // Gut ist nicht im Inventar
}
