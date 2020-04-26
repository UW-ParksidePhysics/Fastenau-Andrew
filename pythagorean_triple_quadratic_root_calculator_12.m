% Author: Andrew Fastenau with help from the one and only Paul Rizzo!
fileID = fopen('pythagorean_triples.txt','r');
op = fopen('pythagorean_triple_quadratic_roots.txt', 'wt');
formatSpec = '%d %d %d\n';
sizeA = [3 Inf];
[A, count] = fscanf(fileID, formatSpec, sizeA);

n = 1;
while n <= count/3
    a = A(1, n);
    b = A(2, n);
    c = A(3, n);
    
    D2 = b ^ 2 - 4 * a * c;
    if a == 0
       disp('a Cannot Equal Zero')
    end
    
    if D2 >= 0  % test_roots_float
        D = sqrt(D2);
        x1 = round((-b - D) / (2 * a));
        x2 = round((2 * c) / (-b - D));
        R = [x1, x2];
        fprintf(op, '%d %d %d ', a, b, c);fprintf(op, '%d ', R);fprintf(op, '\n');
    
    elseif D2 < 0  % test_roots_complex
        D2 = -D2;
        D = round((sqrt(D2) / (2 * a)), 3);
        b2 = round(-b / (2 * a), 3);
        fprintf(op, '%d %d %d ', a, b, c);fprintf(op, '%g %s %g %s',b2, '+', D, 'i');fprintf(op, '%g %s %g %s\n', b2, '-', D, 'i');
    end
    n = n + 1;
end

type pythagorean_triple_quadratic_roots.txt