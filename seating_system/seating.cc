#include <iostream>
#include <set>
#include <vector>

using namespace std;

void show(vector<string> G) {
  for (int i = 0; i < G.size(); i++) {
    for (int j = 0; j < G[0].size(); j++) {
      printf("%c", G[i][j]);
    }
    puts("");
  }
  puts("");
}

vector<string> step(vector<string> G) {
  vector<string> next_state = G;

  for (int i = 0; i < G.size(); i++) {
    for (int j = 0; j < G[0].size(); j++) {
      if (G[i][j] == '.') {
        continue;
      }

      int empty = 0;
      int occ = 0;

      if (i - 1 >= 0) {
        if ((G[i-1][j]) == '#') {
          occ++;
        } else if ((G[i-1][j]) == 'L') {
          empty++;
        }
      }

      if (i + 1 < G.size()) {
        if ((G[i+1][j]) == '#') {
          occ++;
        } else if ((G[i+1][j]) == 'L') {
          empty++;
        }
      }

      if (j + 1 < G[0].size()) {
        if ((G[i][j+1]) == '#') {
          occ++;
        } else if ((G[i][j+1]) == 'L') {
          empty++;
        }
      }

      if (j - 1 >= 0) {
        if ((G[i][j-1]) == '#') {
          occ++;
        } else if ((G[i][j-1]) == 'L') {
          empty++;
        }
      }

      if (j - 1 >= 0 && i + 1 < G.size()) {
        if ((G[i+1][j-1]) == '#') {
          occ++;
        } else if ((G[i+1][j-1]) == 'L') {
          empty++;
        }
      }

      if (j - 1 >= 0 && i - 1 >= 0) {
        if ((G[i-1][j-1]) == '#') {
          occ++;
        } else if ((G[i-1][j-1]) == 'L') {
          empty++;
        }
      }

      if (j + 1 < G[0].size() && i + 1 < G.size()) {
        if ((G[i+1][j+1]) == '#') {
          occ++;
        } else if ((G[i+1][j+1]) == 'L') {
          empty++;
        }
      }

      if (j + 1 < G[0].size() && i - 1 < G.size()) {
        if ((G[i-1][j+1]) == '#') {
          occ++;
        } else if ((G[i-1][j+1]) == 'L') {
          empty++;
        }
      }

      if (G[i][j] == 'L' && occ == 0) {
        next_state[i][j] = '#';
      } else if (G[i][j] == '#' && occ >= 4) {
        next_state[i][j] = 'L';
      }

    }
  }
  return next_state;
}


int main() {
  char ch;
  vector<string> G;
  for (string line; getline(cin, line);) {
    G.push_back(line);
  }


  set<vector<string>> seen;
  while (!seen.count(G)) {
    seen.insert(G);
    // show(G);
    G = step(G);
  }

  int ret = 0;
  for (int i = 0; i < G.size(); i++) {
    for (int j = 0; j < G[0].size(); j++) {
      if (G[i][j] == '#') {
        ret++;
      }
    }
  }
  printf("%d\n", ret);
}
