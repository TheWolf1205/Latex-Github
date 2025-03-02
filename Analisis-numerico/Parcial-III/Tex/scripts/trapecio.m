format rational

% Creamos la función f
f = @(x) 4 ./ (1 + x.^2);

% Parámetros de la integral y el método
a = 0;
b = 1;
valores_n = [10, 50, 100, 250, 500, 1000, 1500, 2000];
I_exacto = pi; 

% Se crea un vector para guardar los errores
errores_trapecio = zeros(size(valores_n));

% Método del trapecio
for k = 1:length(valores_n)
    n = valores_n(k);
    h = (b - a) / n;
    % Extremos de la partición
    x_extremos = a:h:b;
    m = length(x_extremos);

    % Aplicar la regla del trapecio compuesta
    I_trapecio = (h/2) * (f(a) + 2*sum(f(x_extremos(2:m-1))) + f(b));

    % Calculo del error
    errores_trapecio(k) = abs(I_trapecio - I_exacto);
end

% Graficar error del método del trapecio
figure;
loglog(valores_n, errores_trapecio, '-o', 'LineWidth', 2);
xlabel('n');
ylabel('Error absoluto');
ylim([1e-16, 1e-2]);
title('Error absoluto vs número de subintervalos (Trapecio)');
grid on;