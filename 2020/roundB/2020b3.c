#include <stdio.h>
#include <stdlib.h>

const long long R = 1000000000;
char s[2000];

void f(char *s, int l, int r, long long *x, long long *y) {
    int i;
    for (i = l; i <= r; ) {
        switch (s[i]) {
            case 'S': *x = (*x + 1) % R; i ++; break;
            case 'W': *y = (*y - 1) % R; i ++; break;
            case 'N': *x = (*x - 1) % R; i ++; break;
            case 'E': *y = (*y + 1) % R; i ++; break;
            default: {
                long long times = (long long)(s[i] - '0');
                int j, k = 0;
                for (j = i + 1; ; j ++) {
                    if (s[j] == '(') k ++;
                    if (s[j] == ')') k --;
                    if (k == 0) break;
                }
                long long dx = 0, dy = 0;
                f(s, i + 2, j - 1, &dx, &dy);
                *x = (*x + times * dx) % R;
                *y = (*y + times * dy) % R;
                i = j + 1;
            }
        }
    }
/*
    for (i = l; i <= r; i ++) {
        printf("%c", s[i]);
    }
    printf(": %lld %lld\n", *x, *y);
*/
}

int main() {
    int T;
    scanf("%d", &T);
    int t;
    for (t = 1; t <= T; t ++) {
        scanf("%s", s);
        int len = strlen(s);
        long long x = 0, y = 0;
        f(s, 0, len - 1, &x, &y);
        while (x < 0) x += R;
        while (y < 0) y += R;
        x = x % R;
        y = y % R;
        x ++; y ++;
        printf("Case #%d: %lld %lld\n", t, y, x);
    }
    return 0;
}
