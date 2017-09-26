//Christopher Paterno Ram Hacks Novice 1 Challenge Fall 2017
#include <iostream>
#include <cstdlib>
#include <string>

int main(int argc, char *argv[]) {
    if (argc != 2) {
      return 1;
    }
    int n = atoi(argv[1]);
    int mod1 = 5;
    int mod2 = 7;
    std::string r = "RAM";
    std::string h = "Hacks";
    std::string rh = "RAMHacks";
    for (int i = 1; i <= n; i++) {
      if (i % mod1 == 0 && i % mod2 == 0) {
        std::cout << rh << std::endl;
      }
      else if (i % mod1 == 0) {
        std::cout << r << std::endl;
      }
      else if (i % mod2 == 0) {
        std::cout << h << std::endl;
      }
      else {
        std::cout << i << std::endl;
      }
    }
    return 0;
}
