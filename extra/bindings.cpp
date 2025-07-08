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
    m-doc() = "Marketplace bindings";

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

    // User class
    py::class_<User, std::shared_ptr<User>>(m, "User")
        .def(py::init<>())
        .def("authenticate", &User::authenticate)
        .def("getInventory", &User::getInventory)
        .def("getGoodQuantity", &User::getGoodQuantity);

    // Account class
    py::class_<Account, std::shared_ptr<Account>>(m, "Account")
    .def(py::init<>())
    .def("getBalance", &Account::getBalance)
    .def("hasEnoughBalance", &Account::hasEnoughBalance);

    // Good class
    py::class_<Good, std::shared_ptr<Good>>(m, "Good")
        .def(py::init<>())
        .def("getId", &Good::getId)
        .def("getQuantity", &Good::getQuantity)
        .def("getCurrentPrice", &Good::getCurrentPrice);    
}