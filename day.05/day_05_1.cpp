#include <iostream>
#include <string>
#include <list>

bool isUpper(char c) {
    return c >= 'A' && c <= 'Z';
}

bool isLower(char c) {
    return c >= 'a' && c <= 'z';
}

int dist(char c) {
    if (isUpper(c)) {
        return c - 'A';
    } else {
        return c - 'a';
    }
}

bool opposite(char a, char b) {
    if (isUpper(a) && isUpper(b)) {
        return false;
    }
    if (isLower(a) && isLower(b)) {
        return false;
    }

    return dist(a) == dist(b);
}

void generate(std::list<char>& material, std::string input) {
    for (int i = 0; i < input.length(); i++) {
        material.push_back(input[i]);
    }
}

void react(std::list<char>& material) {
    for (auto iter = material.begin(); iter != material.end(); ) {
        
        iter++;
        if (iter == material.end()) {
            break;
        }

        char next = *iter;

        iter--;

        if (opposite(*iter, next)) {
            iter = material.erase(iter);
            iter = material.erase(iter);
        } else {
            iter++;
        }
    }
}

void print(std::list<char>& list) {
    for (auto iter = list.begin(); iter != list.end(); iter++) {
        std::cout << *iter;
    }
    std::cout << std::endl;
}

int getShortest(std::list<char>& material) {
    int lastLength = material.size();
    do {
        lastLength = material.size();
        react(material);
        // print(material);
    } while (lastLength != material.size());
    return lastLength;
}

int main() {
    std::string input;
    getline(std::cin, input);

    std::list<char> material;
    generate(material, input);
    int shortest = getShortest(material);

    std::cout << shortest << std::endl;

    return 0;
}
