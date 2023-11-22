function [a] = vander(x, y)
    
    if length(x) ~= length(y)
        error('x e y deben tener el mismo tamaño');
    end

    n = length(x) - 1;

    A = ones(length(x), n + 1);
    for i = 1:n
        A(:, n + 1 - i) = x.^i;
    end

    b = y
    a = inv(A)*b  

    %xpol = linspace(min(x), max(x), 100);
    
    %p = [zeros(size(xpol))];
    %for i = 1:length(a)
    %    p = p + a(i) * xpol.^(n + 1 - i);
    %end

    %plot(x, y, 'r*', xpol, p, 'b-');
    %hold on;
    %grid on;

end