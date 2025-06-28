#pragma once
#include <string>
#include <vector>
#include <chrono>
#include <memory>

struct ChatMessage {
    std::string username;
    std::string message;
    std::chrono::system_clock::time_point timestamp;
    
    ChatMessage(const std::string& user, const std::string& msg);
};

class Chat {
public:
    using Ptr = std::shared_ptr<Chat>;
    
    Chat();
    
    // Nachrichten
    void addMessage(const std::string& username, const std::string& message);
    std::vector<ChatMessage> getMessages() const;
    std::vector<ChatMessage> getRecentMessages(int count) const;
    
    // Für Polling
    std::vector<ChatMessage> getMessagesSince(
        std::chrono::system_clock::time_point since
    ) const;

private:
    std::vector<ChatMessage> messages;
};