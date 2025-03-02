format rational
% Creamos la función f
f = @(x) 4 ./ (1 + x.^2);
% Parámetros de la integral y el método
a = 0;
b = 1;
valores_n = [10, 50, 100, 250, 500, 1000, 1500, 2000];
I_exacto = pi; 
% Se crea un vector para guardar los errores
errores_simpson = zeros(size(valores_n));
% Método de Simpson
tic;
for k = 1:length(valores_n)
    n = valores_n(k);
    % Aquí nos aseguramos que n sea par (Simpson necesita n par)
    if mod(n, 2) == 1
        n = n + 1;
    end
    h = (b - a) / n;
    % Extremos de la partición
    x_extremos = a:h:b;
    m = length(x_extremos);
    % Aplicar la regla de Simpson compuesta
    I_simpson = (h/3) * (f(a) + 4*sum(f(x_extremos(2:2:m-1))) + 2*sum(f(x_extremos(3:2:m-2))) + f(b));
    % Calculo del error
    errores_simpson(k) = abs(I_simpson - I_exacto);
end
tiempo = toc
% Graficar error del método de Simpson
figure;
loglog(valores_n, errores_simpson, '-o', 'LineWidth', 2);
xlabel('n');
ylabel('Error absoluto');
ylim([1e-16, 1e-2]); 
title('Error absoluto vs número de subintervalos (Simpson)');
grid on;
