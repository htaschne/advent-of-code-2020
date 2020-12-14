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

void scan(vector<string> &G, int *e, int *o, int ii, int jj) {
  int empty = 0;
  int occ = 0;

  int i = ii;
  int j = jj;
  while (i - 1 >= 0) {
    if ((G[i - 1][j]) == '#') {
      occ++;
      break;
    } else if ((G[i - 1][j]) == 'L') {
      empty++;
      break;
    }
    i--;
  }

  i = ii;
  while (i + 1 < G.size()) {
    if ((G[i + 1][j]) == '#') {
      occ++;
      break;
    } else if ((G[i + 1][j]) == 'L') {
      empty++;
      break;
    }
    i++;
  }

  i = ii;
  while (j - 1 >= 0) {
    if ((G[i][j - 1]) == '#') {
      occ++;
      break;
    } else if ((G[i][j - 1]) == 'L') {
      empty++;
      break;
    }
    j--;
  }

  j = jj;
  while (j + 1 < G[0].size()) {
    if ((G[i][j + 1]) == '#') {
      occ++;
      break;
    } else if ((G[i][j + 1]) == 'L') {
      empty++;
      break;
    }
    j++;
  }

  j = jj;
  while (j - 1 >= 0 && i + 1 < G.size()) {
    if ((G[i + 1][j - 1]) == '#') {
      occ++;
      break;
    } else if ((G[i + 1][j - 1]) == 'L') {
      empty++;
      break;
    }
    j--;
    i++;
  }

  i = ii;
  j = jj;
  while (j - 1 >= 0 && i - 1 >= 0) {
    if ((G[i - 1][j - 1]) == '#') {
      occ++;
      break;
    } else if ((G[i - 1][j - 1]) == 'L') {
      empty++;
      break;
    }
    j--;
    i--;
  }

  i = ii;
  j = jj;
  while (j + 1 < G[0].size() && i + 1 < G.size()) {
    if ((G[i + 1][j + 1]) == '#') {
      occ++;
      break;
    } else if ((G[i + 1][j + 1]) == 'L') {
      empty++;
      break;
    }
    j++;
    i++;
  }

  i = ii;
  j = jj;
  while (j + 1 < G[0].size() && i - 1 < G.size()) {
    if ((G[i - 1][j + 1]) == '#') {
      occ++;
      break;
    } else if ((G[i - 1][j + 1]) == 'L') {
      empty++;
      break;
    }
    j++;
    i--;
  }

  *e = empty;
  *o = occ;
}

void step(vector<string> &G) {
  vector<string> next_state = G;
  for (int i = 0; i < G.size(); i++) {
    for (int j = 0; j < G[0].size(); j++) {
      if (G[i][j] == '.') {
        continue;
      }

      int empty = 0;
      int occ = 0;
      scan(G, &empty, &occ, i, j);

      if (G[i][j] == 'L' && occ == 0) {
        next_state[i][j] = '#';
      } else if (G[i][j] == '#' && occ >= 5) {
        next_state[i][j] = 'L';
      }
    }
  }
  G = next_state;
}

int main() {
  vector<string> G;
  for (string line; getline(cin, line);)
    G.push_back(line);

  set<vector<string>> seen;
  while (!seen.count(G)) {
    seen.insert(G);
    // show(G);
    step(G);
  }

  int ret = 0;
  for (int i = 0; i < G.size(); i++)
    for (int j = 0; j < G[0].size(); j++)
      if (G[i][j] == '#')
        ret++;
  printf("%d\n", ret);
}
