#include <iostream>
#include <climits> // For INT_MAX and INT_MIN

class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            int temp = x % 10;

            // Check for overflow
            if (ans > INT_MAX / 10 || ans < INT_MIN / 10) {
                return 0;
            }

            ans = (ans * 10) + temp;
            x = x / 10;
        }
        return ans;
    }
};

int main() {
    Solution solution;
    int x;
    
    std::cout << "Enter an integer to reverse: ";
    std::cin >> x;

    int result = solution.reverse(x);
    std::cout << "Reversed integer: " << result << std::endl;

    return 0;
}
