#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::fstream file("input.txt");

    if (!file.is_open()) {
        std::cerr << "File open error!\n";
        return 1;
    }

    std::vector<int> l1{};
    std::vector<int> l2{};

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        int n1, n2;
        iss >> n1 >> n2;
        l1.push_back(n1);
        l2.push_back(n2);
    }

    std::sort(l1.begin(), l1.end());
    std::sort(l2.begin(), l2.end());

    int ans = 0;
    int n = l1.size();
    for (int i=0; i<n; i++){
		ans += abs(l1[i] - l2[i]);
	}

	std::cout << "ans: " << ans << "\n";
}