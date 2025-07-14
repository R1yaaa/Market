#include "../include/market.hpp"
#include <algorithm>

// Konstruktor: Initialisiert den Markt mit einer Liste von Gütern
Market::Market() {
    initializeGoods();
}

// Registriert einen neuen Benutzer mit Benutzername und Passwort
bool Market::registerUser(const std::string& username, const std::string& password) {
    // Prüfe, ob der Benutzername bereits existiert
    if (users.find(username) != users.end()) {
        return false; // Benutzer existiert schon
    }

    // Erstelle einen neuen Benutzer und speichere ihn
    auto new_user = std::make_shared<User>(username, password);
    users[username] = new_user;

    return true;
}

// Loggt einen Benutzer ein, wenn Benutzername und Passwort stimmen
bool Market::loginUser(const std::string& username, const std::string& password) {
    // Suche nach dem Benutzer
    auto it = users.find(username);
    if (it == users.end()) {
        return false; // Benutzer nicht gefunden
    }

    // Überprüfe Passwort
    if (!it->second->authenticate(password)) {
        return false; // Falsches Passwort
    }

    // Benutzer als eingeloggt markieren
    logged_in_users.insert(username);

    return true;
}

// Loggt den Benutzer aus, wenn Benutzername und Passwort korrekt sind
bool Market::logout(const std::string& username, const std::string& password) {
    // Suche nach dem Benutzer
    auto it = users.find(username);
    if (it == users.end()) {
        return false; // Benutzer nicht gefunden
    }

    // Passwort überprüfen
    if (!it->second->authenticate(password)) {
        return false; // Falsches Passwort
    }

    // Prüfe, ob Benutzer überhaupt eingeloggt ist
    if (logged_in_users.find(username) == logged_in_users.end()) {
        return false; // Benutzer war nicht eingeloggt
    }

    // Benutzer aus der Liste der eingeloggt Benutzer entfernen
    logged_in_users.erase(username);

    return true;
}

// Gibt den ersten aktuell eingeloggt Benutzer zurück
std::shared_ptr<User> Market::getCurrentUser() const {
    if (logged_in_users.empty()) {
        return nullptr; // Kein Benutzer eingeloggt
    }

    // Nehme den ersten eingeloggt Benutzer
    std::string username = *logged_in_users.begin();
    auto it = users.find(username);
    if (it != users.end()) {
        return it->second;
    }

    return nullptr;
}

// Gibt den Benutzer mit gegebenem Namen zurück (falls vorhanden)
std::shared_ptr<User> Market::getUser(const std::string& username) {
    auto it = users.find(username);
    if (it != users.end()) {
        return it->second;
    }
    return nullptr;
}

// Prüft, ob ein Benutzer eingeloggt ist
bool Market::isUserLoggedIn(const std::string& username) const {
    return logged_in_users.find(username) != logged_in_users.end();
}

// Gibt die Liste aller im Markt verfügbaren Güter zurück
const std::vector<std::shared_ptr<Good>>& Market::getGoods() const {
    return goods;
}

// Gibt ein bestimmtes Gut anhand seiner ID zurück
std::shared_ptr<Good> Market::getGood(int goodId) {
    auto it = std::find_if(goods.begin(), goods.end(), 
        [goodId](const std::shared_ptr<Good>& good) {
            return good->getId() == goodId;
        });

    if (it != goods.end()) {
        return *it;
    }

    return nullptr;
}

// Ermöglicht dem aktuellen Benutzer, ein Gut zu kaufen
bool Market::buyGood(int goodId, int quantity) {
    // Hole den aktuellen Benutzer
    auto current_user = getCurrentUser();
    if (!current_user) {
        return false; // Kein Benutzer eingeloggt
    }

    // Suche das gewünschte Gut
    auto good = getGood(goodId);
    if (!good) {
        return false; // Gut nicht gefunden
    }

    // Prüfe, ob genug Menge vorhanden ist
    if (!good->hasEnoughQuantity(quantity)) {
        return false; // Nicht genug Menge verfügbar
    }

    // Berechne Gesamtkosten
    double total_cost = good->getCurrentPrice() * quantity;

    // Prüfe, ob der Benutzer genug Guthaben hat
    auto account = current_user->getAccount();
    if (!account->hasEnoughBalance(total_cost)) {
        return false; // Nicht genug Guthaben
    }

    // Führe die Transaktion durch
    if (account->withdraw(total_cost)) {
        if (good->reduceQuantity(quantity)) {
            current_user->addGood(goodId, quantity);
            return true;
        } else {
            // Wenn die Reduktion der Menge fehlschlägt, mache die Abbuchung rückgängig
            account->deposit(total_cost);
            return false;
        }
    }

    return false;
}

// Ermöglicht dem Benutzer, ein Gut aus seinem Inventar zu verkaufen
bool Market::sellGood(int goodId, int quantity) {
    // Hole den aktuellen Benutzer
    auto current_user = getCurrentUser();
    if (!current_user) {
        return false; // Kein Benutzer eingeloggt
    }

    // Finde das Gut
    auto good = getGood(goodId);
    if (!good) {
        return false; // Gut nicht gefunden
    }

    // Prüfe, ob Benutzer genug vom Gut im Besitz hat
    if (current_user->getGoodQuantity(goodId) < quantity) {
        return false; // Nicht genug im Inventar
    }

    // Berechne Verkaufserlös
    double total_revenue = good->getCurrentPrice() * quantity;

    // Führe den Verkauf durch
    if (current_user->removeGood(goodId, quantity)) {
        good->increaseQuantity(quantity); // Erhöhe Marktmenge
        current_user->getAccount()->deposit(total_revenue); // Gutschrift an Benutzerkonto
        return true;
    }

    return false;
}

// Aktualisiert die Preise aller Güter anhand eines Preisgenerators
void Market::updatePrices() {
    for (auto& good : goods) {
        double new_price = price_generator.generateNextPrice(good->getCurrentPrice());
        good->updatePrice(new_price);
    }
}

// Initialisiert den Markt mit einer festen Liste von verfügbaren Gütern
void Market::initializeGoods() {
    goods.push_back(std::make_shared<Good>(1, "confidence boost", 50.0, 100));
   
}
