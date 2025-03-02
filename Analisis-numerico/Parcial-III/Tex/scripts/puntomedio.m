format rational

% Creamos la función f
f = @(x) 4 ./ (1 + x.^2);

% Parámetros de la integral y el método
a = 0;
b = 1;
valores_n = [10, 50, 100, 250, 500, 1000, 1500, 2000];
I_exacto = pi; 

% Se crea un vector para guardar los errores
errores = zeros(size(valores_n));

% Método del punto medio
tic;
for k = 1:length(valores_n)
    n = valores_n(k);
    % Aquí se encuentra el tamaño del intervalo
    h = (b - a) / n; 
    % Se calculan los puntos medios y los guarda en el vector x_medios
    x_medios = a + ((2*(0:1:n-1)+1)*h)/2;
    % Regla del punto medio compuesta
    I_punto_medio = h * sum(f(x_medios)); 
    % Calculo del error
    errores(k) = abs(I_punto_medio - I_exacto);
end
tiempo = toc

% Graficar log-log del error vs n
figure;
loglog(valores_n, errores, '-o', 'LineWidth', 2);
xlabel('n');
ylabel('Error absoluto');
ylim([1e-16, 1e-2]);
title('Error absoluto vs número de subintervalos (Punto Medio)');
grid on;
