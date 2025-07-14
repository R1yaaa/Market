#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../include/market.hpp"
#include "../include/good.hpp"
#include "../include/user.hpp"
#include "../include/account.hpp"
#include <string>
#include <memory>

namespace py = pybind11;

PYBIND11_MODULE(unolib, m) {
    m.doc() = "Marketplace bindings";  // Fixed: Use .doc() instead of -doc()

    // Market class
    py::class_<Market, std::shared_ptr<Market>>(m, "Market")
        .def(py::init<>())
        .def("getUser", &Market::getUser)
        .def("registerUser", &Market::registerUser)
        .def("loginUser", &Market::loginUser)
        .def("updatePrices", &Market::updatePrices)
        .def("getGoods", &Market::getGoods)
        .def("getGood", &Market::getGood)
        .def("buyGood", &Market::buyGood)
        .def("sellGood", &Market::sellGood)
        .def("logout", &Market::logout);

    // User class - Fixed: Remove py::init<>() and use proper constructor
    py::class_<User, std::shared_ptr<User>>(m, "User")
        .def(py::init<const std::string&, const std::string&>())  // Use actual constructor
        .def("authenticate", &User::authenticate)
        .def("getInventory", &User::getInventory)
        .def("getGoodQuantity", &User::getGoodQuantity)
        .def("getAccount", &User::getAccount)
        .def("getUsername", &User::getUsername);

    // Account class - Fixed: Remove py::init<>() and use proper constructor
    py::class_<Account, std::shared_ptr<Account>>(m, "Account")
        .def(py::init<double>())  // Use actual constructor with initial_balance
        .def("getBalance", &Account::getBalance)
        .def("hasEnoughBalance", &Account::hasEnoughBalance)
        .def("deposit", &Account::deposit)
        .def("withdraw", &Account::withdraw);

    // Good class - Fixed: Remove py::init<>() and use proper constructor
    py::class_<Good, std::shared_ptr<Good>>(m, "Good")
        .def(py::init<int, const std::string&, double, int>())  // Use actual constructor
        .def("getId", &Good::getId)
        .def("getName", &Good::getName)
        .def("getQuantity", &Good::getQuantity)
        .def("getCurrentPrice", &Good::getCurrentPrice)
        .def("updatePrice", &Good::updatePrice)
        .def("hasEnoughQuantity", &Good::hasEnoughQuantity);
}