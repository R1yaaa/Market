/**
 * @file tests.cpp
 * @author saja
 * @brief test einiger funktionen
 * @version 0.1
 * @date 2025-07-13

 * 
 */
#include <gtest/gtest.h>
#include "../include/market.hpp"
#include "../include/user.hpp"
#include "../include/account.hpp"
#include "../include/good.hpp"
#include "../include/price_generator.hpp"
#include <memory>

TEST(MarketTest, RegisterAndLoginUser) {
    Market market;
    
    // Test user registration
    EXPECT_TRUE(market.registerUser("testuser", "password123"));
    EXPECT_FALSE(market.registerUser("testuser", "password456")); // Duplicate username
    
    // Test user login
    EXPECT_TRUE(market.loginUser("testuser", "password123"));
    EXPECT_FALSE(market.loginUser("testuser", "wrongpassword"));
    EXPECT_FALSE(market.loginUser("nonexistent", "password123"));
    
    // Test getting user
    auto user = market.getUser("testuser");
    EXPECT_NE(user, nullptr);
    EXPECT_EQ(user->getUsername(), "testuser");
}

TEST(MarketTest, BuyAndSellGoods) {
    Market market;
    
    // Register and login user
    market.registerUser("trader", "password123");
    market.loginUser("trader", "password123");
    
    // Get first available good
    auto goods = market.getGoods();
    EXPECT_FALSE(goods.empty());
    
    auto good = goods[0];
    int goodId = good->getId();
    double price = good->getCurrentPrice();
    
    // Test buying
    EXPECT_TRUE(market.buyGood(goodId, 5));
    
    auto current_user = market.getCurrentUser();
    EXPECT_NE(current_user, nullptr);
    EXPECT_EQ(current_user->getGoodQuantity(goodId), 5);
    
    // Check account balance decreased
    double expected_balance = 1000.0 - (price * 5);
    EXPECT_DOUBLE_EQ(current_user->getAccount()->getBalance(), expected_balance);
    
    // Test selling
    EXPECT_TRUE(market.sellGood(goodId, 3));
    EXPECT_EQ(current_user->getGoodQuantity(goodId), 2);
    
    // Check account balance increased
    double new_expected_balance = expected_balance + (price * 3);
    EXPECT_DOUBLE_EQ(current_user->getAccount()->getBalance(), new_expected_balance);
}

TEST(MarketTest, InsufficientFunds) {
    Market market;
    
    // Register user with default balance (1000 POOSE-Coins)
    market.registerUser("pooruser", "password123");
    market.loginUser("pooruser", "password123");
    
    auto goods = market.getGoods();
    auto expensive_good = goods[0];
    int goodId = expensive_good->getId();
    
    // Try to buy more than affordable
    int expensive_quantity = 1000; // Should cost more than 1000 POOSE-Coins
    EXPECT_FALSE(market.buyGood(goodId, expensive_quantity));
    
    // User should still have original balance
    auto current_user = market.getCurrentUser();
    EXPECT_DOUBLE_EQ(current_user->getAccount()->getBalance(), 1000.0);
}

TEST(MarketTest, InsufficientInventory) {
    Market market;
    
    market.registerUser("seller", "password123");
    market.loginUser("seller", "password123");
    
    auto goods = market.getGoods();
    int goodId = goods[0]->getId();
    
    // Try to sell without having the good
    EXPECT_FALSE(market.sellGood(goodId, 1));
    
    // Buy some goods first
    EXPECT_TRUE(market.buyGood(goodId, 3));
    
    // Try to sell more than owned
    EXPECT_FALSE(market.sellGood(goodId, 5));
    
    // Sell valid amount
    EXPECT_TRUE(market.sellGood(goodId, 2));
}



TEST(UserTest, InventoryManagement) {
    User user("testuser", "password123");
    
    // Add goods to inventory
    user.addGood(1, 10);
    user.addGood(2, 5);
    
    EXPECT_EQ(user.getGoodQuantity(1), 10);
    EXPECT_EQ(user.getGoodQuantity(2), 5);
    EXPECT_EQ(user.getGoodQuantity(3), 0); // Non-existent good
    
    // Add more of the same good
    user.addGood(1, 5);
    EXPECT_EQ(user.getGoodQuantity(1), 15);
    
    // Remove goods
    EXPECT_TRUE(user.removeGood(1, 7));
    EXPECT_EQ(user.getGoodQuantity(1), 8);
    
    // Try to remove more than available
    EXPECT_FALSE(user.removeGood(1, 10));
    EXPECT_EQ(user.getGoodQuantity(1), 8); // Should remain unchanged
    
    // Remove all of a good
    EXPECT_TRUE(user.removeGood(1, 8));
    EXPECT_EQ(user.getGoodQuantity(1), 0);
    EXPECT_EQ(user.getInventory().find(1), user.getInventory().end()); // Should be removed from map
}

TEST(AccountTest, BasicOperations) {
    Account account(500.0);
    
    EXPECT_DOUBLE_EQ(account.getBalance(), 500.0);
    EXPECT_TRUE(account.hasEnoughBalance(500.0));
    EXPECT_FALSE(account.hasEnoughBalance(600.0));
    
    // Test deposit
    account.deposit(100.0);
    EXPECT_DOUBLE_EQ(account.getBalance(), 600.0);
    
    // Test withdraw
    EXPECT_TRUE(account.withdraw(200.0));
    EXPECT_DOUBLE_EQ(account.getBalance(), 400.0);
    
    // Test insufficient balance
    EXPECT_FALSE(account.withdraw(500.0));
    EXPECT_DOUBLE_EQ(account.getBalance(), 400.0); // Should remain unchanged
}



TEST(GoodTest, QuantityManagement) {
    Good good(1, "Test Silver", 25.0, 50);
    
    // Test reduce quantity
    EXPECT_TRUE(good.reduceQuantity(20));
    EXPECT_EQ(good.getQuantity(), 30);
    
    // Test insufficient quantity
    EXPECT_FALSE(good.reduceQuantity(40));
    EXPECT_EQ(good.getQuantity(), 30); // Should remain unchanged
    
    // Test increase quantity
    good.increaseQuantity(15);
    EXPECT_EQ(good.getQuantity(), 45);
    
    // Test invalid operations
    EXPECT_FALSE(good.reduceQuantity(0));
    EXPECT_FALSE(good.reduceQuantity(-5));
    good.increaseQuantity(-10); // Should be ignored
    EXPECT_EQ(good.getQuantity(), 45);
}

TEST(GoodTest, PriceUpdates) {
    Good good(1, "Test Platinum", 100.0, 25);
    
    // Test price update
    good.updatePrice(120.0);
    EXPECT_DOUBLE_EQ(good.getCurrentPrice(), 120.0);
    
    // Test invalid price (should be ignored)
    good.updatePrice(-10.0);
    EXPECT_DOUBLE_EQ(good.getCurrentPrice(), 120.0);
    
    good.updatePrice(0.0);
    EXPECT_DOUBLE_EQ(good.getCurrentPrice(), 120.0);
}

TEST(MarketTest, UserLogout) {
    Market market;
    
    // Registriere und logge einen Benutzer ein
    market.registerUser("testuser", "password123");
    EXPECT_TRUE(market.loginUser("testuser", "password123"));
    
    // Überprüfe, ob der Benutzer eingeloggt ist
    EXPECT_TRUE(market.isUserLoggedIn("testuser"));
    
    // Führe einen erfolgreichen Logout durch
    EXPECT_TRUE(market.logout("testuser", "password123"));
    EXPECT_FALSE(market.isUserLoggedIn("testuser"));
    
    // Versuche, mit falschem Passwort auszuloggen (sollte fehlschlagen)
    EXPECT_FALSE(market.logout("testuser", "wrongpassword"));
}

