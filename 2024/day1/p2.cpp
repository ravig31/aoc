#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>

int main() {
    std::fstream file("input.txt");

    if (!file.is_open()) {
        std::cerr << "File open error!\n";
        return 1;
    }
    std::vector<int> l1{};
    std::unordered_map<int, int> cnt1{};
    std::unordered_map<int, int> cnt2{};

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        int n1, n2;
        iss >> n1 >> n2;
		l1.push_back(n1);
		cnt1[n1] += 1;
		cnt2[n2] += 1;
    }
	
    int ans = 0;
	for (const auto num : l1){
		if (cnt2.contains(num)) {
			ans += num * cnt2[num];
		}
	}

	std::cout << "ans: " << ans << "\n";
}