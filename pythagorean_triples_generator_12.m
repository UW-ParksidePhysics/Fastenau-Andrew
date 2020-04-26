% Author: Andrew Fastenau with help from the titan Paul Rizzo!
C = input('Largest c value? '); % C = 1000
op = fopen('pythagorean_triples.txt', 'wt');

m = 1;
n = 1;
while m < C
    while n < C
        a = m ^ 2 - n ^ 2;
        b = 2 * m * n;
        c = m ^ 2 + n ^ 2;
        if c > C
            break
        end
        if m == n
            break
        end
        if gcd(m, n) == 1  % Checks to see if m and n are coprime
            if ~rem(m, 2) == 0  % Checks to see if m is odd
                if ~rem(n, 2) == 0  % Checks to see if n is odd
                else
                    fprintf(op, '%d %d %d\n', a, b, c);
                end
            else
                fprintf(op, '%d %d %d\n', a, b, c);
            end
        end
        n = n + 1;
    end
    m = m + 1;
    n = 1;
end
fclose(op);

type pythagorean_triples.txt